import sys

def solution():
    n = int(input())
    m = int(input())

    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    # 대각 원소 0으로 채우기
    for i in range(1, n + 1):
        graph[i][i] = 0

    for i in range(m):
        start, end, price = map(int, sys.stdin.readline().rstrip().split())
        if price < graph[start][end]:
            graph[start][end] = price

    # 플로이드 워셜 알고리즘
    # 1. 첫번째 부터 노드 개수까지 반복
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                print(0, end=' ')
            else:
                print(graph[i][j], end=' ')
        print()

solution()