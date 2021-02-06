h, w = map(int, input().split())
s = [input() for _ in range(h)]

ans = 0
for i in range(h-1):
    for j in range(w-1):
        mas = ""
        mas += s[i][j]
        mas += s[i+1][j]
        mas += s[i][j+1]
        mas += s[i+1][j+1]
        if mas.count("#") == 1 or mas.count("#") == 3:
            ans += 1
print(ans)