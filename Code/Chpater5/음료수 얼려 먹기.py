rowOffset = [-1, 0, 1, 0]
columnOffset = [0, 1, 0, -1]
offsetLength = len(rowOffset)

def bfs(array2D, row, column):
    array2D[row][column] = 1
    for i in range(offsetLength):
        nextRow = row + rowOffset[i]
        nextColumn = column + columnOffset[i]
        if (nextRow >= 0 and nextRow < len(array2D)
                and nextColumn >= 0 and nextColumn < len(array2D[0])
                and array2D[nextRow][nextColumn] == 0) :
            bfs(array2D, nextRow, nextColumn)

def solution(array2D):
    ret = 0
    for i in range(len(array2D)):
        for j in range(len(array2D[0])):
            if array2D[i][j] == 0:
                bfs(array2D, i, j)
                ret += 1
    return ret

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(solution(graph))


