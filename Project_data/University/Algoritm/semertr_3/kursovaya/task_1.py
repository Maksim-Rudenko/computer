import math

def function(R):
    return [4 * math.pi * R ** 2, 4 /3 * math.pi * R ** 3]

r = int(input())
print(function(r))


