from collections import deque
import sys

rowOffset = [-1, 1, 0, 0]
columnOffset = [0, 0, -1, 1]

def bfs(area, virusPositionQueue):
    count = len(virusPositionQueue)
    for i in range(count):
        position = virusPositionQueue.popleft()
        #상하 좌우로 퍼트리기
        for j in range(4):
            nextPos = (position[0] + rowOffset[j], position[1] + columnOffset[j])
            if (0 <= nextPos[0] < len(area)
                    and 0 <= nextPos[1] < len(area)
                and area[nextPos[0]][nextPos[1]] == 0):
                #퍼트리고 큐에 담는다.
                area[nextPos[0]][nextPos[1]] = area[position[0]][position[1]]
                virusPositionQueue.append((nextPos[0], nextPos[1]))

def solution(area, time, x, y, k):
    virusPosQueueList = [deque() for _ in range(k)]
    #큐의 배열 만들고 바이러스의 위치들담기
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] > 0:
                index = area[i][j] - 1
                virusPosQueueList[index].append((i, j))
    for i in range(time):
        for virusPosQueue in virusPosQueueList:
            bfs(area, virusPosQueue)

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

