def find_parent(parent, node_index):
    if parent[node_index] != node_index:
        parent[node_index] = find_parent(parent, parent[node_index])
    return parent[node_index]
def union_parent(parent, one, other):
    one = find_parent(parent, one)
    other = find_parent(parent, other)

    if one < other:
        parent[other] = one
    else:
        parent[one] = other
def set_up():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        start, end, cost = map(int, input().split())
        edges.append((cost, start, end))

    edges.sort()

    return n, m, edges

def solution():
    n, m, edges = set_up()

    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i
    ret = 0

    for edge in edges:
        cost, start, end = edge
        if find_parent(parent, start) != find_parent(parent, end):
            union_parent(parent, start, end)
        else:
            ret += cost

    return ret

print(solution())




