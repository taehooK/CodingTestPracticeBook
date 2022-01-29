def solution(array, c):
    array.sort()

    min_gap = 1#최소 gap
    max_gap = array[-1] - array[0]    #최대 gap
    ret = 0

    while min_gap <= max_gap:
        middle_gap = (min_gap + max_gap) // 2
        count = 1
        previous = array[0]
        i = 1
        while i < len(array):
            if array[i] - previous >= middle_gap:
                count += 1
                previous = array[i]
            i += 1

        if count >= c:
            min_gap = middle_gap + 1
            ret = middle_gap
        else:
            max_gap = middle_gap - 1

    return ret

def get_input():
    n, c = map(int, input().split())
    array = []
    for _ in range(n):
        array.append(int(input()))

    return n, c, array

n, c, array = get_input()
print(solution(array, c))

