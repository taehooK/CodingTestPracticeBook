
string = input()
length = len(string)
previousChar = int(string[0])
zeroGroupCount = 0
oneGroupCount = 0
i = 1
while i < length:
    currentChar = int(string[i])
    if previousChar != currentChar:
        if previousChar == 0:
            zeroGroupCount += 1
        else:
            oneGroupCount += 1
    previousChar = currentChar
    i += 1

if previousChar == 0:
    zeroGroupCount += 1
else:
    oneGroupCount += 1

ret = oneGroupCount
if zeroGroupCount < oneGroupCount:
    ret = zeroGroupCount

print(ret)