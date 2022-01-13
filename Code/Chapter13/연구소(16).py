from itertools import combinations
from collections import deque
import copy

rowOffset = [-1, 1, 0, 0]
columnOffset = [0, 0, -1, 1]
def getZeroAndVirusCount(area):
    zeroCount = 0
    virusCount = 0
    for row in area:
        for data in row:
            if data == 0:
                zeroCount += 1
            if data == 2:
                virusCount += 1
    return zeroCount, virusCount

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

n, m = map(int, input().split())
area = []
for i in range(n):
    area.append(list(map(int, input().split())))
#모든 빈칸 좌표 찾고 데이터 넣기
emptySpace = []
virusPosition = deque()

for i in range(len(area)):
    for j in range(len(area[0])):
        if area[i][j] == 0:
            emptySpace.append((i, j))
        elif area[i][j] == 2:
            virusPosition.append((i, j))
combination = list(combinations(emptySpace, 3))
prtinArea = area
maxCount = 0
minVirusCount = n * m
for i in range(len(combination)):
    copyArea = copy.deepcopy(area)
    for coordinate in combination[i]:
        copyArea[coordinate[0]][coordinate[1]] = 1
    bfs(copyArea, copy.deepcopy(virusPosition), minVirusCount)
    zeroCount, virusCount = getZeroAndVirusCount(copyArea)
    minVirusCount = min(virusCount - len(virusPosition), minVirusCount)
    maxCount = max(zeroCount, maxCount)

print(maxCount)

