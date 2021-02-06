v, t, s, d = map(int, input().split())

if v * t <= d and v * s >= d:
    print("No")
else:
    print("Yes")