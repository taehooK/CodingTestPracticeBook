def solution(array_2d, n):
    row = 0
    for array in array_2d:
        length = len(array)
        for i in range(length):
            top_row, top_right_column = row - 1
            top_left_column = i - 1
            top_right_column = i
            top_left = 0
            top_right = 0

            if top_row >= 0 and top_left_column >= 0:
                top_left = array_2d[top_row][top_left_column]
            if top_row >= 0 and top_right_column < length - 1:
                top_right = array_2d[top_row][top_right_column]
            array_2d[row][i] = array_2d[row][i] + max(top_left, top_right)

        row += 1
    return max(array_2d[n - 1])

def get_input():
    n = int(input())
    array_2d = []

    for i in range(n):
        array_2d.append(list(map(int, input().split())))

    return array_2d, n

array_2d, n = get_input()
print(solution(array_2d, n))
