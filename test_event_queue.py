import unittest

from event_queue import EventQueue
from point2D import Point2D


class TestEventQueue(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.points = [(3, 3), (4, 2), (5, 4), (6, 2), (0, 5)]
    cls.points = [Point2D(i, j) for i, j in cls.points]

  def setUp(self):
    self.q = EventQueue()
    for i in self.points:
      self.q.add(i)

  def test_event_orders_max_as_root(self):
    self.assertEqual(self.q.peek(), Point2D(0, 5))

  def test_always_pops_biggest_element(self):
    self.assertEqual(self.q.pop(), Point2D(0, 5))
    self.assertEqual(self.q.pop(), Point2D(5, 4))
    self.assertEqual(self.q.pop(), Point2D(3, 3))
    self.assertEqual(self.q.pop(), Point2D(4, 2))
    self.assertEqual(self.q.pop(), Point2D(6, 2))
