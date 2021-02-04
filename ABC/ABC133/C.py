n, d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        s = 0
        for k in range(d):
            s += (X[i][k] - X[j][k]) ** 2
        if int(s ** 0.5) - s ** 0.5 == 0: ans += 1

print(ans)