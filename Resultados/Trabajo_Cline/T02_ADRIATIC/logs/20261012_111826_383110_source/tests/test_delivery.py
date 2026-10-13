"""Integration checks on generated files; run after pipeline --stage all."""
import hashlib
import json
import sys
import unittest
from pathlib import Path
import numpy as np
import pandas as pd
import yaml
from lifelines import KaplanMeierFitter

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from validate import numbers
from reporting import table


class DeliveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.out=ROOT/'data_derived'
        cls.cfg=yaml.safe_load((ROOT/'config/config.yaml').read_text(encoding='utf-8'))

    def test_source_identity(self):
        pdf=Path(self.cfg['project_root'])/self.cfg['pdf_relative']
        self.assertEqual(hashlib.sha256(pdf.read_bytes()).hexdigest(),'44b9eb70e00ad09bd8d80c014b585dd85f6a2a8f1ac1e6b8bdd3d68503234d0c')

    def test_parsing_and_nonreached_display(self):
        self.assertEqual(numbers('55.9 (37.3–NR)'),[55.9,37.3])
        self.assertEqual(numbers('68.0 (61.9–73.3)'),[68.,61.9,73.3])
        rendered=table(pd.DataFrame({'value':[np.inf,np.nan]}))
        self.assertIn('NR',rendered)
        self.assertIn('—',rendered)

    def test_four_clinical_populations_and_support(self):
        audit=json.loads((self.out/'extraction_audit.json').read_text(encoding='utf-8'))
        for ep in self.cfg['pages']:
            for arm,n in [('durvalumab',264),('placebo',266)]:
                ipd=pd.read_csv(self.out/f'pseudo_ipd_{ep}_{arm}.csv')
                points=pd.read_csv(self.out/f'points_{ep}_{arm}.csv')
                self.assertEqual(list(ipd.columns),['time_months','event','arm','endpoint'])
                self.assertEqual(len(ipd),n)
                self.assertTrue(ipd.event.isin([0,1]).all())
                self.assertTrue(np.isfinite(ipd.time_months).all())
                self.assertTrue(ipd.time_months.between(0,audit[f'{ep}_{arm}']['support_end']+1e-9).all())
                self.assertEqual(points.survival.iloc[0],1)
                self.assertTrue((points.survival.diff().dropna()<=0).all())
                self.assertTrue(ipd.arm.eq(arm).all() and ipd.endpoint.eq(ep).all())

    def test_h1_and_all_risks_are_calculated(self):
        validation=pd.read_csv(self.out/'validation.csv')
        h1=validation[validation.scope=='H1']
        self.assertEqual(len(h1),18)
        self.assertEqual(len(validation[validation.scope=='riesgo']),88)
        self.assertEqual(len(validation[validation.quantity.str.startswith('seguimiento_censurados_')]),12)
        self.assertFalse(h1[['published','reconstructed','tolerance']].isna().any().any())
        for row in h1.itertuples():
            expected='reproducido' if abs(row.reconstructed-row.published)<=row.tolerance+1e-12 else 'discrepancia'
            self.assertEqual(row.classification,expected)
        for ep in self.cfg['pages']:
            for arm in self.cfg['colors']:
                ipd=pd.read_csv(self.out/f'pseudo_ipd_{ep}_{arm}.csv')
                km=KaplanMeierFitter().fit(ipd.time_months,ipd.event)
                subset=validation[(validation.endpoint==ep)&(validation.arm==arm)]
                for row in subset[subset.scope=='riesgo'].itertuples():
                    time=float(row.quantity.split('_')[1])
                    self.assertEqual(row.reconstructed,int((ipd.time_months>=time).sum()))
                for row in subset[subset.quantity.str.match(r'^S_\d+$')].itertuples():
                    self.assertAlmostEqual(row.reconstructed,float(km.predict(float(row.quantity[2:]))))

    def test_slp_empty_interval(self):
        for arm in self.cfg['colors']:
            intervals=pd.read_csv(self.out/f'intervals_SLP_{arm}.csv')
            row=intervals[(intervals.start==30)&(intervals.end==33)].iloc[0]
            self.assertEqual(row.events,0)
            self.assertEqual(row.censors,0)

    def test_complete_simulation_and_truth(self):
        metrics=pd.read_csv(self.out/'simulation_metrics.csv')
        populations=pd.read_csv(self.out/'simulation_populations.csv')
        self.assertEqual(len(metrics),1800)
        self.assertEqual(len(populations),400)
        self.assertEqual(set(metrics.replicate),set(range(100)))
        self.assertTrue((metrics.groupby('replicate').size()==18).all())
        self.assertTrue((metrics.seed==self.cfg['seed']+metrics.replicate).all())
        self.assertFalse(metrics.duplicated(['replicate','endpoint','arm','quantity']).any())
        for row in populations.itertuples():
            stem=f'{row.replicate:03d}_{row.endpoint}_{row.arm}'
            truth=pd.read_csv(self.out/'simulation'/f'truth_{stem}.csv')
            rec=pd.read_csv(self.out/'simulation'/f'reconstructed_{stem}.csv')
            intervals=pd.read_csv(self.out/'simulation'/f'intervals_{stem}.csv')
            self.assertEqual(len(truth),row.n)
            self.assertEqual(len(rec),row.n)
            self.assertEqual(truth.event.sum(),row.events)
            self.assertTrue(rec.time_months.between(0,truth.time_months.max()+1e-9).all())
            self.assertEqual(intervals.events.sum(),rec.event.sum())
            self.assertEqual(intervals.censors.sum(),len(rec)-rec.event.sum())
        summary=pd.read_csv(self.out/'simulation_summary.csv')
        for row in summary.itertuples():
            group=metrics[(metrics.endpoint==row.endpoint)&(metrics.quantity==row.quantity)]
            valid=group[group.evaluable]
            self.assertEqual(row.total,len(group))
            self.assertEqual(row.evaluable,len(valid))
            self.assertEqual(row.within_tolerance,int(valid.within_tolerance.sum()))
            self.assertAlmostEqual(row.mae,float(valid.error.abs().mean()))

    def test_deliverables_exist(self):
        for name in ['INFORME_T02.md','ENTREGA_LISTA.md','REPRODUCIR.md','requirements_T02.txt','data_derived/PROCEDENCIA.md']:
            self.assertGreater((ROOT/name).stat().st_size,0)
        for stem in ['overlay_SG','overlay_SLP','differences_SG','differences_SLP','simulation_E20']:
            for ext in ['png','svg']:
                self.assertGreater((ROOT/'figures'/f'{stem}.{ext}').stat().st_size,1000)


if __name__=='__main__':
    unittest.main()