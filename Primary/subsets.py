def generate_subsets(n, k, start=1, current=[]):
    if len(current) == k:
        print(current)
        return

    for i in range(start, n + 1):
        generate_subsets(n, k, i + 1, current + [i])


# مثال: N = 5 و k = 3
N = 5
K = 3
generate_subsets(N, K)


def generate_all_subsets(n, current=[]):
    # چاپ زیرمجموعه فعلی
    print(current)

    # تولید زیرمجموعه‌های بیشتر
    for i in range(1, n + 1):
        if i not in current:  # اطمینان از عدم تکرار
            generate_all_subsets(n, current + [i])


N = 5
generate_all_subsets(N)