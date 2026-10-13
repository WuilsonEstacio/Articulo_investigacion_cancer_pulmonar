"""D1 independent level count and ties; D2 genuine PDF round-trip and replay."""
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
import yaml
from lifelines import KaplanMeierFitter

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from extract import extract_pdf,polygon_plateaus
from vector_simulation import FigureGeometry
from simulate import generate
from round1 import cox_ties
from validate import fit_cox


class Round1UnitTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg=yaml.safe_load((ROOT/'config/config.yaml').read_text(encoding='utf-8'))

    def test_substroke_plateaus_and_broken_pair(self):
        # Every middle plateau is shorter than stroke width and has no
        # overlap between its upper and lower horizontal edges.
        xs=[0,2,2.10,2.20,2.30,5]
        ys=[10,11,12,13,14]
        h=.251
        upper=[]
        lower=[]
        for i,y in enumerate(ys):
            upper.extend([(xs[i]+(h if i else 0),y-h),(xs[i+1]+(h if i+1<len(ys) else 0),y-h)])
            lower.extend([(xs[i]-(h if i else 0),y+h),(xs[i+1]-(h if i+1<len(ys) else 0),y+h)])
        vertices=upper+list(reversed(lower))
        seg=[(i,a,b) for i,(a,b) in enumerate(zip(vertices,vertices[1:]+vertices[:1]))]
        result=polygon_plateaus(seg)
        self.assertEqual(len(result),len(ys))
        np.testing.assert_allclose([p['y'] for p in result],ys)
        np.testing.assert_allclose([p['left'] for p in result],xs[:-1])
        # Removing an intermediate edge must fail, not silently fuse steps.
        with self.assertRaises(ValueError):
            polygon_plateaus([s for s in seg if s[0]!=4])

    def test_pdf_roundtrip_shared_extractor(self):
        cfg=self.cfg
        rng=np.random.default_rng(cfg['seed'])
        pair={arm:generate(rng,n,f'SG_{arm}',cfg['simulation']) for arm,n in [('durvalumab',264),('placebo',266)]}
        geometry=FigureGeometry(cfg)
        with tempfile.TemporaryDirectory(dir=ROOT/'logs',prefix='round1_test_') as temp:
            directory=Path(temp)
            pdf=directory/'km.pdf'
            geometry.render(pdf,pair,cfg)
            curves,audit=extract_pdf(pdf,dict(cfg,pages={'SG':1}),directory)
            geometry.render(directory/'replay.pdf',pair,cfg)
            self.assertEqual(pdf.read_bytes(),(directory/'replay.pdf').read_bytes())
            for arm,truth in pair.items():
                point=curves['SG',arm]
                km=KaplanMeierFitter().fit(truth.time_months,truth.event)
                sf=km.survival_function_.iloc[:,0]
                change=np.r_[True,np.diff(sf.to_numpy())<0]
                plateau=point[point.kind=='plateau']
                self.assertEqual(len(plateau),int(change.sum()))
                np.testing.assert_allclose(plateau.time_months,sf.index.to_numpy()[change],atol=1e-4,rtol=0)
                np.testing.assert_allclose(plateau.survival,sf.to_numpy()[change],atol=1e-5,rtol=0)
                self.assertAlmostEqual(point.time_months.iloc[-1],truth.time_months.max(),places=4)
                self.assertAlmostEqual(audit[f'SG_{arm}']['x_scale'],geometry.ax,places=5)
                self.assertAlmostEqual(audit[f'SG_{arm}']['y_scale'],geometry.ay,places=3)
                marks=pd.read_csv(directory/f'censor_marks_SG_{arm}.csv')
                self.assertGreater(len(marks),0)
                self.assertLessEqual(len(marks),int((truth.event==0).sum()))

    def test_cox_efron_breslow(self):
        pair={'durvalumab':pd.DataFrame({'time_months':[1,2,3,5,8,10],'event':[1,1,0,1,0,1]}),
              'placebo':pd.DataFrame({'time_months':[1,2,4,6,7,9],'event':[1,1,1,0,1,0]})}
        self.assertAlmostEqual(cox_ties(pair,'efron'),fit_cox(pair)['hr'],places=5)
        self.assertGreater(abs(cox_ties(pair,'efron')-cox_ties(pair,'breslow')),1e-5)
        no_ties={arm:d.assign(time_months=d.time_months+i*.1) for i,(arm,d) in enumerate(pair.items())}
        self.assertAlmostEqual(cox_ties(no_ties,'efron'),cox_ties(no_ties,'breslow'),places=10)


class Round1DeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cfg=yaml.safe_load((ROOT/'config/config.yaml').read_text(encoding='utf-8'))
        cls.out=ROOT/'data_derived'

    def test_archived_original_and_unchanged_criteria(self):
        hashes=pd.read_csv(ROOT/'logs/ronda0_original_sha256.csv')
        self.assertEqual(len(hashes),1235)
        for row in hashes.itertuples():
            path=ROOT/'logs/ronda0_original'/row.file
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),row.sha256.lower(),str(path))
        for name in ['src/guyot.py','src/simulate.py','config/config.yaml','CRITERIOS_PREESPECIFICADOS.md']:
            self.assertEqual((ROOT/name).read_bytes(),(ROOT/'logs/ronda0_documentos'/name).read_bytes(),name)

    def test_polygon_levels_plateaus_and_maximum_tie_per_curve(self):
        ties=pd.read_csv(self.out/'round1_ties.csv')
        for ep in self.cfg['pages']:
            for arm in self.cfg['colors']:
                with self.subTest(endpoint=ep,arm=arm):
                    seg=pd.read_csv(self.out/f'segments_{ep}_{arm}.csv')
                    # Independent count from geometric levels: no call to the
                    # production pairing/count function, no IPD or H1 target.
                    levels={}
                    for sign in [1,-1]:
                        data=seg[(abs(seg.y2-seg.y1)<=.002)&((seg.x2-seg.x1)*sign>1e-6)]
                        vals=sorted(((data.y1+data.y2)/2).to_numpy())
                        unique=[]
                        for value in vals:
                            if not unique or value-unique[-1]>.002:
                                unique.append(value)
                        levels[sign]=unique
                    midpoints=[]
                    for a in levels[1]:
                        for b in levels[-1]:
                            if abs(b-a-.502)<=.0021:
                                midpoints.append((a+b)/2)
                    points=pd.read_csv(self.out/f'points_{ep}_{arm}.csv')
                    extracted=points[points.kind=='plateau']
                    self.assertEqual(len(midpoints),len(extracted))
                    np.testing.assert_allclose(extracted.y_pdf,midpoints,atol=.002,rtol=0)
                    paired=pd.read_csv(self.out/f'plateaus_{ep}_{arm}.csv')
                    self.assertEqual(len(paired),len(midpoints))
                    for version,directory in [('original',ROOT/'logs/ronda0_original'),('corregido',self.out)]:
                        ipd=pd.read_csv(directory/f'pseudo_ipd_{ep}_{arm}.csv')
                        events=ipd[ipd.event==1].groupby('time_months').size()
                        row=ties[(ties.version==version)&(ties.endpoint==ep)&(ties.arm==arm)].iloc[0]
                        self.assertEqual(row.max_tie,int(events.max()))
                        self.assertEqual(row.distinct_event_times,len(events))
                    before=ties[(ties.version=='original')&(ties.endpoint==ep)&(ties.arm==arm)].iloc[0]
                    after=ties[(ties.version=='corregido')&(ties.endpoint==ep)&(ties.arm==arm)].iloc[0]
                    self.assertGreater(after.plateaus,before.plateaus)
                    self.assertGreater(after.distinct_event_times,before.distinct_event_times)
                    self.assertLess(after.max_tie,before.max_tie)

    def test_e20a_preserved_byte_for_byte(self):
        original=ROOT/'logs/ronda0_original'
        files=list((original/'simulation').glob('*.csv'))+list(original.glob('simulation_*.csv'))
        self.assertEqual(len(files),1203)
        for path in files:
            target=self.out/path.relative_to(original)
            self.assertEqual(path.read_bytes(),target.read_bytes(),str(path))

    def test_e20b_all_replicates_same_truth_and_diagnostics(self):
        metrics=pd.read_csv(self.out/'simulation_b_metrics.csv')
        pop=pd.read_csv(self.out/'simulation_b_populations.csv')
        risks=pd.read_csv(self.out/'simulation_b_risks.csv')
        self.assertEqual(len(metrics),1800)
        self.assertEqual(len(pop),400)
        self.assertEqual(len(risks),8800)
        self.assertEqual(set(metrics.replicate),set(range(100)))
        self.assertTrue((metrics.seed==self.cfg['seed']+metrics.replicate).all())
        original_metrics=pd.read_csv(self.out/'simulation_metrics.csv')
        np.testing.assert_array_equal(metrics.tolerance,original_metrics.tolerance)
        np.testing.assert_array_equal(metrics.truth,original_metrics.truth)
        for row in pop.itertuples():
            directory=self.out/'simulation_b'/f'{row.replicate:03d}_{row.endpoint}'
            truth=directory/f'truth_{row.arm}.csv'
            original=self.out/'simulation'/f'truth_{row.replicate:03d}_{row.endpoint}_{row.arm}.csv'
            self.assertEqual(truth.read_bytes(),original.read_bytes())
            self.assertGreater((directory/'km.pdf').stat().st_size,1000)
            rec=pd.read_csv(directory/f'reconstructed_{row.arm}.csv')
            points=pd.read_csv(directory/f'points_{row.endpoint}_{row.arm}.csv')
            self.assertEqual(len(rec),row.n)
            self.assertTrue(rec.time_months.between(0,points.time_months.iloc[-1]+1e-9).all())
            self.assertEqual(row.plateaus,row.true_plateaus)
            self.assertEqual(row.max_tie,rec[rec.event==1].groupby('time_months').size().max())
            select=risks[(risks.replicate==row.replicate)&(risks.endpoint==row.endpoint)&(risks.arm==row.arm)]
            self.assertEqual(row.max_risk_error,select.difference.abs().max())
            self.assertAlmostEqual(row.mean_risk_error,select.difference.abs().mean())
            for r in select.itertuples():
                self.assertEqual(r.reconstructed,int((rec.time_months>=r.time_months).sum()))
        summary=pd.read_csv(self.out/'simulation_b_summary.csv')
        for row in summary.itertuples():
            group=metrics[(metrics.endpoint==row.endpoint)&(metrics.quantity==row.quantity)]
            valid=group[group.evaluable]
            self.assertEqual(row.total,len(group))
            self.assertEqual(row.within_tolerance,int(valid.within_tolerance.sum()))
            self.assertAlmostEqual(row.mae,float(valid.error.abs().mean()))

    def test_report_original_first_and_delivery_state(self):
        report=(ROOT/'INFORME_T02.md').read_text(encoding='utf-8')
        original=(ROOT/'logs/ronda0_documentos/INFORME_T02.md').read_text(encoding='utf-8')
        self.assertTrue(report.startswith(original))
        section=report.split('## Ronda 1 de corrección')[1]
        self.assertLess(section.index('#### Resultado original'),section.index('#### Resultado corregido'))
        self.assertIn('E2.0a: sin digitalización',section)
        self.assertIn('E2.0b:',section)
        self.assertIn('Estado: entregada (ronda 1)',(ROOT/'ENTREGA_LISTA.md').read_text(encoding='utf-8'))
        hrs=pd.read_csv(self.out/'round1_hr.csv')
        np.testing.assert_allclose(hrs.efron_lifelines,hrs.efron_score,atol=1e-5,rtol=0)


if __name__=='__main__':
    unittest.main()