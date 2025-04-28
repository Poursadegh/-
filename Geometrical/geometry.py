import math


def triangle_area(x1, y1, x2, y2, x3, y3):
    return abs(x1(y2 - y3) + x2(y1 - y2) + x3(y2 - y1))


def hamras(x1, y1, x2, y2, x3, y3):
    return (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1)


def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def is_circle_inside_triangle(x1, y1, x2, y2, x3, y3, xc, yc, r):
    def distance_from_line(x1, y1, x2, y2, x, y):
        return abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / math.sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)

    d1 = distance_from_line(x1, y1, x2, y2, xc, yc)
    d2 = distance_from_line(x2, y2, x3, y3, xc, yc)
    d3 = distance_from_line(x3, y3, x1, y1, xc, yc)

    return d1 >= r and d2 >= r and d3 >= r


def line_intersection(m1, b1, m2, b2):
    if m1 == m2:
        return "Lines are parallel"
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y)


def polygon_area(points):  # مساحت چند ضلعی غیز منتظم
    n = len(points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n  # Wrap around to the first point
        area += points[i][0] * points[j][1]
        area -= points[j][0] * points[i][1]
    return abs(area) / 2.0


def is_point_in_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]

        if ((y1 > y) != (y2 > y)) and (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1):
            inside = not inside
    return inside


def polygon_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)


def angle_between_vectors(v1, v2):
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    magnitude_v1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
    magnitude_v2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
    cos_theta = dot_product / (magnitude_v1 * magnitude_v2)
    angle_rad = math.acos(cos_theta)
    angle_deg = math.degrees(angle_rad)
    return angle_deg


def does_circle_intersect_line(xc, yc, r, m, b):
    # تبدیل معادله خط به فرمت عمومی Ax + By + C = 0
    A = m
    B = -1
    C = b

    # محاسبه فاصله از مرکز دایره به خط
    distance = abs(A * xc + B * yc + C) / math.sqrt(A ** 2 + B ** 2)
    return distance <= r


def orientation(p, q, r):
    """Determine the orientation of the triplet (p, q, r).
    Returns:
      0 -> p, q and r are collinear
      1 -> Clockwise
      2 -> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2


def on_segment(p, q, r):
    """Check if point q lies on line segment 'pr'."""
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))


def segments_intersect(p1, q1, p2, q2):
    """Check if line segments 'p1q1' and 'p2q2' intersect."""
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # Special Cases
    # p1, q1 and p2 are collinear and p2 lies on segment p1q1
    if o1 == 0 and on_segment(p1, p2, q1):
        return True
    # p1, q1 and p2 are collinear and q2 lies on segment p1q1
    if o2 == 0 and on_segment(p1, q2, q1):
        return True
    # p2, q2 and p1 are collinear and p1 lies on segment p2q2
    if o3 == 0 and on_segment(p2, p1, q2):
        return True
    # p2, q2 and q1 are collinear and q1 lies on segment p2q2
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


def polygons_intersect(poly1, poly2):
    """Check if two polygons intersect."""
    n1 = len(poly1)
    n2 = len(poly2)

    # Check each edge of the first polygon with each edge of the second polygon
    for i in range(n1):
        p1 = poly1[i]
        q1 = poly1[(i + 1) % n1]  # Next vertex (wrap around)

        for j in range(n2):
            p2 = poly2[j]
            q2 = poly2[(j + 1) % n2]  # Next vertex (wrap around)

            if segments_intersect(p1, q1, p2, q2):
                return True

    return False


class Event:
    def __init__(self, point, line, event_type):
        self.point = point  # نقطه رویداد (x, y)
        self.line = line  # خط مربوط به رویداد
        self.event_type = event_type  # نوع رویداد (نقطه شروع یا پایان)

    def __lt__(self, other):
        return self.point[0] < other.point[0]  # مرتب‌سازی بر اساس x


def orientation(p, q, r):
    """Determine the orientation of the triplet (p, q, r)."""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    return 1 if val > 0 else 2  # clockwise or counterclockwise


def segments_intersect(p1, q1, p2, q2):
    """Check if line segments p1q1 and p2q2 intersect."""
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    return False


def sweep_line_intersection(lines):
    """Check for intersections among a list of lines."""
    events = []

    # جمع‌آوری رویدادها
    for line in lines:
        p1, p2 = line
        events.append(Event(p1, line, 'start'))
        events.append(Event(p2, line, 'end'))
