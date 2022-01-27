def binary_search(array, value):
    start = 0
    end = len(array) - 1

    while start < end:
        middle = (start + end) // 2
        if array[middle] == value:
            return middle
        elif array[middle] > value:
            start = middle + 1
        else:
            end = middle - 1
    return -1

def solution(array, number):
    index = binary_search(array, number)
    if index == -1:
        return -1
    count = 1
    i = index - 1
    while i >= 0 and array[i] == number:
        count += 1
        i -= 1
    i = index + 1
    while i < len(array) and array[i] == number:
        count += 1
        i += 1

    return count

def get_input():
    count, x = map(int, input().split())
    array = list(map(int, input().split()))

    return array, x

array, x = get_input()
print(solution(array, x))



