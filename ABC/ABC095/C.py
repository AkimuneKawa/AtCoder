a, b, c, x, y = map(int, input().split())

n_a = 0
n_b = 0
n_c = 0

if a+b > 2*c:
    n_c += min(x, y) * 2
else:
    n_a += min(x, y)
    n_b += min(x, y)

if x > y:
    if a > 2*c:
        n_c += (x-y) * 2
    else:
        n_a += x-y
else:
    if b > 2*c:
        n_c += (y-x) * 2
    else:
        n_b += y-x

print(a*n_a + b*n_b + c*n_c)
        