import math

K = int(input())
S = input()

ret = 0

for i in range(len(S),len(S)+K+1):
    n = i - 1
    r = len(S) - 1
    c = math.factorial(n) / (math.factorial(r) * math.factorial(n-r))
    selection = 25 ** (K-(K+len(S)-i)) * 26 ** (K+len(S)-i)
    ret += c * selection

print(int(ret % (10 ** 9 + 7)))