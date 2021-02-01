import itertools

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

perm = itertools.permutations(range(1, n+1))

str_perm = [''.join([str(i) for i in one]) for one in perm]
str_perm.sort()
perm = [[int(c) for c in one] for one in str_perm]

print(abs(perm.index(p) - perm.index(q)))