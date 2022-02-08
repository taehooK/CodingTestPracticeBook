import random
def solution(array):
    length = len(array)
    memory = [0] * length

    memory[0] = array[0]
    memory[1] = max(array[0], array[1])

    for i in range(2, length):
        memory[i] = max(memory[i - 1], memory[i - 2] + array[i])
    return max(memory[length - 2], memory[length - 1])

def bookSolution(array):
    d = [0] * 100
    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        d[i] = max(d[i - 1], d[i - 2] + array[i])
    return d[len(array) - 1]


for i in range(5):
    array = []
    for i in range(100):
        array.append(random.randint(1, 100))
    print(solution(array))
    print(bookSolution(array))