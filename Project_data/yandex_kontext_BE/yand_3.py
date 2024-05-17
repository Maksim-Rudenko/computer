def count_non_intersecting_segments(a, b):
    n = len(a)
    if n == 0:
        return 0
    a, b = sorted(a), sorted(b)
    start, end, count = -1, -1, 0
    for i in range(n):
        if a[i] >= start and b[i] >= end:
            count += 1
            start, end = a[i], b[i]
    return count

a = [1, 2, 3, 4, 5]
b = [4, 5, 1, 5, 6]

print(count_non_intersecting_segments(a,b))