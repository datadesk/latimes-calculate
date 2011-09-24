from __future__ import with_statement
import unittest
import calculate
from datetime import datetime, date


class BaseTest(unittest.TestCase):
    
    def setUp(self):
        pass


class CalculateTest(BaseTest):
    
    def test_adjusted_monthly_value(self):
        self.assertEqual(
            calculate.adjusted_monthly_value(10, datetime(2009, 4, 1, 0, 10, 10)),
            10.0
        )
        self.assertEqual(
            calculate.adjusted_monthly_value(10, datetime(2009, 2, 17)),
            10.714285714285714
        )
        self.assertEqual(
            calculate.adjusted_monthly_value(10, date(2009, 12, 31)),
            9.67741935483871
        )
        with self.assertRaises(TypeError):
            calculate.adjusted_monthly_value('a', date(2009, 12, 31))
        with self.assertRaises(TypeError):
            calculate.adjusted_monthly_value(10, '2010-01-01')
        with self.assertRaises(TypeError):
            calculate.adjusted_monthly_value(10, 2)
    
    def test_benfords_law(self):
        self.assertEqual(
            calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], verbose=False),
            -0.863801937698704
        )
        self.assertEqual(
            calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], method="last_digit", verbose=False),
            0
        )
        with self.assertRaises(ValueError):
            calculate.benfords_law([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], method='magic')
        with self.assertRaises(TypeError):
            calculate.benfords_law(10.0)
    
    def test_competition_rank(self):
        dict_list = [
            {'name': 'Joan', 'value': 1},
            {'name': 'Jane', 'value': 2},
            {'name': 'Mary', 'value': 2},
            {'name': 'Josh', 'value': 3},
        ]
        self.assertEqual(
            calculate.competition_rank(dict_list, dict_list[0], 'value', 'desc'),
            4
        )
        class Dummy:
            def __init__(self, **entries): 
                self.__dict__.update(entries)
        obj_list = [Dummy(**d) for d in dict_list]
        self.assertEqual(
            calculate.competition_rank(obj_list, obj_list[0], 'value', 'asc'),
            1
        )
        self.assertEqual(
            calculate.competition_rank(obj_list, obj_list[1], 'value', 'asc'),
            2
        )
        self.assertEqual(
            calculate.competition_rank(obj_list, obj_list[2], 'value', 'asc'),
            2
        )
        self.assertEqual(
            calculate.competition_rank(obj_list, obj_list[3], 'value', 'asc'),
            4
        )

if __name__ == '__main__':
    unittest.main()
