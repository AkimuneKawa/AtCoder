n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    str_i = str(i)
    arr = list(map(int, str_i))
    s = sum(arr)
    if s <= b and s >= a:
        ans += i
print(ans)