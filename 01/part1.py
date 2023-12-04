def getNum(line):
    firstNum = -1
    secondNum = -1

    for i in line:
        if (str.isnumeric(i)):
            if firstNum == -1:
                firstNum = int(i)
            secondNum = int(i)
    return firstNum * 10 + secondNum

with open('input.txt') as f:
    lines = f.readlines()
    print(sum(list(map(lambda n: getNum(n), lines))))




