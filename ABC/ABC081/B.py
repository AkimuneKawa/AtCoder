n = int(input())
l = list(map(int, input().split()))

minimum = 1000
for i, a in enumerate(l):
    x = a
    count = 0
    while x%2 == 0:
        count += 1
        x = int(x/2)
    if count < minimum or i == 0:
        minimum = count

print(minimum)