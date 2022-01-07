

count = int(input())
coins = list(map(int, input().split()))
list.sort(coins)

priceSet = set([0])

for coin in coins:
    priceList = list(priceSet)
    for price in priceList:
        sum = coin + price
        priceSet.add(sum)

maxPrice = max(priceSet)
i = 1
while i < maxPrice:
    if i not in priceSet:
        break
    i += 1

minPriceSum = i
print(minPriceSum)
