''' 문제
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
a. X가 5로 나누어 떨어지면, 5로 나눈다.
b. X가 3으로 나누어떨어지면, 3으로 나눈다.
c. X가 2로 나누어떨어지면, 2로 나눈다.
d. X에서 1을 뺀다.

정수 X가 주여졌을 떄, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
'''

'''
#종료조건
1.연산횟수가 크거나 같을 때 종료
2.정수가 1일 때 -> 연산횟수 기록
#실행문
1. X가 5로 나누어 떨어지면 5로 나눔(재귀, 연산횟수 + 1)
2. X가 3으로 나누어 떨어지면 3으로 나눔(재귀, 연산횟수 + 1)
3. X가 2로 나누어 떨어지면 2로 나눔(재귀, 연산횟수 + 1)
4. X에서 1을 뺌(재귀, 연산횟수 + 1)

'''
ret = 30000

def recursive(number, count):
    global ret
    if count >= ret:
        return

    if number == 1:
        ret = count
        return

    if number % 5 == 0:
        recursive(number // 5, count + 1)
    if number % 3 == 0:
        recursive(number // 3, count + 1)
    if number % 2 == 0:
        recursive(number // 2, count + 1)
    recursive(number - 1, count + 1)

def solution(number):
    global ret
    ret = 30000
    recursive(number, 0)

    return ret

def bookSolution(number): # 책에 있는 정답
    d = [0] * 30001

    for i in range(2, number + 1):
        # 현재의 수에서 1을 빼는 경우
        d[i] = d[i - 1] + 1
        # 현재의 수가 2로 나누어 떨어지는 경우
        if i % 2 == 0:
            d[i] = min(d[i], d[i // 2] + 1)
        #현재의 수가 3으로 나누어 떨어지는 경우
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        #현재의 수가 5로 나누어 떨어지는 경우
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)

    return d[number]

print(solution(1))
print(solution(4000))
print(bookSolution(4000))