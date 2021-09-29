class Point2D:
    """
    Para el problema de segmentos de lineas, asumimos que un punto es mayor a
    otro comparando primero su componente Y, en caso de igualdad comparamos por
    componente X.
    """
    def __init__(self, x=None, y=None):
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_coords(self):
        return self._x, self._y

    def set_coords(self, coords):
        self._x, self._y = coords

    def __add__(self, point):
        return Point2D(self._x + point.get_x(), self._y + point.get_y())

    def __sub__(self, point):
        return Point2D(self._x - point.get_x(), self._y - point.get_y())

    def __eq__(self, point):
        return self._x == point.get_x() and self._y == point.get_y()

    def __repr__(self):
        return f"({self._x}, {self._y})"

    def __lt__(self, point):
        if self._y == point.get_y():
            return self._x > point.get_x()
        return self._y < point.get_y()

    def __gt__(self, point):
        if self._y == point.get_y():
            return self._x < point.get_x()
        return self._y > point.get_y()

    def __le__(self, point):
        if self._y == point.get_y():
            return self._x >= point.get_x()
        return self._y < point.get_y()

    def __ge__(self, point):
        if self._y == point.get_y():
            return self._x <= point.get_x()
        return self._y > point.get_y()


class SegmentPoint2D(Point2D):
    """
        Stores the segment so it can return to it.
    """
    def __init__(self, x=None, y=None):
        super().__init__(x, y)
        self._segment = None

    def set_segment(self, segment):
        self._segment = segment

    def get_segment(self):
        return self._segment

    def is_upper(self):
        return self._segment.upper == self

    def is_intersection(self):
        return self._segment is None
