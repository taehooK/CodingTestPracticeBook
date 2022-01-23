def get_input():
    n = int(input())
    array = list(map(int, input().split()))

    return array

def solution(array):
    array.sort()

    middle = len(array) // 2
    if len(array) % 2 == 0:
        middle -= 1

    return array[middle]
if __name__ == '__main__':
    array = get_input()
    print(solution(array))
