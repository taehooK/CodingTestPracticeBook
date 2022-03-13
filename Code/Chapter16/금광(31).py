def solution(array_2d):
    n = len(array_2d)
    m = len(array_2d[0])
    memory = [[0] * m for _ in range(n)]
    max = 0

    for column in range(m): # 열만큼 반복
        for row in range(n): # 행만큼 반복
            # 금강원소랑 max(메모리의 왼쪽 위, 왼쪽, 왼쪽 아래)와 더하고 메모리제이션에 기록
            value = array_2d[row][column]
            plus_value = 0
            if row - 1 >= 0 and column - 1 >= 0:
                plus_value = memory[row - 1][column - 1] #왼쪽 위
            if column - 1 >= 0 and memory[row][column - 1] > plus_value: #왼쪽
                plus_value = memory[row][column - 1]
            if row + 1 < n and column - 1 >= 0 and memory[row + 1][column - 1] > plus_value: #왼쪽 아래
                plus_value = memory[row + 1][column - 1]

            memory[row][column] = value + plus_value # 최대값 기록
            if memory[row][column] > max:
                max = memory[row][column]
    return max
def get_input():
    t = int(input())
    array_3d = []

    for _ in range(t):
        n, m = map(int, input().split())
        temp = list(map(int, input().split()))
        array_2d = []
        index = 0
        for i in range(n):
            array = []
            for j in range(m):
                array.append(temp[index])
                index += 1
            array_2d.append(array)
        array_3d.append(array_2d)

    return array_3d

array_3d = get_input()
for array_2d in array_3d:
    print(solution(array_2d))








