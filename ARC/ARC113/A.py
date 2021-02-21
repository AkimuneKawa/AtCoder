import collections
import math

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

k = int(input())

ans = 0
for i in range(1, k+1):
    a = prime_factorize(i)
    c = collections.Counter(a)
    tmp = 1
    for key in c.keys():
        bunsi = math.factorial(c[key] + 2)
        bunbo = 2 * math.factorial(c[key])
        tmp *= bunsi / bunbo
    ans += tmp
    
print(int(ans))