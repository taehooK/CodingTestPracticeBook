
ballCount, maxWeight = input().split()
ballWeightList = list(map(int, input().split()))
ret = 0

length = len(ballWeightList)
i = 0
while i < length:
    j = i + 1
    while j < length:
        if ballWeightList[i] != ballWeightList[j]:
            ret += 1
        j += 1
    i += 1

print(ret)