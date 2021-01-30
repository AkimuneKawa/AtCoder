def counter(x):
    if x == 0: return 0
    return counter(x >> 1) + (x & 1)

a = []
x = []
y = []
n = int(input())
for i in range(n):
    a.append(int(input()))
    xy = [list(map(int, input().split())) for _ in range(a[i])]
    tmp_x, tmp_y = [list(i) for i in zip(*xy)]
    x.append(tmp_x)
    y.append(tmp_y)

ans = 0
for bits in range(2 ** n):
    ok = True
    for i in range(n):
        if not (bits & (1 << i)): continue
        if not ok: break
        for j in range(a[i]):
            if ((bits >> (x[i][j] - 1)) & 1) ^ y[i][j]:
                    ok = False
                    break
    if ok: ans = max(ans, counter(bits))

print(ans)