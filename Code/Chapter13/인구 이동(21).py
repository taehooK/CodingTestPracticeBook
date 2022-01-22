import sys
from collections import deque

rowOffset = [-1, 1, 0, 0]
columnOffset = [0, 0, -1, 1]

limit_number = 10**6
sys.setrecursionlimit(limit_number)

def dfs(area, union, visited, row, column):
    global l, r, n
    sum = area[row][column]

    for i in range(4):
        nextRow = row + rowOffset[i]
        nextColumn = column + columnOffset[i]

        if 0 <= nextRow < len(area) and 0 <= nextColumn < len(area) and (nextRow, nextColumn) not in visited:
            diff = abs(area[row][column] - area[nextRow][nextColumn])
            if l <= diff <= r:
                visited[(nextRow, nextColumn)] = 1
                union.append((nextRow, nextColumn))
                sum += dfs(area, union, visited, nextRow, nextColumn)

    return sum

def solution(area, n):
    associations = deque()
    visited = dict()
    average_deque = deque()
    ret = 0
    while True:
        for i in range(n):
            j = i % 2
            while j < n:
                if (i,j) not in visited:
                    visited[(i,j)] = 1
                    union = deque()
                    union.append((i, j))
                    sum = dfs(area, union, visited, i, j)
                    if len(union) > 1:
                        associations.append(union)
                        average_deque.append(sum // len(union))
                j += 2

        if len(associations) > 0:
            for union in associations:
                average = average_deque.popleft()
                for coordinate in union:
                    area[coordinate[0]][coordinate[1]] = average
            ret += 1
        else:
            break
        associations.clear()
        visited.clear()
        average_deque.clear()

    return ret

def convert_to_index(row, column, length):
    return row * length + column
def get_input():
    n, l, r = map(int, input().split())
    area = []
    for i in range(n):
        area.append(list(map(int, sys.stdin.readline().rstrip().split())))

    return n, area, l, r


if __name__ == '__main__':
    n, area, l, r = get_input()
    print(solution(area, n))
