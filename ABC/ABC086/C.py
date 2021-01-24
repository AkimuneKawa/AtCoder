n = int(input())
txy = [list(map(int, input().split())) for _ in range(n)]
txy.insert(0, [0,0,0])
t, x, y = [list(i) for i in zip(*txy)]

for i in range(1, n+1):
    time = t[i] - t[i-1]
    dist = abs(x[i] - x[i-1]) + abs(y[i] - y[i-1])
    if not(time >= dist and (time - dist) % 2 == 0):
        print("No")
        exit()

print("Yes")