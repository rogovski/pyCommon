import unittest
import numpy as np
from ..data import array as autil

class TestDataArrayMethods(unittest.TestCase):

  def test_map_rows(self):
      tdata = np.array([[1,2,3],
                        [4,5,6]])
      res = autil.maprows(lambda row: row + 1, tdata)
      self.assertEqual(res.shape[0], 2)
      self.assertEqual(res.shape[1], 3)

  def test_map_cols(self):
      tdata = np.array([[1,2,3],
                        [4,5,6]])
      res = autil.maprows(lambda col: col + 1, tdata)
      self.assertEqual(res.shape[0], 2)
      self.assertEqual(res.shape[1], 3)