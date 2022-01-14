from itertools import combinations
from collections import deque
import copy

rowOffset = [-1, 1, 0, 0]
columnOffset = [0, 0, -1, 1]

def bfs(area, virusPosition, minVirusCount):
    addedvirusCount = 0
    #남은 바이러스가 있는 동안 반복
    while virusPosition and addedvirusCount < minVirusCount:
        position = virusPosition.popleft()
        for i in range(4):
            row = position[0] + rowOffset[i]
            column = position[1] + columnOffset[i]
            if row >= 0 and row < len(area) and column >= 0 and column < len(area[0]) and area[row][column] == 0:
                area[row][column] = 2
                virusPosition.append((row, column))
                addedvirusCount += 1

    return addedvirusCount

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))

emptySpace = []
virusPosition = deque()

for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j] == 0:
            emptySpace.append((i, j))
        elif area[i][j] == 2:
            virusPosition.append((i, j))

emptySpaceLength = len(emptySpace) - 3 # 울타리 제외
combination = list(combinations(emptySpace, 3))
prtinArea = area
maxCount = 0
minAddedVirusCount = n * m
for i in range(len(combination)):
    copyArea = [item[:] for item in area]
    for coordinate in combination[i]:
        copyArea[coordinate[0]][coordinate[1]] = 1
    addedVirusCount = bfs(copyArea, copy.deepcopy(virusPosition), minAddedVirusCount)
    zeroCount = emptySpaceLength - addedVirusCount
    minAddedVirusCount = min(addedVirusCount, minAddedVirusCount)
    maxCount = max(zeroCount, maxCount)

print(maxCount)

