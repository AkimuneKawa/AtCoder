N = int(input())
ans = 0
for i in range(1, N):
    ans += N / (N-i)
print(ans)