n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = []
for i in range(n):
    if a[i] != x:
        ans.append(a[i])

ans_str = [str(i) for i in ans]

print(" ".join(ans_str))