input_str = input()
num_days = int(input_str)

input_array = input()
arr = [str(x) for x in input_array.split()]

def solve(times):
    def to_minutes(t):
        hours, minutes = t.split(':')
        return int(hours) * 60 + int(minutes)
    
    int_times = sorted(map(to_minutes, times))
    min_diff = 24 * 60 + int_times[0] - int_times[-1]
    print(min_diff)
    prev = int_times[0]
    for i in range(1, len(int_times)):
        curr = int_times[i]
        min_diff = min(min_diff, curr - prev)
        prev = curr
    return min_diff

print(solve(arr))