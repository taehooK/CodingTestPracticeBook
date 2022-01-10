from collections import deque
rowOffset = [-1, 0, 1, 0]
columnOffset = [0, 1, 0, -1]
offsetLength = len(rowOffset)

def bfs(graph, startRow, startColumn):
    graph[startRow][startColumn] = 2
    queue = deque()
    queue.append((startRow, startColumn))
    minCount = 1
    appendCount = 1
    gameClear = False

    while not gameClear:
        count = appendCount
        appendCount = 0
        for i in range(count):
            coordinate = queue.popleft()
            for i in range(offsetLength):
                row = coordinate[0] + rowOffset[i]
                column = coordinate[1] + columnOffset[i]
                if row == len(graph) - 1 and column == len(graph[0]) - 1:
                    gameClear = True
                elif ( row >= 0 and row < len(graph) and column >= 0 and
                     column < len(graph[0]) and graph[row][column] == 1):
                     graph[row][column] = 2
                     queue.append((row, column))
                     appendCount+= 1
        minCount += 1

    return minCount


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(bfs(graph, 0, 0))