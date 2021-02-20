n, m, x, y = map(int, input().split())

d = {}
for _ in range(m):
    a, b, t, k = map(int, input().split())
    if a in d.keys():
        d[a].append([b, t, k])
    else:
        d[a] = [[b, t, k]]
    if b in d.keys():
        d[b].append([a, t, k])
    else:
        d[b] = [[a, t, k]]

mins = [-1 for _ in range(n+1)]
    
mins[x] = 0