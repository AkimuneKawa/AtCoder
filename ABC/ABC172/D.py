N = int(input())
A = list(map(int, input().split()))

A = sorted(A, reverse=True)

A_map = {}
for val in A:
    A_map[val] = 0

count = 0
for i in range(A):
    if i == 0:
        A_map[A[i]] = 1
    else:
        count += max(A_map)
        A_map[max(A_map)] -= 1
        if A_map[max(A_map)] == 0:
            del A_map[max(A_map)]
        

        