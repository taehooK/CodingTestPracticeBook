from collections import deque
from itertools import combinations
import sys

rowOffset = [-1, 1, 0 ,0]
columnOffset = [0, 0, -1, 1]
#감시를 피할 수 있는상황이면 True, 그렇지않으면 False를 반환하는 함수
def check(area, teachers_position):
    for position in teachers_position:
        for i in range(4):
            row = position[0] + rowOffset[i]
            column = position[1] + columnOffset[i]
            while 0 <= row < len(area) and 0 <= column < len(area):
                if area[row][column] == 'O':
                    break
                elif area[row][column] == 'S':
                    return False
                row += rowOffset[i]
                column += columnOffset[i]
    return True

def get_value_position(area, value):
    queue = deque()
    for i in range(len(area)):
        for j in range(len(area)):
            if area[i][j] == value:
                queue.append((i, j))
    return queue

def solution(area):
    teacher_position = list(get_value_position(area, 'T'))
    blank_position = get_value_position(area, 'X')
    blank_position = combinations(blank_position, 3)

    for positions in blank_position:
        for position in positions:
            area[position[0]][position[1]] = 'O'
        if check(area, teacher_position):
            return True
        for position in positions:
            area[position[0]][position[1]] = 'X'

    return False
def get_input():
    n = int(input())
    area = []
    for i in range(n):
        area.append(list(map(str, sys.stdin.readline().rstrip().split())))
    return area

if __name__ == '__main__':
    area = get_input()
    if solution(area):
        print('YES')
    else:
        print('NO')
