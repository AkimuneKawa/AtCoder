n = int(input())
a = []
b = []
for _ in range(n):
    A, B = map(int, input().split())
    a.append(A)
    b.append(B)

ans = 10 ** 11

for i in range(n):
    ans = min(ans, a[i]+b[i])

a_min = a.index(min(a))
b_min = b.index(min(b))

if a_min != b_min:
    print(min(ans, max(a[a_min], b[b_min])))
else:
    a_new = [i for i in a if i != a[a_min]]
    if len(a_new) == 0:
        a_new.append(a[a_min])
    b_new = [i for i in b if i != b[b_min]]
    if len(b_new) == 0:
        b_new.append(b[b_min])
    print(min([ans, max(a[a_min], min(b_new)), max(min(a_new), b[b_min])]))