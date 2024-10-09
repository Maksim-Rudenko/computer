
import itertools
numbers = [1, 2, 3]
target = 10
result = [seq for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i)]
print(sum(result[0]))