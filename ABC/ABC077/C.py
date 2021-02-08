import bisect

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

a.sort()
c.sort()

ans = 0
for x in b:
    num_a = bisect.bisect_left(a, x)
    num_c = len(c) - bisect.bisect_right(c, x)
    ans += num_a * num_c
print(ans)