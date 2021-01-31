n = int(input())

ans = 0
n2 = 2*n
for i in range(1, int(n2 ** 0.5) + 1):
    if n2 % i == 0 and abs(n2/i -i +1) % 2 == 0:
        ans += 2
print(ans)