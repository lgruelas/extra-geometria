class Segment:
"""
    Representa un segmento de recta, definido por dos puntos.
ATTRS:
    - _upper_endpoint
    - _lower_endpoint
    - _color
"""
    def __init__(self, p1, p2, color=None):
    """
    Asume que necesariamente p1 != p2.
    ARGS:
        - p1 (SegmentPoint2D): endpoint.
        - p2 (SegmentPoint2D): endpoint.
    RAISES:
        - ValueError: si p1 y p2 son iguales.
    """
    if p1 == p2:
        raise ValueError("p1 and p2 can't be equal.")
    elif p1 > p2:
        self._upper_endpoint = p1
        self._lower_endpoint = p2
    else:
        self._lower_endpoint = p1
        self._upper_endpoint = p2
    self._lower_endpoint.set_segment(self)
    self._upper_endpoint.set_segment(self)
    self._color = color

    def get_upper(self):
        return self._upper_endpoint

    def get_lower(self):
        return self._lower_endpoint

    def get_color(self):
        return self._color