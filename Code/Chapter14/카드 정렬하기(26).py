import heapq

def get_input():
    n = int(input())
    array = []
    for i in range(n):
        array.append(int(input()))

    return array

def solution(array):
    heap = []
    for value in array:
        heapq.heappush(heap, value)

    sum = 0

    while len(heap) > 1:
        merge = heapq.heappop(heap) + heapq.heappop(heap)
        sum += merge
        heapq.heappush(heap, merge)

    return sum


if __name__ == '__main__':
    array = get_input()
    print(solution(array))