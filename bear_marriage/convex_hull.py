from .data import ColoredPoint


def is_clockwise(p: ColoredPoint, q: ColoredPoint, r: ColoredPoint) -> bool | None:
    """Find the orientation of the ordered triplet (p, q, r)."""
    # cross product of vectors `pq` and `qr`
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return None  # Collinear
    elif val > 0:
        return True  # Clockwise
    else:
        return False  # Counterclockwise


def jarvis_algorithm(points: list[ColoredPoint]) -> list[int]:
    """Find the convex hull using the Jarvis algorithm."""
    n = len(points)
    if n < 3:
        return list(range(n))

    # Find the leftmost point
    hull = []
    i_start = min(range(n), key=lambda i: points[i])
    i_point = i_start

    while True:
        hull.append(i_point)
        i_endpoint = 0
        for j in range(1, n):
            if (points[i_endpoint] == points[i_point]) or (
                is_clockwise(points[i_point], points[i_endpoint], points[j])
            ):
                i_endpoint = j

        i_point = i_endpoint
        if i_point == i_start:
            break

    return hull
