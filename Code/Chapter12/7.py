number = int(input())

count = 0
temp = number
while temp > 0:
    count += 1
    temp //= 10

count = count / 2
temp = number
backPart = 0
i = 1
while i <= count:
    backPart += temp % 10
    temp //= 10
    i += 1

frontPart = 0
i = 1
while i <= count:
    frontPart += temp % 10
    temp //= 10
    i += 1

if backPart == frontPart:
    print("LUCKY")
else:
    print("READY")