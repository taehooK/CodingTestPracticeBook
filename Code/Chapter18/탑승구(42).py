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

def solution():
    g = int(input())
    p = int(input())

    parent = [0] * (g + 1)
    for i in range(1, g + 1):
        parent[i] = i
    ret = 0

    for i in range(p):
        info = int(input())
        root = find_parent(parent, info)

        if root == 0:
            break
        union_parent(parent, root, root - 1)
        ret += 1

    return ret

print(solution())



