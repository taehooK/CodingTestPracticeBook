import heapq

def get_input():
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]
    for i in range(m):
        start, end = map(int, input().split())
        graph[start - 1].append(end - 1)
        graph[end - 1].append(start - 1)

    return n, m, graph

def solution(graph, n, m):

# 다익스트라 알고리즘 돌리고 최솟값 찾고 구하기
    q = []
    INF = int(1e9)
    distance = [INF] * n

    start = (0, 0)
    distance[0] = 0
    heapq.heappush(q, start)

    while q:
        cost, index = heapq.heappop(q)

        if distance[index] < cost:
            continue

        for neighbor in graph[index]:
            current_cost = cost + 1
            if current_cost < distance[neighbor]:
                distance[neighbor] = current_cost
                heapq.heappush(q, (current_cost, neighbor))

    max_distance = max(distance)
    max_index = distance.index(max_distance) + 1
    count = distance.count(max_distance)

    return max_index, max_distance, count

n, m, graph = get_input()
min_index, distance, count = solution(graph, n, m)
print(min_index, distance, count)
