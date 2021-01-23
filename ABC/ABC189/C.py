n = int(input())
l = list(map(int, input().split()))

M = 0

for i in range(n-1):
    m = l[i]
    for j in range(i, n):
        m = min(m, l[j])
        M = max(M, m*(j-i+1))
 
print(M)

# O(N^2)になってて解説通りだがPythonではギリギリ通らない...