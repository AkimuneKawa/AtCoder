N, K = map(int, input().split())
prices = list(map(int, input().split()))

sum_price = 0

for i in range(K):
    min_price = min(prices)
    sum_price += min_price
    prices.remove(min_price)

print(sum_price)