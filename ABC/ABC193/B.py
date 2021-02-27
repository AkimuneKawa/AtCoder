n = int(input())

ans = 10 ** 10
can = False
for _ in range(n):
    A, P, X = map(int, input().split())
    if X - A > 0:
        can = True
        ans = min(ans, P)

if can:
    print(ans)
else:
    print(-1)
    