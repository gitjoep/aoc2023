def getNum(line):
    firstNum = -1
    secondNum = -1

    for i in line:
        if (str.isnumeric(i)):
            if firstNum == -1:
                firstNum = int(i)
            secondNum = int(i)
    return firstNum * 10 + secondNum

with open('input2.txt') as f:
    lines = f.readlines()
    lines = list(map(lambda n: n.replace("one", "one1one"), lines))
    lines = list(map(lambda n: n.replace("two", "two2two"), lines))
    lines = list(map(lambda n: n.replace("three", "three3three"), lines))
    lines = list(map(lambda n: n.replace("four", "four4four"), lines))
    lines = list(map(lambda n: n.replace("five", "five5five"), lines))
    lines = list(map(lambda n: n.replace("six", "six6six"), lines))
    lines = list(map(lambda n: n.replace("seven", "seven7seven"), lines))
    lines = list(map(lambda n: n.replace("eight", "eight8eight"), lines))
    lines = list(map(lambda n: n.replace("nine", "nine9nine"), lines))
    print(lines)
    print(list(map(lambda n: getNum(n), lines)))
    print(sum(list(map(lambda n: getNum(n), lines))))


