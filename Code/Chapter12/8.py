def find(list, char):
    index = 0
    for otherChar in list:
        if otherChar >= char:
            break
        index += 1
    return index

string = input()
ret = list()
sum = 0

for char in string:
    if 'A' <= char <= 'Z':
        index = find(ret, char)
        ret.insert(index, char)
    else:
        sum += int(char)

print("".join(ret) + str(sum))


