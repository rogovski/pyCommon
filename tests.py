import unittest
from test import test_data_array
from test import test_data_frame

def run():
    suite1 = unittest.TestLoader().loadTestsFromTestCase(test_data_array.TestDataArrayMethods)
    unittest.TextTestRunner(verbosity=2).run(suite1)

    suite2 = unittest.TestLoader().loadTestsFromTestCase(test_data_frame.TestDataFrameMethods)
    unittest.TextTestRunner(verbosity=2).run(suite2)