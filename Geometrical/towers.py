import numpy as np
import matplotlib.pyplot as plt

def skyline(buildings):
    events = []
    for x_left, x_right, height in buildings:
        events.append((x_left, -height))  # شروع مستطیل
        events.append((x_right, height))   # پایان مستطیل

    events.sort()

    heights = {0: 1}  # ارتفاع 0 را اضافه می‌کنیم
    prev_max_height = 0
    result = []

    for x, h in events:
        if h < 0:  # اگر شروع یک مستطیل است
            heights[-h] = heights.get(-h, 0) + 1
        else:  # اگر پایان یک مستطیل است
            heights[h] -= 1
            if heights[h] == 0:
                del heights[h]

        # محاسبه حداکثر ارتفاع فعلی
        current_max_height = max(heights)

        # اگر حداکثر ارتفاع تغییر کرده است، آن را به نتایج اضافه می‌کنیم
        if current_max_height != prev_max_height:
            result.append((x, current_max_height))
            prev_max_height = current_max_height

    return result

def plot_skyline(skyline):
    x_coords, heights = zip(*skyline)

    # رسم مرز مستطیل‌ها
    for i in range(len(x_coords) - 1):
        plt.fill_between([x_coords[i], x_coords[i + 1]], 0, heights[i], color='skyblue', alpha=0.5)

    plt.plot(x_coords, heights, color='blue', linewidth=2)

    plt.title("مرز قابل مشاهده آسمان‌خراش‌ها")
    plt.xlabel("محور X")
    plt.ylabel("ارتفاع")
    plt.grid()
    plt.show()

# تولید 1000 آپارتمان با مختصات تصادفی
num_apartments = 1000
np.random.seed(0)  # برای نتایج قابل تکرار
buildings = []
for _ in range(num_apartments):
    x_left = np.random.randint(0, 100)  # مختصات چپ بین 0 تا 100
    width = np.random.randint(1, 10)     # عرض آپارتمان
    x_right = x_left + width
    height = np.random.randint(1, 20)    # ارتفاع بین 1 تا 20
    buildings.append((x_left, x_right, height))

# محاسبه مرز قابل مشاهده
skyline = skyline(buildings)

# رسم مرز
plot_skyline(skyline)