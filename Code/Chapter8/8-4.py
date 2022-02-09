#점화식 a(i) = min(a(i), a(i-k) + 1))
def solution(coins, target_price):
    number_of_price = [10001] * (target_price + 1)

    for coin in coins:
        number_of_price[coin] = 1

    for i in range(2, target_price + 1):
        for coin in coins:
            if i - coin >= 0:
                number_of_price[i] = min(number_of_price[i], number_of_price[i - coin] + 1)

    ret = number_of_price[target_price]
    if ret > 10000:
        ret = -1
    return ret

def bookSolution(array, n, m):
    d = [10001] * (m + 1)
    d[0] = 0
    for i in range(n):
        for j in range(array[i], m + 1):
            if d[j - array[i]] != 10001:
                d[j] = min(d[j], d[j - array[i]] + 1)

    ret = d[m]
    if ret > 10000:
        ret = -1
    return ret

def get_input():
    n, m = map(int, input().split())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))

    return numbers, m, n

numbers, m, n = get_input()
print(solution(numbers, m))
print(bookSolution(numbers, n, m))









