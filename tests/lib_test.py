# -*- coding: UTF-8 -*-

# Import from standard library
import os
import projectvivan
import unittest
import pandas as pd

# Import from our lib
from projectvivan.lib import clean_data, try_me

class TestUtils(unittest.TestCase):

    # @unittest.skip('')
    def test_clean_data(self):
        datapath = os.path.dirname(os.path.abspath(projectvivan.__file__)) + '/data'
        df = pd.read_csv('{}/data.csv.gz'.format(datapath))
        self.assertListEqual(list(df.columns)[:6],
                             ['id', 'civility', 'birthdate', 'city',
                              'postal_code', 'vote_1'])
        self.assertEqual(df.shape, (999, 142))
        out = clean_data(df)
        self.assertEqual(out.shape, (985, 119))

    def test_try_me(self):
        self.assertEqual(try_me(), "hello!")

if __name__ == '__main__':
    unittest.main()
