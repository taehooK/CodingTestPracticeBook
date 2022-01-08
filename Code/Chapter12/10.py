def solution(key, lock):
    keySideLength = len(key)
    keySpinCount = 0
    for list in key:
        for j in list:
            if j == 1:
                keySpinCount += 1

    lockSlotCount = 0
    for list in lock:
        for j in list:
            if j == 0:
                lockSlotCount += 1

    if lockSlotCount > keySpinCount:
        return False

    lockLength = len(lock)
    i = 1
    while i <= 4:
        keyRowOffset = 1 - keySideLength
        while keyRowOffset < lockLength:
            keyColumnOffset = 1 - keySideLength
            while keyColumnOffset < lockLength:
                if checkTwoArrayMatch(key, lock, keyRowOffset, keyColumnOffset, lockSlotCount):
                    return True
                keyColumnOffset += 1
            keyRowOffset += 1
        key = rotate_90(key)
        i += 1

    return False

def checkTwoArrayMatch(key, lock, keyRowOffset, keyColumnOffset, lockSlotCount):
    keySideLength = len(key)
    lockLength = len(lock)

    i = 0
    slotMatchCount = 0
    isUnMatch = False
    while i < keySideLength and not isUnMatch:
        lockY = i + keyRowOffset
        j = 0
        while j < keySideLength and lockY < lockLength and lockY >= 0:
            lockX = j + keyColumnOffset
            if lockX < lockLength and lockX >= 0:
                if key[i][j] == lock[lockY][lockX]:
                    isUnMatch = True
                    break
                elif lock[lockY][lockX] == 0:
                    slotMatchCount += 1
            j += 1
        i += 1

    if slotMatchCount == lockSlotCount:
        return True
    return False

def rotate_90(array):
    N = len(array)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = array[r][c]
    return ret

key = [[0, 0 , 0],
       [1, 0, 0],
       [0, 1, 1]]
lock = [[1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]]

print(solution(key, lock)) # True


#key의 행 offset
#key의 열 offset

#1. key의 행 offset이 lock의 행 개수보다 작은만큼 반복한다,
#1.1. key의 열 offset이 lock의 열개수보다 작은만큼 반복한다.
 #1.1.1. key의 행개수만큼 반복한다.
   #1.1.1.1. key의 열 개수만큼 반복
    #1.1.1.1.1. offset을 적용한 좌표가 lock의 범위안에 있으면
     #1.1.1.1.1.1. 두 수가 같으면 현재의 offset을 더 이상 비교히지 않는다.
     #1.1.1.1.1.2. lock의 값이 0이면 일치하는 홈 개수를 센다.
 #1.1.2.일치하는 홈개수가 자물쇠의 홈개수랑 같으면 true를 반환한다.
