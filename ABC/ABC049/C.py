s = input()

while len(s) != 0:
    if s.endswith("erase"):
        s = s[:-5]
    elif s.endswith("eraser"):
        s = s[:-6]
    elif s.endswith("dream"):
        s = s[:-5]
    elif s.endswith("dreamer"):
        s = s[:-7]
    else:
        print("NO")
        exit()

print("YES")