n, k = map(int, input().split())

def g_1(x):
    s = [int(c) for c in str(x)]
    s.sort(reverse=True)
    st = [str(i) for i in s]
    ret = "".join(st)
    if ret == "":
        return 0
    else:
        return int(ret)

def g_2(x):
    s = [int(c) for c in str(x)]
    s.sort()
    ret = ""
    for i in s:
        if i != 0:
            ret += str(i)
    if ret == "":
        return 0
    else:
        return int(ret)

def f(x):
    return g_1(x) - g_2(x)

ans = n
for _ in range(k):
    ans = f(ans)

print(ans)