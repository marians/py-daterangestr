# encoding: utf-8

import unittest
from daterangestr import to_dates
from datetime import datetime


class MyTests(unittest.TestCase):

    def test01(self):
        a, b = to_dates('2012')
        self.assertEqual(a, datetime(2012, 1, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2012, 12, 31, 23, 59, 59))

    def test02(self):
        a, b = to_dates('201201')
        self.assertEqual(a, datetime(2012, 1, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2012, 1, 31, 23, 59, 59))

    def test03(self):
        a, b = to_dates('20121001')
        self.assertEqual(a, datetime(2012, 10, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2012, 10, 1, 23, 59, 59))

    def test04(self):
        a, b = to_dates('2011-2011')
        self.assertEqual(a, datetime(2011, 1, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2011, 12, 31, 23, 59, 59))

    def test05(self):
        a, b = to_dates('2011-2012')
        self.assertEqual(a, datetime(2011, 1, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2012, 12, 31, 23, 59, 59))

    def test06(self):
        a, b = to_dates('201104-2012')
        self.assertEqual(a, datetime(2011, 4, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2012, 12, 31, 23, 59, 59))

    def test07(self):
        a, b = to_dates('201104-201203')
        self.assertEqual(a, datetime(2011, 4, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2012, 3, 31, 23, 59, 59))

    def test08(self):
        a, b = to_dates('20110408-2011')
        self.assertEqual(a, datetime(2011, 4, 8, 0, 0, 0))
        self.assertEqual(b, datetime(2011, 12, 31, 23, 59, 59))

    def test09(self):
        a, b = to_dates('2011-')
        self.assertEqual(a, datetime(2011, 1, 1, 0, 0, 0))
        self.assertEqual(b, datetime(9999, 12, 31, 23, 59, 59))

    def test10(self):
        a, b = to_dates('201104-')
        self.assertEqual(a, datetime(2011, 4, 1, 0, 0, 0))
        self.assertEqual(b, datetime(9999, 12, 31, 23, 59, 59))

    def test11(self):
        a, b = to_dates('20110408-')
        self.assertEqual(a, datetime(2011, 4, 8, 0, 0, 0))
        self.assertEqual(b, datetime(9999, 12, 31, 23, 59, 59))

    def test12(self):
        a, b = to_dates('-2011')
        self.assertEqual(a, datetime(1, 1, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2011, 12, 31, 23, 59, 59))

    def test13(self):
        a, b = to_dates('-201104')
        self.assertEqual(a, datetime(1, 1, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2011, 4, 30, 23, 59, 59))

    def test14(self):
        a, b = to_dates('-20110408')
        self.assertEqual(a, datetime(1, 1, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2011, 4, 8, 23, 59, 59))

    def test15(self):
        """Non leap year"""
        a, b = to_dates('200902')
        self.assertEqual(a, datetime(2009, 2, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2009, 2, 28, 23, 59, 59))

    def test16(self):
        """Non leap year"""
        a, b = to_dates('201002')
        self.assertEqual(a, datetime(2010, 2, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2010, 2, 28, 23, 59, 59))

    def test17(self):
        """Non leap year"""
        a, b = to_dates('201102')
        self.assertEqual(a, datetime(2011, 2, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2011, 2, 28, 23, 59, 59))

    def test18(self):
        """Leap year"""
        a, b = to_dates('201202')
        self.assertEqual(a, datetime(2012, 2, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2012, 2, 29, 23, 59, 59))

    def test19(self):
        """Non leap year"""
        a, b = to_dates('201302')
        self.assertEqual(a, datetime(2013, 2, 1, 0, 0, 0))
        self.assertEqual(b, datetime(2013, 2, 28, 23, 59, 59))


if __name__ == '__main__':
    unittest.main()
