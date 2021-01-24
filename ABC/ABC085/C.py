n, y = map(int, input().split())

for i in range(n+1):
    for j in range(n-i+1):
        if 1000*i + 5000*j + 10000*(n-i-j) == y:
            print(n-i-j, j, i)
            exit()
print(-1,-1,-1)