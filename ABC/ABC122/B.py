s = input()

length = 0
for i in range(len(s)):
    count = 0
    for j in range(i, len(s)):
        if s[j] == 'A' or s[j] == 'C' or s[j] == 'G' or s[j] == 'T':
            count += 1
        else:
            length = max(length, count)
            count = 0
    length = max(length, count)

print(length)