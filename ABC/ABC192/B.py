s = input()

flag = True
for i in range(len(s)):
    if i % 2 == 0:
        if s[i].isupper():
            flag = False
    else:
        if s[i].islower():
            flag = False

if flag:
    print("Yes")
else:
    print("No")