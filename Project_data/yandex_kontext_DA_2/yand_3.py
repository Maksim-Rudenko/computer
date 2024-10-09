def max_difference(arr, K, N):
    #N = len(arr)
    min_values = [0] * N
    max_values = [0] * N

    min_values[0] = arr[0]
    for i in range(1, N):
        min_values[i] = min(min_values[i - 1], arr[i])

    max_values[N - 1] = arr[N - 1]
    for i in range(N - 2, -1, -1):
        max_values[i] = max(max_values[i + 1], arr[i])

    max_diff = float('-inf')
    for i in range(K, N):
        max_diff = max(max_diff, max_values[i] - min_values[i - K])

    return max_diff

input_str = input()
n, k = input_str.split()
n = int(n)
k = int(k)

input_array = input()
arr = [int(x) for x in input_array.split()]

print(max_difference(arr, k, n))

