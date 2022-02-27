def find_parent(parent, node_index):
    if parent[node_index] != node_index:
        parent[node_index] = find_parent(parent, parent[node_index])
    return parent[node_index]

def union_parent(parent, one, other):
    parent_of_one = find_parent(parent, one)
    parent_of_other = find_parent(parent, other)

    if parent_of_one < parent_of_other:
        parent[other] = one
    else:
        parent[one] = other

def solution():
    n, m, parent_array = set_up()
    target_numbers = list(map(int, input().split()))

    parent = find_parent(parent_array, target_numbers[0] - 1)
    for i in range(1, len(target_numbers)):
        current_parent = find_parent(parent_array, target_numbers[i] - 1)
        if parent != current_parent:
            return 'NO'

    return 'YES'

def set_up():
    n, m = map(int, input().split())
    parent = [0] * n

    for i in range(1, n):
        parent[i] = i

    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
        for j in range(n):
            if matrix[i][j] == 1:
                union_parent(parent, i, j)

    return n, m, parent

print(solution())

