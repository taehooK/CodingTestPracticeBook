def solution(array):
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2
        if middle == array[middle]:
            return middle
        elif middle > array[middle]:#1. 가운데 인덱스가 가운데 숫자보다 크면 오른쪽에서 탐색
            start = middle + 1
        else:
            end = middle - 1
    return -1

def get_input():
    n = int(input())
    array = list(map(int, input().split()))

    return array

array = get_input()
print(solution(array))







