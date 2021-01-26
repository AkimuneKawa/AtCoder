def f(a, b):
    return max(len(str(a)), len(str(b)))

n = int(input())

i = 1
ans = n
while i**2 <= n:
    if n % i == 0:
        ans = min(ans, f(i, int(n / i)))
    i += 1

print(ans)