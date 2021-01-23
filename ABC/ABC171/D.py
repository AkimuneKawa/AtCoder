import collections

def calc_sum(c):
    sum_val = 0
    for key, val in c.items():
        sum_val += key * val
    return sum_val

N = int(input())
arr = list(map(int, input().split()))
Q = int(input())

actions = []

for i in range(Q):
    B, C = map(int, input().split())
    actions.append({'B':B, 'C':C})

c = collections.Counter(arr)
sum_val = calc_sum(c)

for i in range(Q):
    B = actions[i]['B']
    C = actions[i]['C']
    if B in c:
        c[C] += c[B]
        sum_val += c[B] * C - c[B] * B
        c.pop(B)

    print(sum_val)