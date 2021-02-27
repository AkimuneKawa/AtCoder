import collections

def score(a):
    l = [int(c) for c in a]
    c = collections.Counter(l)
    score = 0
    for i in range(1, 10):
        if i in c.keys():
            c_i = c[i]
        else:
            c_i = 0
        score += i * 10 ** c_i
    return score

k = int(input())
s = input()
t = input()

bunbo = (9*k - 8) * (9*k - 9)

patterns = []

for i in range(1, 10):
    for j in range(1, 10):
        takahashi = score(s[:4] + str(i))
        aoki = score(t[:4] + str(j))
        if takahashi > aoki:
            patterns.append([i, j])

cards = {}

for i in range(1, 10):
    cards[i] = k - (s+t).count(str(i))

bunsi = 0
for p in patterns:
    tmp_cards = cards.copy()
    if tmp_cards[p[0]] > 0:
        tmp = tmp_cards[p[0]]
        tmp_cards[p[0]] -= 1
        bunsi += tmp * tmp_cards[p[1]]

print(bunsi/bunbo)