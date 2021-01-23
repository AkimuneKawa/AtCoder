n, x = map(int, input().split())
vp = [map(int, input().split()) for _ in range(n)]
v, p = [list(i) for i in zip(*vp)]

al = 0
notDrunk = True
for i in range(n):
    al += float(v[i] * p[i])
    # ポイント：整数の世界に持ち込んで浮動小数点の演算の誤差を避ける
    if al > x * 100:
        print(i+1)
        notDrunk = False
        break

if notDrunk:
    print(-1)