lines = open('input.txt', 'r').readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]
for i in range(len(lines)):
    newline = []
    for j in range(len(lines[i])):
        newline.append((lines[i][j], 0))
    lines[i] = newline

nonSymbols = ['.', '0','1', '2', '3', '4', '5', '6', '7', '8', '9']
print(len(lines))
lines[9].append(('.', 0))

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j][0] in nonSymbols:
            continue
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                if (i + a < 0) or (i + a >= len(lines)):
                    continue
                if (j + b < 0) or (j + b >= len(lines[i])):
                    continue
                lines[i+a][j+b] = (lines[i+a][j+b][0], 1)

for i in lines:
    print(i)
result = 0
for i in lines:
    num = 0
    valid = False
    for j in i:
        if not j[0].isnumeric():
            if valid:
                result += num
            num = 0
            valid = False
            continue
        num = num * 10 + int(j[0])
        if j[1] == 1:
            valid = True
    if valid:
        result += num
print(result)
        

