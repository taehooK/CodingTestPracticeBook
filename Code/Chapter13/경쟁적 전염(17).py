from collections import deque
import sys

rowOffset = [-1, 1, 0, 0]
columnOffset = [0, 0, -1, 1]
def getQueue(area, k):
    virus = list()
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] > 0:
                virus.append((area[i][j], i, j))
    virus.sort()
    queue = deque(virus)

    return queue

def spread(area, queue, virusInfo):
    newInsertCount = 0
    for j in range(4):
        row = virusInfo[1] + rowOffset[j]
        column = virusInfo[2] + columnOffset[j]
        if 0 <= row < len(area) and 0 <= column < len(area) and area[row][column] == 0:
            # 퍼트리고 큐에 담는다.
            area[row][column] = area[virusInfo[1]][virusInfo[2]]
            queue.append((area[row][column], row, column))
            newInsertCount += 1
    return newInsertCount

def solution(area, time, x, y, k):
    queue = getQueue(area, k)
    newInsertCount = len(queue)

    i = 1
    while i <= time and newInsertCount > 0:
        count = newInsertCount
        newInsertCount = 0
        j = 1
        while j <= count:
            virusInfo = queue.popleft()
            newInsertCount += spread(area, queue, virusInfo)
            j += 1
        i += 1
    return area[x - 1][y - 1]

def get_input():
    n, k = map(int, input().split())
    area = []
    for i in range(n):
        area.append(list(map(int, sys.stdin.readline().rstrip().split())))
    s, x, y = map(int, input().split())

    return area, s, x, y, k

if __name__ == "__main__":
    area, s, x, y, k = get_input()
    ret = solution(area, s, x, y, k)
    print(ret)

