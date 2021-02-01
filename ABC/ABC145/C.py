import itertools
import math

n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
x, y = [list(i) for i in zip(*xy)]

per = list(itertools.permutations(range(n)))

val = 0
for one in per:
    for i in range(1, len(one)):
        val += math.sqrt((x[one[i]] - x[one[i-1]])**2 + (y[one[i]] - y[one[i-1]])**2)

print(val/len(per))