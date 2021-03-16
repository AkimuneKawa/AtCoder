from sys import stdin
import heapq

def main():
    input = stdin.readline
    n, m, x, y = map(int, input().split())
    x -= 1
    y -= 1

    elist = [[] for _  in range(n)]
    for _ in range(m):
        a, b, t, k = map(int, input().split())
        a -= 1
        b -= 1
        elist[a].append([b, t, k])
        elist[b].append([a, t, k])

    d = []
    heapq.heapify(d)
    d.append((0,x))
    visited = [10**18]*n
    visited[x] = 0

    while len(d) > 0:
        now, r = heapq.heappop(d)
        if r == y:
            print(now)
            return
        for i, t, k in elist[r]:
            time = ((now-1)//k + 1)*k + t
            if time < visited[i]:
                heapq.heappush(d,(time,i))
                visited[i] = time

    print(-1)
    return

main()