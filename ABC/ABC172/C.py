import copy

H, W, K = map(int, input().split())

c = []

for i in range(H):
    row = list(input())
    c.append(row)

count = 0
for i in range(2 ** len(c)):        
    tmp_c = [c[k] for k in range(len(c)) if ((i >> k) & 1)]
    for j in range(2 ** len(c[0])):
        tmp_tmp_c = copy.copy(tmp_c)
        for l in range(len(tmp_c)):
            tmp_tmp_c[l] = [tmp_c[l][k] for k in range(len(tmp_c[0])) if ((j >> k) & 1)]

        total_blacks = 0
        for i in range(len(tmp_tmp_c)):
            total_blacks += tmp_tmp_c[i].count('#')
        
        if total_blacks == K:
            count += 1

print(count)