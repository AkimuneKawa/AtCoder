import itertools

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
a, b = [list(i) for i in zip(*ab)]

perm = itertools.permutations(range(2, n+1))

ans = 0
for one in perm:
    one = list(one)
    one.insert(0, 1)
    ok = True
    for i in range(len(one)-1):
        ok = ok and any([(one[i] == a[j] and one[i+1] == b[j]) or (one[i] == b[j] and one[i+1] == a[j]) for j in range(len(a))])
    if ok: ans += 1

print(ans)