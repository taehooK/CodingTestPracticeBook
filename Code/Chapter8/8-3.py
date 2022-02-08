

def solution(n):
    memory = [0] * (n + 1)

    memory[1] = 1
    memory[2] = 3

    for i in range(3, n +1):
        memory[i] = (memory[i - 1] + (2 * memory[i - 2])) % 796796

    return memory[n]

def bookSolution(n):
    d = [0] * (n + 1)

    d[1] = 1
    d[2] = 3
    for i in range(3, n + 1):
        d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

    return d[n]
n = 308
print(solution(n))
print(bookSolution(n))

