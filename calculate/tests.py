import sys
import unittest
import calculate
from datetime import datetime, date
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
try:
    import cStringIO as io
except:
    import io


class BaseTest(unittest.TestCase):

    def setUp(self):
        pass


class CalculateTest(BaseTest):

    def test_adjusted_monthly_value(self):
        self.assertEqual(
            calculate.adjusted_monthly_value(
                10,
                datetime(2009, 4, 1, 0, 10, 10)
            ),
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
        self.assertRaises(
            TypeError,
            calculate.adjusted_monthly_value,
            'a',
            date(2009, 12, 31)
        )
        self.assertRaises(
            TypeError,
            calculate.adjusted_monthly_value,
            10,
            '2010-01-01'
        )
        self.assertRaises(
            TypeError,
            calculate.adjusted_monthly_value,
            10,
            2
        )

    def test_age(self):
        # All the data types
        self.assertEqual(
            calculate.age(datetime(1982, 7, 22), date(2011, 12, 3)),
            29
        )
        self.assertEqual(
            calculate.age(datetime(1982, 7, 22)),
            calculate.age(datetime(1982, 7, 22))
        )
        self.assertEqual(
            calculate.age(date(1982, 7, 22), date(2011, 12, 3)),
            29
        )
        self.assertEqual(
            calculate.age(datetime(1982, 7, 22), datetime(2011, 12, 3)),
            29
        )
        self.assertEqual(
            calculate.age(date(1982, 7, 22), datetime(2011, 12, 3)),
            29
        )
        # Leap Day
        self.assertEqual(
            calculate.age(date(1984, 2, 29), date(2011, 12, 3)),
            27
        )
        # Tomorrow bday
        self.assertEqual(
            calculate.age(date(2010, 12, 4), date(2011, 12, 3)),
            0
        )

    def test_at_percentile(self):
        self.assertEqual(calculate.at_percentile([1, 2, 3, 4], 75), 3.25)
        self.assertEqual(calculate.at_percentile([1, 2, 3, 4], 100), 4)
        self.assertEqual(
            calculate.at_percentile([1, 2, 3, 4], 75, interpolation='lower'),
            3.0
        )
        self.assertEqual(
            calculate.at_percentile([1, 2, 3, 4], 75, interpolation='higher'),
            4.0
        )
        self.assertRaises(ValueError, calculate.at_percentile, ['a', 2, 3], 75)
        self.assertRaises(
            ValueError,
            calculate.at_percentile,
            [1, 2, 3, 4],
            75,
            interpolation='mystery-meat'
        )

    def test_benfords_law(self):
        self.assertEqual(
            calculate.benfords_law(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                verbose=False
            ),
            -0.8638019376987044
        )
        self.assertEqual(
            calculate.benfords_law(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                verbose=True
            ),
            -0.8638019376987044
        )
        self.assertEqual(
            calculate.benfords_law(
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                method="last_digit",
                verbose=False
            ),
            0
        )
        self.assertRaises(
            ValueError,
            calculate.benfords_law,
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            method='magic'
        )
        self.assertRaises(TypeError, calculate.benfords_law, 10.0)

    def test_competition_rank(self):
        dict_list = [
            {'name': 'Joan', 'value': 1},
            {'name': 'Jane', 'value': 2},
            {'name': 'Mary', 'value': 2},
            {'name': 'Josh', 'value': 3},
        ]
        self.assertEqual(
            calculate.competition_rank(
                dict_list, dict_list[0], 'value', 'desc'
            ),
            4
        )
        self.assertEqual(
            calculate.competition_rank(
                dict_list, dict_list[1], 'value', 'desc'
            ),
            2
        )
        self.assertEqual(
            calculate.competition_rank(
                dict_list, dict_list[2], 'value', 'desc'
            ),
            2
        )
        self.assertEqual(
            calculate.competition_rank(dict_list, dict_list[3], 'value'), 1
        )

        def sortFunc(obj):
            return 3

        self.assertEqual(
            calculate.competition_rank(
                dict_list, dict_list[2], sortFunc, 'desc'
            ),
            1
        )

        class DummyObj():
            def __init__(self, **entries):
                self.__dict__.update(entries)

        obj_list = [DummyObj(**d) for d in dict_list]
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

        class DummyDjangoObj(models.Model):
            fake_id = models.IntegerField(primary_key=True)
            name = models.TextField()
            value = models.IntegerField()

            def __unicode__(self):
                return '%s (%s)' % (self.name, self.value)

        obj_list = [
            DummyDjangoObj(fake_id=i + 1, **d)
            for i, d in enumerate(dict_list)
        ]
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

        self.assertRaises(
            ValueError,
            calculate.competition_rank,
            obj_list,
            obj_list[3],
            'value',
            'foobar'
        )

    def test_date_range(self):
        dr = calculate.date_range(
            datetime(2009, 1, 1, 12, 31, 0),
            date(2009, 1, 3)
        )
        self.assertEqual(
            list(dr),
            [date(2009, 1, 1), date(2009, 1, 2), date(2009, 1, 3)]
        )
        self.assertRaises(
            ValueError,
            calculate.date_range,
            date(2011, 1, 1),
            date(2010, 12, 31)
        )
        dr2 = calculate.date_range(
            datetime(2009, 1, 1, 12, 31, 0),
            datetime(2009, 1, 3, 0, 0, 1)
        )
        self.assertEqual(
            list(dr2),
            [date(2009, 1, 1), date(2009, 1, 2), date(2009, 1, 3)]
        )

    def test_decile(self):
        self.assertEqual(calculate.decile([1, 2, 3, 4], 3), 8)
        self.assertEqual(
            calculate.decile([1, 2, 3, 3, 4], 3, kind='strict'),
            5
        )
        self.assertEqual(calculate.decile([1, 2, 3, 3, 4], 3, kind='weak'), 9)
        self.assertEqual(calculate.decile([1, 2, 3, 3, 4], 3, kind='mean'), 7)
        self.assertEqual(calculate.decile([1, 2, 3, 4], 4), 10)

    def test_elfi(self):
        self.assertEqual(
            calculate.elfi([0.2, 0.5, 0.05, 0.25]),
            0.64500000000000002
        )
        self.assertEqual(calculate.elfi([1]), 0)
        self.assertEqual(calculate.elfi([0.5, 0.5]), 0.5)
        self.assertRaises(ValueError, calculate.elfi, ['a', 0.2, 3])

    def test_equal_sized_breakpoints(self):
        self.assertEqual(
            calculate.equal_sized_breakpoints(list(range(1, 101)), 5),
            [1.0, 21.0, 41.0, 61.0, 81.0, 100.0]
        )
        self.assertEqual(
            calculate.equal_sized_breakpoints([1, 2, 3, 4, 5], 2),
            [1.0, 3.5, 5.0]
        )
        self.assertEqual(
            calculate.equal_sized_breakpoints([1, 2, 3, 4, 5, 6], 2),
            [1.0, 4.0, 6.0]
        )
        self.assertRaises(
            TypeError,
            calculate.equal_sized_breakpoints,
            ['foo', 'bar', 'baz'],
            2
        )
        self.assertRaises(
            TypeError,
            calculate.equal_sized_breakpoints,
            list(range(1, 101)),
            'a'
        )

    def test_margin_of_victory(self):
        self.assertEqual(
            calculate.margin_of_victory([3285, 2804, 7170]),
            3885
        )
        self.assertEqual(
            calculate.margin_of_victory([50708, 20639]),
            50708 - 20639
        )

    def test_mean(self):
        self.assertEqual(calculate.mean([1, 2, 3]), 2.0)
        self.assertEqual(calculate.mean([1, 99]), 50.0)
        self.assertEqual(calculate.mean([2, 3, 3]), 2.6666666666666665)
        self.assertRaises(ValueError, calculate.mean, ['a', 0.2, 3])

    def test_mean_center(self):
        dict_list = [
            {
                'name': 'The Los Angeles Times',
                'point': Point(-118.245517015, 34.0525260849, srid=4326)
            },
            {
                'name': 'The Higgins Building',
                'point': Point(-118.245015, 34.051007, srid=4326)
            },
            {
                'name': 'Los Angeles City Hall',
                'point': Point(-118.2430171966, 34.0535749927, srid=4326)
            },
        ]
        self.assertEqual(type(calculate.mean_center(dict_list)), Point)
        self.assertEqual(
            calculate.mean_center(dict_list).wkt,
            'POINT (-118.2445164038666690 34.0523693591999930)'
        )

        class DummyObj():
            def __init__(self, **entries):
                self.__dict__.update(entries)

        obj_list = [DummyObj(**d) for d in dict_list]
        self.assertEqual(type(calculate.mean_center(obj_list)), Point)
        self.assertEqual(
            calculate.mean_center(obj_list).wkt,
            'POINT (-118.2445164038666690 34.0523693591999930)'
        )

        class FakePoint(models.Model):
            fake_id = models.IntegerField(primary_key=True)
            name = models.TextField()
            point = models.PointField(srid=4326)

        obj_list = [
            FakePoint(fake_id=i + 1, **d)
            for i, d in enumerate(dict_list)
        ]
        self.assertEqual(type(calculate.mean_center(obj_list)), Point)
        self.assertEqual(
            calculate.mean_center(obj_list).wkt,
            'POINT (-118.2445164038666690 34.0523693591999930)'
        )

    def test_median(self):
        self.assertEqual(calculate.median([1, 3, 2]), 2.0)
        self.assertEqual(calculate.median([1, 2, 3, 4]), 2.5)
        self.assertRaises(TypeError, calculate.median, [None, 1, 2])
        self.assertRaises(ValueError, calculate.median, ['a', 1, 2])

    def test_mode(self):
        self.assertEqual(calculate.mode([1, 2, 3, 2]), 2.0)
        self.assertEqual(calculate.mode([1, 2, 3]), None)
        self.assertEqual(calculate.mode([2, 2, 2]), 2.0)
        self.assertRaises(TypeError, calculate.mode, [None, 1, 2])
        self.assertRaises(ValueError, calculate.mode, ['a', 1, 2])

    def test_nudge_points(self):

        class FakePoint(models.Model):
            name = models.CharField(max_length=30)
            point = models.PointField()
            objects = models.GeoManager()

        c1 = FakePoint(name='One', point=Point(0, 0))
        c2 = FakePoint(name='Two', point=Point(0, 0))
        c3 = FakePoint(name='Three', point=Point(1, 1))

        l = [c1, c2, c3]
        self.assertTrue(l[0].point == l[1].point)

        l2 = calculate.nudge_points(l)
        self.assertTrue(l2[0].point != l2[1].point)
        self.assertTrue(l[2].point == l2[2].point)

    def test_ordinal_rank(self):
        dict_list = [
            {'name': 'Joan', 'value': 1},
            {'name': 'Jane', 'value': 2},
            {'name': 'Mary', 'value': 3},
            {'name': 'Josh', 'value': 4},
        ]
        self.assertEqual(calculate.ordinal_rank(dict_list, dict_list[0]), 1)
        self.assertEqual(calculate.ordinal_rank(dict_list, dict_list[1]), 2)
        self.assertEqual(calculate.ordinal_rank(dict_list, dict_list[2]), 3)
        self.assertEqual(calculate.ordinal_rank(dict_list, dict_list[3]), 4)
        self.assertEqual(
            calculate.ordinal_rank(dict_list, dict_list[3], 'value', 'desc'),
            1
        )

        class DummyObj():
            def __init__(self, **entries):
                self.__dict__.update(entries)

        obj_list = [DummyObj(**d) for d in dict_list]
        self.assertEqual(
            calculate.ordinal_rank(obj_list, obj_list[0], 'value', 'asc'),
            1
        )
        self.assertEqual(
            calculate.ordinal_rank(obj_list, obj_list[1], 'value', 'asc'),
            2
        )
        self.assertEqual(
            calculate.ordinal_rank(obj_list, obj_list[2], 'value', 'asc'),
            3
        )
        self.assertEqual(
            calculate.ordinal_rank(obj_list, obj_list[3], 'value', 'asc'),
            4
        )

        class DummyDjangoObj(models.Model):
            fake_id = models.IntegerField(primary_key=True)
            name = models.TextField()
            value = models.IntegerField()

            def __unicode__(self):
                return '%s (%s)' % (self.name, self.value)

        obj_list = [
            DummyDjangoObj(fake_id=i + 1, **d)
            for i, d in enumerate(dict_list)
        ]
        self.assertEqual(
            calculate.ordinal_rank(obj_list, obj_list[0], 'value'),
            4
        )
        self.assertEqual(
            calculate.ordinal_rank(obj_list, obj_list[1], 'value'),
            3
        )
        self.assertEqual(
            calculate.ordinal_rank(obj_list, obj_list[2], 'value'),
            2
        )
        self.assertEqual(
            calculate.ordinal_rank(obj_list, obj_list[3], 'value'),
            1
        )

        self.assertRaises(
            ValueError,
            calculate.ordinal_rank,
            obj_list,
            obj_list[3],
            order_by='value',
            direction='foobar',
        )

    def test_pearson(self):
        students = [
            dict(sat=1200, gpa=3.6, drinks_per_day=0.3),
            dict(sat=1400, gpa=3.9, drinks_per_day=0.1),
            dict(sat=1100, gpa=3.0, drinks_per_day=0.5),
            dict(sat=800, gpa=2.5,  drinks_per_day=2.0),
        ]
        self.assertEqual(
            calculate.pearson(
                [i.get("sat") for i in students],
                [i.get("gpa") for i in students],
            ),
            0.9714441330841945
        )
        self.assertEqual(
            calculate.pearson(
                [i.get("sat") for i in students],
                [i.get("drinks_per_day") for i in students],
            ),
            -0.9435297685685435
        )
        self.assertRaises(ValueError, calculate.pearson, [1], [1, 2, 3])

    def test_per_capita(self):
        self.assertEqual(calculate.per_capita(12, 100000), 1.2)
        self.assertEqual(calculate.per_capita(12, 0), None)
        self.assertRaises(
            ZeroDivisionError,
            calculate.per_capita,
            12,
            0,
            fail_silently=False
        )

    def test_percentage(self):
        self.assertEqual(calculate.percentage(12, 60), 20)
        self.assertEqual(calculate.percentage(12, 60, multiply=False), 0.2)
        self.assertEqual(calculate.percentage(12, 0), None)
        self.assertRaises(
            ZeroDivisionError,
            calculate.percentage,
            12,
            0,
            fail_silently=False
        )

    def test_percentage_change(self):
        self.assertEqual(calculate.percentage_change(12, 60), 400)
        self.assertEqual(
            calculate.percentage_change(12, 60, multiply=False),
            4.0
        )
        self.assertEqual(calculate.percentage_change(12, 0), -100)
        self.assertEqual(calculate.percentage_change(0, 12), None)
        self.assertRaises(
            ZeroDivisionError,
            calculate.percentage_change,
            0,
            12,
            fail_silently=False
        )

    def test_percentile(self):
        self.assertEqual(calculate.percentile([1, 2, 3, 4], 3), 75)
        self.assertEqual(
            calculate.percentile([1, 2, 3, 3, 4], 3, kind='strict'),
            40
        )
        self.assertEqual(
            calculate.percentile([1, 2, 3, 3, 4], 3, kind='weak'),
            80
        )
        self.assertEqual(
            calculate.percentile([1, 2, 3, 3, 4], 3, kind='mean'),
            60
        )
        self.assertRaises(ValueError, calculate.percentile, ['a', 2, 3], 3)
        self.assertRaises(
            ValueError,
            calculate.percentile,
            [1, 2, 3, 4],
            3,
            kind='mystery-meat'
        )

    def test_per_sqmi(self):
        self.assertEqual(calculate.per_sqmi(12, 60), 0.2)
        self.assertEqual(calculate.per_sqmi(12, 0), None)
        self.assertRaises(
            ZeroDivisionError,
            calculate.per_sqmi,
            12,
            0,
            fail_silently=False
        )

    def test_ptable(self):
        from calculate import ptable
        ptable.indent(['foo', 'bar'])

    def test_random_point(self):
        ymin, xmin = 34.03743993275203, -118.27177047729492
        ymax, xmax = 34.0525171958097, -118.22404861450195
        random_point = calculate.random_point((xmin, ymin, xmax, ymax))
        self.assertEqual(random_point.x < xmax, True)
        self.assertEqual(random_point.x > xmin, True)
        self.assertEqual(random_point.y < ymax, True)
        self.assertEqual(random_point.y > ymin, True)

    def test_range(self):
        self.assertEqual(calculate.range([1, 2, 3]), 2)
        self.assertRaises(ValueError, calculate.range, ['a', 1, 2])
        self.assertRaises(ValueError, calculate.range, [1])

    def test_split_at_breakpoints(self):
        l = list(range(1, 31))
        bp = calculate.equal_sized_breakpoints(l, 5)
        self.assertEqual(bp, [1.0, 7.0, 13.0, 19.0, 25.0, 30.0])
        self.assertEqual(
            calculate.split_at_breakpoints(l, bp),
            [
                [1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24],
                [25, 26, 27, 28, 29, 30]
            ]
        )
        self.assertRaises(
            Exception,
            calculate.split_at_breakpoints,
            ['foo', 'bar', 'baz'],
            bp,
        )
        self.assertRaises(
            Exception,
            calculate.split_at_breakpoints,
            l,
            ['foo', 'bar', 'baz'],
        )

    def test_standard_deviation(self):
        self.assertEqual(
            calculate.standard_deviation([2, 3, 3, 4]),
            0.70710678118654757
        )
        self.assertEqual(
            calculate.standard_deviation([-2, 3, 3, 40]),
            16.867127793432999
        )
        self.assertRaises(
            ValueError,
            calculate.standard_deviation,
            ['a', 2, 3, 3, 4]
        )

    def test_standard_deviation_distance(self):
        dict_list = [
            {
                'name': 'The Los Angeles Times',
                'point': Point(-118.2455170154, 34.0525260849, srid=4326)
            },
            {
                'name': 'The Higgins Building',
                'point': Point(-118.245015, 34.051007, srid=4326)
            },
            {
                'name': 'Los Angeles City Hall',
                'point': Point(-118.2430171966, 34.0535749927, srid=4326)
            },
        ]

        self.assertEqual(
            calculate.standard_deviation_distance(dict_list),
            0.0003720200725858596
        )

        class DummyObj():
            def __init__(self, **entries):
                self.__dict__.update(entries)

        obj_list = [DummyObj(**d) for d in dict_list]
        self.assertEqual(
            calculate.standard_deviation_distance(obj_list),
            0.0003720200725858596
        )

        class FakePoint(models.Model):
            fake_id = models.IntegerField(primary_key=True)
            name = models.TextField()
            point = models.PointField(srid=4326)

        obj_list = [
            FakePoint(fake_id=i + 1, **d)
            for i, d in enumerate(dict_list)
        ]
        self.assertEqual(
            calculate.standard_deviation_distance(obj_list),
            0.0003720200725858596
        )

    def test_variation_coefficient(self):
        self.assertEqual(
            calculate.variation_coefficient([1, 2, -2, 4, -3]),
            6.442049363362563
        )
        self.assertEqual(
            calculate.variation_coefficient(range(1, 100000)),
            0.5773444956580661
        )
        self.assertRaises(
            ValueError,
            calculate.variation_coefficient,
            ['a', 2, 3, 3, 4]
        )

    def test_summary_stats(self):
        _stdout = sys.stdout
        sys.stdout = io.StringIO()
        calculate.summary_stats(list(range(1, 101)))
        sys.stdout = _stdout


if __name__ == '__main__':
    unittest.main()
