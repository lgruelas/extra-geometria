import unittest

from point2D import Point2D


class TestPoint2D(unittest.TestCase):
  def setUp(self):
    self.p1 = Point2D(3, 3)
    self.p2 = Point2D(4, 2)

  def test_less_than(self):
    self.assertTrue(self.p2 < self.p1)
    self.assertFalse(self.p1 < self.p2)
    self.assertFalse(self.p2 < self.p2)
    self.p1.set_coords((6, 2))
    self.assertTrue(self.p1 < self.p2)

  def test_greater_than(self):
    self.assertFalse(self.p2 > self.p1)
    self.assertTrue(self.p1 > self.p2)
    self.assertFalse(self.p2 > self.p2)
    self.p1.set_coords((6, 2))
    self.assertTrue(self.p2 > self.p1)

  def test_less_or_equal_than(self):
    self.assertTrue(self.p2 <= self.p1)
    self.assertFalse(self.p1 <= self.p2)
    self.assertTrue(self.p2 <= self.p2)
    self.p1.set_coords((6, 2))
    self.assertTrue(self.p1 <= self.p2)

  def test_greater_or_equal_than(self):
    self.assertFalse(self.p2 >= self.p1)
    self.assertTrue(self.p1 >= self.p2)
    self.assertTrue(self.p2 >= self.p2)
    self.p1.set_coords((6, 2))
    self.assertTrue(self.p2 >= self.p1)
