import numpy as np
import matplotlib.pyplot as plt

def generate_segments(num_segments):
    segments = []
    for _ in range(num_segments):
        # تولید پاره‌خط‌های افقی
        if np.random.rand() > 0.5:  # 50% احتمال برای افقی یا عمودی
            y = np.random.randint(0, 10)
            x1 = np.random.randint(0, 10)
            x2 = np.random.randint(x1, 10)  # اطمینان از اینکه x2 بزرگتر از x1 باشد
            segments.append((x1, y, x2, y))
        else:  # تولید پاره‌خط‌های عمودی
            x = np.random.randint(0, 10)
            y1 = np.random.randint(0, 10)
            y2 = np.random.randint(y1, 10)  # اطمینان از اینکه y2 بزرگتر از y1 باشد
            segments.append((x, y1, x, y2))
    return segments

def plot_lines(segments, point_A, point_B):
    # رسم پاره‌خط‌ها
    for (x1, y1, x2, y2) in segments:
        plt.plot([x1, x2], [y1, y2], color='black')

    # رسم نقاط A و B
    plt.plot(point_A[0], point_A[1], 'ro', label='نقطه A')
    plt.plot(point_B[0], point_B[1], 'bo', label='نقطه B')

    # محاسبه و رسم مسیر
    path_x = [point_A[0], point_B[0]]
    path_y = [point_A[1], point_A[1], point_B[1]]

    # رسم مسیر با ضخامت بیشتر
    plt.plot([path_x[0], path_x[0]], [point_A[1], point_B[1]], color='red', linestyle='--', linewidth=2.5)
    plt.plot([point_A[0], point_B[0]], [path_y[1], path_y[1]], color='red', linestyle='--', linewidth=2.5)

    # جلوگیری از عبور از روی بخش‌های تکراری
    visited = set()  # مجموعه‌ای برای نگهداری نقاط عبور شده
    path_points = []

    # حرکت به سمت راست یا چپ
    for x in range(min(point_A[0], point_B[0]), max(point_A[0], point_B[0]) + 1):
        if (x, point_A[1]) not in visited:
            path_points.append((x, point_A[1]))
            visited.add((x, point_A[1]))

    # حرکت به سمت بالا یا پایین
    for y in range(min(point_A[1], point_B[1]), max(point_A[1], point_B[1]) + 1):
        if (point_B[0], y) not in visited:
            path_points.append((point_B[0], y))
            visited.add((point_B[0], y))

    # رسم مسیر نهایی
    for i in range(len(path_points) - 1):
        plt.plot([path_points[i][0], path_points[i + 1][0]],
                 [path_points[i][1], path_points[i + 1][1]],
                 color='red', linestyle='--', linewidth=2.5)

    plt.title("مسیر بین نقاط A و B (بدون تکرار)")
    plt.xlabel("محور X")
    plt.ylabel("محور Y")
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid()
    plt.legend()
    plt.show()

# تولید 20 پاره‌خط
num_segments = 20
segments = generate_segments(num_segments)

# تعریف نقاط A و B
point_A = (2, 2)  # مختصات نقطه A
point_B = (6, 4)  # مختصات نقطه B

# رسم پاره‌خط‌ها و مسیر
plot_lines(segments, point_A, point_B)