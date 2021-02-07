import math
from decimal import Decimal
x,y,r=map(Decimal,input().split())
n=0
for i in range(math.ceil(x-r),math.floor(x+r)+1):
    p=((r**2)-(x-i)**2).sqrt()
    n+=math.floor(y+p)-math.ceil(y-p)+1
print(n)