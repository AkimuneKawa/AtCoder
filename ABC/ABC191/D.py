import math
from decimal import *
 
x, y, r = map(float, input().split())
 
x_c = math.ceil(x-r)
x_f = math.floor(x+r)

getcontext().prec = 10
 
ans = 0
for i in range(x_c, x_f + 1):
    p = Decimal(str(r**2 - (x - i)**2))**Decimal('0.5')
    y_c = math.ceil(Decimal(str(y)) - p)
    y_f = math.floor(Decimal(str(y)) + p)
    ans += y_f - y_c + 1
print(ans)