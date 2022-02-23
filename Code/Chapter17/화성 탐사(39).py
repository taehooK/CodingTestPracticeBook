import heapq

def solution(graph, n):
    q = []

    row_offset = [-1, 1, 0, 0]
    column_offset = [0, 0, -1, 1]

    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]

    start = (graph[0][0], 0, 0)
    heapq.heappush(q, start)

    while q:
        cost, row, column = heapq.heappop(q)
        if distance[row][column] < cost:
            continue

        for i in range(4):
            current_row = row + row_offset[i]
            current_column = column + column_offset[i]
            if 0 <= current_row < n and 0 <= current_column < n:
                current_cost = cost + graph[current_row][current_column]
                if current_cost < distance[current_row][current_column]:
                    heapq.heappush(q, (current_cost, current_row, current_column))
                    distance[current_row][current_column] = current_cost

    return distance[n - 1][n - 1]

def get_input():
    n = int(input())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    return graph, n


t = int(input())
for i in range(t):
    graph, n = get_input()
    print(solution(graph, n))

#다익 스트라 알고리즘(우선순위 큐 이용)



#출력한다.