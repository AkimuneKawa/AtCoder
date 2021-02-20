x = input()
m = int(input())

l = [int(c) for c in x]
d = max(l)

l.reverse()
n = d
ans = 0

while True:
    n += 1
    val = 0
    for i in range(len(l)):
        val += l[i] * n ** i
    if val <= m:
        ans += 1
    else:
        break
print(ans)