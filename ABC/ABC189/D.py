def f(s):
    if len(s) == 1:
        if s[0] == "AND":
            return 1
        else:
            return 3
    elif len(s) > 1:
        if s[-1] == "AND":
            return f(s[:-1])
        else:
            return 2 ** (len(s)) + f(s[:-1])

n = int(input())
s = [input() for _ in range(n)]

print(f(s))
