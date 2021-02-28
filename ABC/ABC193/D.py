def score(a):
    c_i = [0] * 10
    for c in a:
        c_i[int(c)] += 1
    ret = 0
    for i in range(1, 10):
        ret += i * 10 ** c_i[i]
    return ret

k = int(input())
s = input()[:4]
t = input()[:4]

cards = {}
for i in range(1, 10):
    cards[i] = k - (s+t).count(str(i))

denom = (9*k - 8) * (9*k - 9)
numer = 0

for i in range(1, 10):
    if cards[i] == 0:
        continue
    for j in range(1, 10):
        if cards[j] == 0 or i == j:
            continue
        takahashi = score(s + str(i))
        aoki = score(t + str(j))
        if takahashi > aoki:
            numer += cards[i] * cards[j]

for i in range(1, 10):
    if cards[i] == 0:
        continue
    takahashi = score(s + str(i))
    aoki = score(t + str(i))
    if takahashi > aoki:
        numer += cards[i] * (cards[i]-1)

print(numer/denom)