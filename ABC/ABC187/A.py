a, b = input().split()

a_num = sum(list(map(int, a)))
b_num = sum(list(map(int, b)))

if a_num >= b_num:
    print(a_num)
else:
    print(b_num)