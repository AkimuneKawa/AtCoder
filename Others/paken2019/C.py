n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(m-1):
    for j in range(i+1, m):
        sum_point = 0
        for k in range(n):
            sum_point += max(A[k][i], A[k][j])
        ans = max(ans, sum_point)

print(ans)