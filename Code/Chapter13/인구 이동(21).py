import sys

rowOffset = [-1, 1, 0, 0]
columnOffset = [0, 0, -1, 1]

limit_number = 10**6
sys.setrecursionlimit(limit_number)

def dfs(area, union, temp, row, column):
    global l, r
    temp[row][column] = 1
    union.append((row, column))

    for i in range(4):
        nextRow = row + rowOffset[i]
        nextColumn = column + columnOffset[i]

        if 0 <= nextRow < len(area) and 0 <= nextColumn < len(area) and temp[nextRow][nextColumn] == -1:
            diff = abs(area[row][column] - area[nextRow][nextColumn])
            if l <= diff <= r:
                dfs(area, union, temp, nextRow, nextColumn)
    if len(union) <= 1:
        temp[row][column] = -1
        del union[0]


def solution(area):
    ret = 0
    while True:
        associations = []
        temp = [[-1] * len(area) for _ in range(len(area))]
        for i in range(len(area)):
            for j in range(len(area)):
                union = []
                if temp[i][j] == -1:
                    dfs(area, union, temp, i, j)
                if len(union) > 0:
                    associations.append(union)

        if len(associations) > 0:
            for union in associations:
                sum = 0
                for coordinate in union:
                    sum += area[coordinate[0]][coordinate[1]]
                average = sum // len(union)
                for coordinate in union:
                    area[coordinate[0]][coordinate[1]] = average
            ret += 1
        else:
            break

    return ret


def get_input():
    n, l, r = map(int, input().split())
    area = []
    for i in range(n):
        area.append(list(map(int, sys.stdin.readline().rstrip().split())))

    return area, l, r


if __name__ == '__main__':
    area, l, r = get_input()
    print(solution(area))
