n = int(input())
a = list(map(int, input().split()))

a2 = [i**2 for i in a]
print(sum(a2) * len(a) - sum(a)**2)