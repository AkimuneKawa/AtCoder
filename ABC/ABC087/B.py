a = int(input())
b = int(input())
c = int(input())
x = int(input())

count = 0
for i_a in range(a+1):
    for i_b in range(b+1):
        for i_c in range(c+1):
            if 500*i_a + 100*i_b + 50*i_c == x:
                count += 1
print(count)
