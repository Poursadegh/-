import matplotlib.pyplot as plt

def count_right_turns_and_plot(coordinates):
    right_turns = 0

    # رسم مسیر حرکت
    plt.figure(figsize=(8, 6))

    # رسم پیکان‌ها برای جهت حرکت
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        plt.arrow(x1, y1, x2 - x1, y2 - y1,
                  head_width=0.2, head_length=0.3,
                  fc='blue', ec='blue')

        # محاسبه علامت حاصل‌ضرب متقاطع برای گردش به راست
        if i > 0:  # از سومین نقطه به بعد
            x0, y0 = coordinates[i - 1]
            cross_product = (x2 - x1) * (y0 - y1) - (y2 - y1) * (x0 - x1)
            # اگر حاصل‌ضرب منفی باشد، گردش به راست است
            if cross_product < 0:
                right_turns += 1
                plt.plot([x1, x1], [y1, y1 + 0.5], color='red', linestyle='--')  # نمایش گردش به راست

    # رسم نقاط A و B
    plt.plot(coordinates[0][0], coordinates[0][1], 'ro', label='نقطه A')
    plt.plot(coordinates[-1][0], coordinates[-1][1], 'bo', label='نقطه B')

    plt.title("مسیر حرکت ماشین")
    plt.xlabel("محور X")
    plt.ylabel("محور Y")
    plt.grid()
    plt.legend()
    plt.axis('equal')
    plt.show()

    return right_turns

# ورودی: دنباله‌ای از مختصات
coordinates = [(0, 0), (1, 2), (2, 2), (3, 1), (2, 0), (1, 1)]

# محاسبه تعداد گردش‌های به راست و رسم مسیر
right_turn_count = count_right_turns_and_plot(coordinates)

# خروجی
print(f"تعداد گردش‌های به راست: {right_turn_count}")