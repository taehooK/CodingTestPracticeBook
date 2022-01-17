def dfs(i, numbers, value):
    global n, min, max, plusCount, minusCount, divideCount, multiplyCount
    #종료조건
    if i == n:
        if value > max:
            max = value
        if value < min:
            min = value
        return value

    #수행문
    if plusCount > 0:
        plusCount -= 1
        dfs(i + 1, numbers, value + numbers[i])
        plusCount += 1

    if minusCount > 0:
        minusCount -= 1
        dfs(i + 1, numbers, value - numbers[i])
        minusCount += 1

    if multiplyCount > 0:
        multiplyCount -= 1
        dfs(i + 1, numbers, value * numbers[i])
        multiplyCount += 1

    if divideCount > 0:
        divideCount -= 1
        dfs(i + 1, numbers, int(value / numbers[i]))
        divideCount += 1



if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    plusCount, minusCount, multiplyCount, divideCount = map(int, input().split())
    min = 1000000000
    max = -1000000000
    dfs(1, numbers, numbers[0])
    print(max)
    print(min)