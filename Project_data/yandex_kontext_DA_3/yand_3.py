input_array = input()
days = [int(x) for x in input_array.split()]

def solve(temps):
    min_from_left = [(temps[0], 0)]
    for i in range(1, len(temps)):
        prev_min, prev_idx = min_from_left[-1]
        if prev_min >= temps[i]:
            min_from_left.append((temps[i], i))
        else:
            min_from_left.append((prev_min, prev_idx))
            
#     max_from_right = [(temps[-1], len(temps) - 1)]
 
    max_diff = -float('inf')
    ans_left, ans_right = 0, float('inf')
 
    max_num, max_idx = -float('inf'), 0
    for i in range(len(temps) - 1, -1, -1):
#         next_max, next_idx = max_from_right[-1]
#         if temps[i] >= next_max:
#             max_from_right.append((temps[i], i))
#         else:
#             max_from_right.append((next_max, next_idx))
        
        if max_num <= temps[i]:
            max_num = temps[i]
            max_idx = i
        
        min_num, min_idx = min_from_left[i]
        curr_diff = max_num - min_num
#         print(curr_diff, min_idx, max_idx, max_diff)
        if curr_diff > max_diff:
            max_diff = curr_diff
            ans_left, ans_right = min_idx, max_idx
        elif curr_diff == max_diff and (
            ans_right - ans_left > max_idx - min_idx or 
            (ans_right - ans_left == max_idx - min_idx and ans_right > max_idx)
        ):
            ans_left, ans_right = min_idx, max_idx
    print(max_diff, ans_left, ans_right)        
    return max_diff, ans_left, ans_right           
        
    
solve(days)