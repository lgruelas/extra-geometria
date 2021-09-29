def sort_by_x(element, reverse=False):
    '''
        In situ sort (more or less) by X attr.
        INPUT:
            - element (list) list of Point2D class to be sorted.
        RETURN:
            - None
        RAISES:
            - TypeError if element is not a list.
    '''
    if not isinstance(element, list):
        raise TypeError('Must be a list.')
    return element.sort(key=lambda x: (x.get_x(), x.get_y()), reverse=reverse)


def sort_by_y(element, reverse=False):
    '''
        In situ sort (more or less) by Y attr.
        INPUT:
            - element (list) list of Point2D class to be sorted.
        RETURN:
            - None
        RAISES:
            - TypeError if element is not a list.
    '''
    if not isinstance(element, list):
        raise TypeError('Must be a list.')
    return element.sort(key=lambda x: (x.get_y(), x.get_x()), reverse=reverse)


def move_to_origin(point, A, B):
    """
        Moves the passed points to origin respect to point.
    """
    return A - point, B - point


def is_turn_right(points, point2):
    '''
        INPUT:
            - points, list of two point2D, just the last two elements are used.
            - point2, the point we want to check the turn needed to reach it.
        RETURN: boolean, true if it represents a turn right.
    '''
    C, P = move_to_origin(points[-2], points[-1], point2)
    return C.get_x() * P.get_y() < C.get_y() * P.get_x()


def is_turn_left(points, point2):
    '''
        INPUT:
            - points, list of two point2D, just the last two elements are used.
            - point2, the point we want to check the turn needed to reach it.
        RETURN: boolean, true if it represents a turn left.
    '''
    C, P = move_to_origin(points[-2], points[-1], point2)
    return C.get_x() * P.get_y() > C.get_y() * P.get_x()


def get_convex_hull(elements):
    '''
        INPUT: list of Point2D instances
        RETURN: list whit the points in the ConvexHUll of the set
    '''
    sort_by_x(elements)
    upper = elements[:2]
    lower = elements[:2]
    for i in range(2, len(elements)):
        while len(upper) > 1 and not is_turn_right(upper[-2:], elements[i]):
            upper.pop()
        while len(lower) > 1 and not is_turn_left(lower[-2:], elements[i]):
            lower.pop()
        upper.append(elements[i])
        lower.append(elements[i])
    sort_by_x(lower, reverse=True)
    return upper + lower[1:-1]


def is_point_inside_triangle(x, p):
    """ Given a set of points X, and a point P, checks if there is a triangle
    made with points on X that contain P.

    In order to now if a point is inside a triangle, we can check if it's
    inside the convex hull of the set of points X.

    To check if it's inside the convex hull, we can add it to the group of
    points and check if the algorithm append it.
    ARGS:
        - x (set): set of Point2D.
        - p (Point2D): point to look.

    RETURN:
        - bool, True if there is a triange formed with points on x that
            contain P.
    """
    convex_hull = get_convex_hull(x + [p])
    if p in convex_hull:
        return False
    return True
