def rotateDirection(currentDirection, roatetDirection):
    newDirection = currentDirection
    if roatetDirection == 'D':
        newDirection += 1
    elif roatetDirection == 'L':
        newDirection -= 1
    if newDirection <= 0:
        newDirection = 4
    elif newDirection > 4:
        newDirection = 1
    return newDirection

def getNextCoordinate(currentRow, currentColumn, direction):
    nextRow = currentRow
    nextColumn = currentColumn
    if direction == 1:
        nextColumn += 1
    elif direction == 2:
        nextRow += 1 
    elif direction == 3:
        nextColumn -= 1
    elif direction == 4:
        nextRow -= 1

    return (nextRow, nextColumn)

def move(board, destRow, destColumn, snakeCoordinates):
    length = len(snakeCoordinates)
    tailCoordinate = snakeCoordinates[length - 1]
    board[tailCoordinate[0]][tailCoordinate[1]] = 0
    board[destRow][destColumn] = 1

    del snakeCoordinates[length - 1]
    snakeCoordinates.insert(0, (destRow, destColumn))

def snakeGame():
    #보드 크기 입력받기
    N = int(input())
    #보드 만들기
    board = [[0] * N for y in range(N)]
    board[0][0] = 1

    length = len(board)
    #사과의 개수 입력받기
    appleCount = int(input())
    #사과의 개수만큼 사과의 행, 열을 입력받는다.
    for i in range(appleCount):
        row, column = map(int, input().split())
        board[row - 1][column - 1] = -1

    trigger = dict()
    #뱀의 방향 변환 횟수를 입력받는다.
    conversionCount = int(input())
    #방향 변환 횟수만큼 시간과 방향을 입력받는다.
    for i in range(conversionCount):
        time, direction = input().split()
        time = int(time)
        trigger[time] = direction

    currentDirection = 1
    retTime = 0
    snakeCoordinates = list()
    snakeCoordinates.append((0, 0))

    gameOver = False
    while not gameOver:
        if retTime in trigger:
            currentDirection = rotateDirection(currentDirection, trigger.get(retTime))

        headCoordinate = snakeCoordinates[0]
        nextCoordinate = getNextCoordinate(headCoordinate[0], headCoordinate[1], currentDirection)

        if nextCoordinate[0] < 0 or nextCoordinate[0] >= length or nextCoordinate[1] < 0 or nextCoordinate[1] >= length: #벽에 부딪힐 때
            gameOver = True
        elif board[nextCoordinate[0]][nextCoordinate[1]] > 0: # 몸통
            gameOver = True
        elif board[nextCoordinate[0]][nextCoordinate[1]] == -1:
            board[nextCoordinate[0]][nextCoordinate[1]] = 1
            snakeCoordinates.insert(0, (nextCoordinate[0], nextCoordinate[1]))
        else:
            move(board, nextCoordinate[0], nextCoordinate[1], snakeCoordinates)

        retTime += 1

    return retTime

print(snakeGame())

#1. 보드판을 채운다.
#2. 게임이 끝날 때까지 반복한다.
 #2.1. 초를 센다.
 #2.2. 트리거가 있으면 방향을 바꾼다.
 #2.3. 이동한다.
#2.3.1. 이동할 자리에 사과가 있으면
 #2.3.1.1. 이동할 자리를 머리로 정한다.
 #2.3.1.2. 길이를 늘린다.
  #2.3.2. 이동할 자리에 장애물이 있으면
 #2.3.2.1. 게임을 종료한다.
#2.3.3. 이동할 자리에 아무것도 없으면
 #2.3.3.1. 한 칸 이동한다.
#3. 초를 반환한다.


