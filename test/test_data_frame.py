import unittest
from ..either import core       as either
from ..data import frame        as frame
from ..data import query        as query
import pandas                   as pd
import numpy                    as np

# self.assertEqual('foo'.upper(), 'FOO')
# self.assertTrue('FOO'.isupper())
# self.assertFalse('Foo'.isupper())
# with self.assertRaises(TypeError):
#   s.split(2)

class TestDataFrameMethods(unittest.TestCase):

  def test_dict_list_keep(self):
      df = frame.Frame();
      df.loadCsv('C:\\Users\\ESCO-1\\CodeRepos\\stream\\pycommondev\\pyCommon\\test\\test_data\\test_data_frame1.csv');
      keepsE = df.asDictListKeep(keep=['Corp'])
      self.assertEqual(len(keepsE.val), df._df.shape[0])