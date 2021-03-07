a, b = map(int, input().split())

ko = a+b

if ko >= 15 and b >= 8:
    print(1)
elif ko >= 10 and b >= 3:
    print(2)
elif ko >= 3:
    print(3)
else:
    print(4)