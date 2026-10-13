import sys
import unittest
from pathlib import Path
import numpy as np
from lifelines import KaplanMeierFitter
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from guyot import reconstruct,step_at


class GuyotTests(unittest.TestCase):
    def test_uncensored_known_events(self):
        ipd,_=reconstruct([0,1,2,4],[1,.75,.5,0],[0,3,6],[4,2,0],4)
        self.assertEqual(int(ipd.event.sum()),4)
        np.testing.assert_allclose(KaplanMeierFitter().fit(ipd.time_months,ipd.event).predict([1,2,4]),[.75,.5,0])

    def test_all_censored(self):
        ipd,audit=reconstruct([0,6],[1,1],[0,3,6,9],[8,4,1,0],0)
        self.assertEqual(len(ipd),8)
        self.assertEqual(int(ipd.event.sum()),0)
        self.assertTrue(np.isinf(KaplanMeierFitter().fit(ipd.time_months,ipd.event).median_survival_time_))
        self.assertEqual(int((ipd.time_months>=3).sum()),4)

    def test_empty_interval(self):
        ipd,audit=reconstruct([0,1,3,6,7,8],[1,.9,.9,.9,.8,.8],[0,3,6,9],[10,8,8,0],2)
        row=audit.iloc[1]
        self.assertEqual(row.events,0)
        self.assertEqual(row.censors,0)

    def test_boundary_event(self):
        ipd,_=reconstruct([0,3,6],[1,.8,.6],[0,3,6,9],[10,10,8,0],4)
        self.assertEqual(int((ipd.time_months>=3).sum()),10)
        self.assertEqual(int((ipd.time_months>=6).sum()),8)

    def test_step_is_right_continuous(self):
        np.testing.assert_array_equal(step_at([0,2,4],[1,.8,.5],[-1,0,1,2,3,4]),[1,1,1,.8,.8,.5])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            reconstruct([0,1,2],[1,.5,.6],[0,3],[10,0],5)
        with self.assertRaises(ValueError):
            reconstruct([0,1],[1,.5],[0,3],[10,11],5)

    def test_reproducible(self):
        args=([0,1,2,4,6],[1,.9,.8,.6,.6],[0,3,6,9],[10,6,1,0],4)
        a,_=reconstruct(*args)
        b,_=reconstruct(*args)
        self.assertTrue(a.equals(b))
        self.assertTrue((a.time_months<=6).all())


if __name__=='__main__':
    unittest.main()