import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def draw_circles_and_count_regions(circles):
    fig, ax = plt.subplots(figsize=(8, 8))

    # رسم دایره‌ها
    for i, (x, y, radius) in enumerate(circles):
        circle = Circle((x, y), radius, color=np.random.rand(3,), alpha=0.5, label=f'دایره {i + 1}')
        ax.add_patch(circle)

    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal', adjustable='box')

    plt.title("رسم دایره‌ها و شمارش نواحی")
    plt.xlabel("محور X")
    plt.ylabel("محور Y")
    plt.grid()
    plt.legend(loc='upper right')
    plt.show()

    # محاسبه تعداد نواحی (یک تخمین ساده)
    num_regions = len(circles) * (len(circles) + 1) // 2  # تخمین نواحی با تداخل
    return num_regions

# ورودی: لیست دایره‌ها (x, y, شعاع)
circles = [
    (0, 0, 3),
    (1, 1, 3),
    (2, -1, 2),
    (-2, 2, 2),
    (-1, -2, 1)
]

# رسم دایره‌ها و شمارش نواحی
region_count = draw_circles_and_count_regions(circles)

# خروجی
print(f"تعداد نواحی تولید شده: {region_count}")