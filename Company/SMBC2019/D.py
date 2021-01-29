n = int(input())
s = input()

count = 0
keyset = set()
for i in range(10):
    for j in range(10):
        for k in range(10):
            if str(i) in s:
                first = s.index(str(i))
                l = s[first+1:]
                if str(j) in l:
                    second = l.index(str(j))
                    l = l[second+1:]
                    if str(k) in l:
                        if not (str(i) + str(j) + str(k) in keyset):
                            count += 1
                            keyset.add(str(i) + str(j) + str(k))
print(count)