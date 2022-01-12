from collections import deque
import sys

def bfs(graph, start, k):
    queue = deque([start])
    iLevelInsertCount = 1
    visited = dict()
    visited[start] = True

    j = 1
    while queue and j <= k:
        count = iLevelInsertCount
        iLevelInsertCount = 0
        i = 0
        while i < count:
            neighbor = graph[queue.popleft()]
            for neighborIndex in neighbor:
                if neighborIndex not in visited:
                    visited[neighborIndex] = True
                    queue.append(neighborIndex)
                    iLevelInsertCount += 1
            i += 1
        j += 1

    return list(queue)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    index, target = map(int, sys.stdin.readline().rstrip().split())
    graph[index].append(target)

ret = bfs(graph, x, k)
ret.sort()

if len(ret) > 0:
    for i in ret:
        print(i)
else:
    print(-1)
