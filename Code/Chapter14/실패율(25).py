def solution(N, stages):
    answer = []
    sumArray = [0] * (N + 1)
    for stage in stages:
        sumArray[stage - 1] += 1
    count = len(stages)
    for i in range(len(sumArray) - 1):
        if count <= 0:
            answer.append((i + 1, 0))
        else:
            answer.append((i + 1, sumArray[i] / count))
        count -= sumArray[i]

    answer.sort(key=lambda x: -x[1])
    answer= [i[0] for i in answer]

    return answer

if __name__ == '__main__':
    print(solution(5, [2,1,2,6,2,4,3,3,]))
    print(solution(4, [1,1,1,2,2]))
