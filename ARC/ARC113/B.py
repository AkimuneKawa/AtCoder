a, b, c = map(int, input().split())

a_l = []
tmp_a = a
while True:
    i = int(str(tmp_a)[-1])
    if i in a_l:
        break
    else:
        a_l.append(i)
        tmp_a = tmp_a * a

yo = pow(b, c, len(a_l))

print(a_l[yo - 1])