import unittest

from third import get_convex_hull, is_point_inside_triangle
from point2D import Point2D


class TestPointInTriangle(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls._dataset = []
    with open("test_convex_data.txt", "r") as f:
      for i in range(int(f.readline().strip())):
        cls._dataset.append(Point2D(*map(int, f.readline().strip().split())))

  def test_point_in_triangle(self):
    self.assertTrue(is_point_inside_triangle(self._dataset, Point2D(4, 4)))

  def test_point_not_in_triangle(self):
    self.assertFalse(is_point_inside_triangle(self._dataset, Point2D(6, 4)))

  def test_point_in_triangle_when_same_line(self):
    """
      Tests the point is considered inside triangle when lies in the perimeter.
    """
    self.assertTrue(is_point_inside_triangle(self._dataset, Point2D(4, 5)))


class TestConvexHull(unittest.TestCase):
  def setUp(self):
    self._dataset = []
    with open("test_convex_data.txt", "r") as f:
      for i in range(int(f.readline().strip())):
        self._dataset.append(Point2D(*map(int, f.readline().strip().split())))

  def test_convex_hull(self):
    expected_convex_hull = [(1, 1), (2, 5), (5, 5), (5, 3)]
    expected_convex_hull = [Point2D(i, j) for i, j in expected_convex_hull]
    self.assertEqual(get_convex_hull(self._dataset), expected_convex_hull)
