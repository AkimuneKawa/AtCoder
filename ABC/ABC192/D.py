def f(x, n): # n進法のx
    x = x[::-1]
    return sum([int(x[i]) * n ** i for i in range(len(x))])

x = list(map(int, list(input())))
m = int(input())

if len(x) == 1:
    if x[0] <= m:
        print(1)
    else:
        print(0)
    exit()

left = max(x)
right = m + 1

while abs(left - right) > 1:
    mid = (left + right) // 2
    if f(x, mid) <= m:
        left = mid
    else:
        right = mid

print(left - max(x))