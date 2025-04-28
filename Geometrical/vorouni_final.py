import numpy as np
import matplotlib.pyplot as plt


def compute_voronoi(points, grid_size=10):
    # ایجاد یک شبکه n بعدی
    dimensions = points.shape[1]
    grid = np.zeros((grid_size,) * dimensions, dtype=int)

    # محاسبه نواحی Voronoi
    for index in np.ndindex(grid.shape):
        point = np.array(index) * (10 / grid_size)  # مقیاس به محدوده 0 تا 10
        min_dist = float('inf')
        closest_point = -1

        for i, p in enumerate(points):
            dist = np.linalg.norm(p - point)  # محاسبه فاصله اقلیدسی
            if dist < min_dist:
                min_dist = dist
                closest_point = i

        grid[index] = closest_point  # ذخیره نزدیک‌ترین نقطه

    return grid


def plot_voronoi(points, grid):
    plt.imshow(grid[..., 0], cmap='jet', origin='lower')  # فقط برای 2 بعد
    plt.scatter(points[:, 0], points[:, 1], color='black', label='صندوق‌ها', marker='o')

    for i, point in enumerate(points):
        plt.text(point[0], point[1], f' صندوق {i + 1}', fontsize=12, ha='right')

    plt.title("نواحی Voronoi برای ابعاد بالاتر")
    plt.xlabel("محور X")
    plt.ylabel("محور Y")
    plt.colorbar(label='نقطه نزدیک‌ترین')
    plt.grid()
    plt.legend()
    plt.show()


# مثال استفاده
points = np.array([[1, 1], [2, 4], [5, 2], [3, 3], [6, 5]])
grid_size = 20  # اندازه شبکه
voronoi_grid = compute_voronoi(points, grid_size)
plot_voronoi(points, voronoi_grid)