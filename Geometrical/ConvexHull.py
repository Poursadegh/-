import matplotlib.pyplot as plt
import numpy as np

#
# def orientation(p, q, r):
#     """Determine the orientation of the triplet (p, q, r).
#     Returns:
#       0 -> p, q and r are collinear
#       1 -> Clockwise
#       2 -> Counterclockwise
#     """
#     val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
#     if val == 0:
#         return 0
#     return 1 if val > 0 else 2


# def distance(p1, p2):
#     """Calculate the distance between two points."""
#     return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
#
#
# def convex_hull(points):
#     """Computes the convex hull of a set of 2D points."""
#     # Step 1: Find the point with the lowest y-coordinate
#     points = sorted(points)
#     lowest = points[0]
#
#     # Step 2: Sort the points based on polar angle with the lowest point
#     sorted_points = sorted(points[1:],
#                            key=lambda p: (np.arctan2(p[1] - lowest[1], p[0] - lowest[0]), distance(lowest, p)))
#
#     # Step 3: Create the convex hull
#     hull = [lowest]
#     for point in sorted_points:
#         while len(hull) > 1 and orientation(hull[-2], hull[-1], point) != 2:
#             hull.pop()  # Remove last point in hull
#         hull.append(point)
#
#     return hull
#
#
# # Example usage
# points = [(0, 0), (1, 2), (2, 1), (3, 3), (5, 1), (3, 0), (2, 2), (4, 0)]
# hull = convex_hull(points)
#
# # Display points and convex hull
# x_hull, y_hull = zip(*hull)
# plt.plot(x_hull + (hull[0][0],), y_hull + (hull[0][1],), 'r-')  # Draw hull
# plt.scatter(*zip(*points), color='blue')  # Draw points
# plt.title("Convex Hull")
# plt.show()
#
# import matplotlib.pyplot as plt
#
#
# def orientation(p, q, r):
#     """Determine the orientation of the triplet (p, q, r)."""
#     val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
#     if val == 0:
#         return 0  # Collinear
#     return 1 if val > 0 else 2  # Clockwise or counterclockwise
import matplotlib.pyplot as plt


def orientation(p, q, r):
    """Determine the orientation of the triplet (p, q, r)."""
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise


def jarvis_hull(points):
    """Computes the convex hull of a set of 2D points using the Jarvis March algorithm."""
    n = len(points)
    if n < 3:
        return points  # Convex hull is not possible with fewer than 3 points

    # Step 1: Find the leftmost point
    leftmost = min(points, key=lambda p: (p[0], p[1]))

    hull = []
    p = leftmost

    while True:
        hull.append(p)  # Add current point to the hull
        q = points[0]  # Assume the next point is the first point

        # Step 2: Find the most counter-clockwise point
        for r in points:
            if r == p:
                continue  # Skip the current point
            if orientation(p, q, r) == 2:  # If r is more counterclockwise than q
                q = r

        p = q  # Move to the next point

        # Stop if we have come back to the starting point
        if p == leftmost:
            break

    return hull


# Example usage
points = [(0, 0), (1, 2), (2, 1), (3, 3), (5, 1), (3, 0), (2, 2), (4, 0)]
hull = jarvis_hull(points)

# Display points and convex hull
x_hull, y_hull = zip(*hull)
plt.plot(x_hull + (hull[0][0],), y_hull + (hull[0][1],), 'r-')  # Draw hull
plt.scatter(*zip(*points), color='blue')  # Draw points
plt.title("Convex Hull (Jarvis March)")
plt.show()
