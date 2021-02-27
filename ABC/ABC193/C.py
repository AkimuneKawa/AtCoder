n = int(input())

m = 2
while m ** 2 <= n:
    m += 1

count = 0
s = set()
for i in range(2, m):
    j = 2
    while i ** j <= n:
        if i ** j not in s:
            s.add(i ** j)
            count += 1
        j += 1
print(n-count)