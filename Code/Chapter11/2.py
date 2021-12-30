

stringNumber = str(input())
ret = int(stringNumber[0])

length = len(stringNumber)
i = 1
while i < length:
    number = int(stringNumber[i])
    if number > 1 and ret > 1:
        ret *= number
    else:
        ret += number

    i += 1

print(ret)