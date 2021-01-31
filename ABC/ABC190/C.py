n, m = map(int, input().split())
ab = [map(int, input().split()) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]
k = int(input())
cd = [map(int, input().split()) for _ in range(k)]
c, d = [list(i) for i in zip(*cd)]

ans = 0
for bits in range(2 ** k):
    oita = set()
    for i in range(k):
        if (bits >> i) & 1:
            oita.add(c[i])
        else:
            oita.add(d[i])
    count = 0
    for i in range(m):
        if a[i] in oita and b[i] in oita:
            count += 1
    ans = max(ans, count)

print(ans)