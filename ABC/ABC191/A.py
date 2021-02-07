v, t, s, d = map(int, input().split())

print("Yes" if v * t > d or v * s < d else "No")