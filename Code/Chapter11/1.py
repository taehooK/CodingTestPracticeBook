


count = int(input())#1. 모함가의 수를 입력받는다.
numbersOfFear = list(map(int, input().split()))#2. 모험가들의 공포도를 입력받는다.
numbersOfFear.sort();#3. 공포도들을 오름차순 정렬한다.

countOfGroup = 0
countInGroup = 0
i = 0

while i < count: #4. 모험가의 수만큼 반복한다.
    maxFear = numbersOfFear[i]#4.1. 최대 공포도를 갱신한다.
    countInGroup += 1#4.2. 그룹내 인원을 센다.
    if countInGroup >= maxFear: #4.3. 그룹내 인원이 최대 공포도보다 크거나 같으면
        countOfGroup += 1#4.3.1. 그룹 수를 센다.
        countInGroup = 0#4.3.2. 그룹내 인원을 초기화한다.
    i += 1

print(countOfGroup)
