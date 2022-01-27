import time

def binary_search_left(array, value):
    start = 0
    end = len(array) - 1

    while start <= end:
        if array[start] == value:
            return start

        middle = (start + end) // 2
        if array[middle] == value and middle > 0 and array[middle - 1] != value:
            return middle
        elif value > array[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return -1


def binary_search_right(array, value):
    start = 0
    end = len(array) - 1

    while start <= end:
        if array[end] == value:
            return end

        middle = (start + end) // 2
        if array[middle] == value and middle < len(array) and array[middle + 1] != value:
            return middle
        elif value >= array[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return -1

def solution(array, number):
    startIndex = binary_search_left(array, number)
    endIndex = binary_search_right(array, number)

    if startIndex == -1:
        return -1
    return endIndex - startIndex + 1

def get_input():
    count, x = map(int, input().split())
    array = list(map(int, input().split()))

    return array, x

array, x = get_input()
print(solution(array, x))


