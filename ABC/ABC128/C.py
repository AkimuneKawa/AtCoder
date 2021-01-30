n, m = map(int, input().split())
s = [list(map(int, input().split())) for _ in range(m)]
k = [l.pop(0) for l in s]
p = list(map(int, input().split()))

count = 0
for i in range(2 ** n):
    all_on = True
    for j in range(m):
        sum_on = 0
        for k in range(n):
            if ((i >> k) & 1) and (k+1 in s[j]):
                sum_on += 1
        if sum_on % 2 != p[j]:
            all_on = False
    if all_on:
        count += 1

print(count)