import numpy as np
import matplotlib.pyplot as plt

# مختصات صندوق‌ها (ورودی)
points = np.array([[1, 1], [2, 4], [5, 2], [3, 3], [6, 5]])


def compute_voronoi(points, grid_size=10):
    # ایجاد یک شبکه از نقاط
    grid = np.zeros((grid_size, grid_size), dtype=int)

    for x in range(grid_size):
        for y in range(grid_size):
            min_dist = float('inf')
            closest_point = -1

            for i, point in enumerate(points):
                # محاسبه فاصله اقلیدسی
                dist = np.sqrt((point[0] - x) ** 2 + (point[1] - y) ** 2)
                if dist < min_dist:
                    min_dist = dist
                    closest_point = i

            grid[x, y] = closest_point  # ذخیره نزدیک‌ترین نقطه

    return grid


def plot_voronoi(points, grid):
    plt.imshow(grid, cmap='jet', origin='lower')

    # رسم نقاط صندوق‌ها
    plt.scatter(points[:, 0], points[:, 1], color='black', label='صندوق‌ها', marker='o')

    # اضافه کردن برچسب‌ها
    for i, point in enumerate(points):
        plt.text(point[0], point[1], f' صندوق {i + 1}', fontsize=12, ha='right')

    plt.title("نواحی Voronoi بدون استفاده از کتابخانه")
    plt.xlabel("محور X")
    plt.ylabel("محور Y")
    plt.colorbar(label='نقطه نزدیک‌ترین')
    plt.grid()
    plt.legend()
    plt.show()


# محاسبه نواحی Voronoi
grid_size = 10
voronoi_grid = compute_voronoi(points, grid_size)

# رسم نواحی Voronoi
plot_voronoi(points, voronoi_grid)