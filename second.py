from event_queue import EventQueue
from point2D import SegmentPoint2D
from segment import Segment


def parse_to_segment_list(raw_segment_list, color):
    """
    me imagino que raw_segment_list se verá como:
        [[(x, y), (x, y)], [(x, y), (x, y)], [(x, y), (x, y)]]
    """
    to_return = []
    for i in raw_segment_list:
        point1 = SegmentPoint2D(i[0][0], i[0][1])
        point2 = SegmentPoint2D(i[1][0], i[1][1])
        segment = Segment(point1, point2, color)
        to_return.append(segment)
    return to_return



def interseccion_conjuntos(azul_list, rojo_list):
    """
    Regresa el número de intersecciones entre dos conjuntos de segmentos.
    ARGS:
        - azul_list (list of list of tuples)
        - rojo_list (list of list of tuples)
    """

    # Convertimos a lista de segmentos
    blue = parse_to_segment_list(azul_list, "blue")
    red = parse_to_segment_list(rojo_list, "red")

    # Inicializamos el event queue q
    q = EventQueue()

    # La poblamos con los endpoints de los dos conjuntos de segmentos
    for segment in blue:
        q.add(segment.get_upper())
        q.add(segment.get_lower())

    for segment in red:
        q.add(segment.get_upper())
        q.add(segment.get_lower())

    # Inicializamos las structures
    red_structure = []
    blue_structure = []

    while not q.is_empty():
        event_point = q.pop()
        if event_point.is_upper():
            handle_upper_event_endpoint()
        elif event_point.is_intersection():
            handle_intersection_event_endpoint()
        else:
            handle_lower_event_endpoint()
