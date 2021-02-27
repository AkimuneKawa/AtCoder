t = int(input())
for _ in range(t):
    x, y, p, q = map(int, input().split())
    if max(2*x+2*y, p+q) % min(2*x+2*y, p+q) == 0 and (x <= p+q or x+y <+ p):
        print("infinity")
    else:
        n = 0
        m = 0
        while True:
            if not ((2*x + 2*y) * n + x >= (p+q)*(m+1) or (2*x + 2*y) * n + x + y <= (p+q)*m + p):
                print(max((p+q)*m + p, (2*x + 2*y) * n + x))
                break
            elif (p+q)*m + p > (2*x + 2*y) * n + x:
                n += 1
            else:
                m += 1