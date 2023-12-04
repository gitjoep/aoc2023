lines = open('input.txt', 'r').readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]
for i in range(len(lines)):
    newline = []
    for j in range(len(lines[i])):
        newline.append((lines[i][j], 0))
    lines[i] = newline

lines[9].append(('.', 0))
gearCount = 1
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j][0] != '*':
            continue

        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if (i + a < 0) or (i + a >= len(lines)):
                    continue
                if (j + b < 0) or (j + b >= len(lines[i])):
                    continue
                lines[i+a][j+b] = (lines[i+a][j+b][0], gearCount)
        gearCount += 1

result = 0

gearMap = {}

for i in lines:
    num = 0
    gearNum = 0
    for j in i:
        if not j[0].isnumeric():
            if gearNum != 0:
                if gearNum in gearMap:
                    gearMap[gearNum].append(num)
                else:
                    gearMap[gearNum] = [num]
            num = 0
            gearNum = 0
            continue
        num = num * 10 + int(j[0])
        if j[1] != 0:
            gearNum = j[1]
    if gearNum != 0:
            if gearNum in gearMap:
                gearMap[gearNum].append(num)
            else:
                gearMap[gearNum] = [num]
result = 0
for i in gearMap.values():
    if len(i) == 2:
        result += i[0] * i[1]
print(result)

        

