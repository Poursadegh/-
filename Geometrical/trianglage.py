import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

def generate_points(n):
    # تولید n نقطه تصادفی
    return np.random.rand(n, 2) * 10

def compute_delaunay(points):
    # محاسبه مثلث‌بندی Delaunay
    return Delaunay(points)

def plot_triangulation(points, tri):
    plt.triplot(points[:, 0], points[:, 1], tri.simplices)
    plt.plot(points[:, 0], points[:, 1], 'o')
    for i, point in enumerate(points):
        plt.text(point[0], point[1], f' {i+1}', fontsize=12, ha='right')

    plt.title("مثلث‌بندی Delaunay")
    plt.xlabel("محور X")
    plt.ylabel("محور Y")
    plt.grid()
    plt.show()

def compute_edge_lengths(tri, points):
    lengths = []
    for simplex in tri.simplices:
        for i in range(len(simplex)):
            p1 = points[simplex[i]]
            p2 = points[simplex[(i + 1) % len(simplex)]]
            length = np.linalg.norm(p1 - p2)
            lengths.append(length)
    return lengths

# تعداد نقاط
n = 10
points = generate_points(n)

# محاسبه مثلث‌بندی
tri = compute_delaunay(points)

# رسم مثلث‌بندی
plot_triangulation(points, tri)

# محاسبه طول‌های اضلاع
edge_lengths = compute_edge_lengths(tri, points)
total_length = sum(edge_lengths)

print(f"جمع طول‌های اضلاع: {total_length:.2f}")