lines = ""
with open("input.txt") as f:
    lines = f.readlines()

lines[len(lines) - 1] = lines[len(lines) - 1] + "\n"
lines = list(map(lambda n : n[:-1].split(" "), lines))
lines = list(map(lambda n: (n[0], int(n[1])), lines))

order = ['A', 'K', 'Q','T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def findType(hand):
    handDict = {}
    jCount = 0
    for i in hand:
        if i == "J":
            jCount += 1
        else:
            handDict[i] = handDict.get(i, 0) + 1
    typeDict = [0] * 6
    for i in handDict.values():
        typeDict[i] += 1
    
    if jCount > 0:
        if typeDict[4] == 1:
            typeDict[4 + jCount] += 1
            typeDict[4] = typeDict[4] - 1
        elif typeDict[3] == 1:
            typeDict[3 + jCount] += 1
            typeDict[3] = typeDict[3] - 1
        elif typeDict[2] >= 1:
            typeDict[2 + jCount] += 1
            typeDict[2] = typeDict[2] - 1
        elif typeDict[1] >= 1:
            typeDict[1 + jCount] += 1
            typeDict[1] = typeDict[1] - 1
        else:
            typeDict[5] = 1
    
    if typeDict[5] >= 1:
        return 1
    elif typeDict[4] >= 1:
        return 2
    elif typeDict[3] >= 1 and typeDict[2] >= 1:
        return 3
    elif typeDict[3] >= 1:
        return 4
    elif typeDict[2] >= 2:
        return 5
    elif typeDict[2] >= 1:
        return 6
    return 7

def compare(hand1, hand2):
    if hand1[1] < hand2[1]:
        return True
    elif hand1[1] > hand2[1]:
        return False
    for hand1Char, hand2Char in zip(hand1[0], hand2[0]):
        if order.index(hand1Char) < order.index(hand2Char):
            return True
        elif order.index(hand1Char) > order.index(hand2Char):
            return False
    return False
    
lines = list(map(lambda n: ((n[0], findType(n[0]), n[1])), lines))
sortedHands = [lines[0]]
for i in lines[1:]:
    for j in range(len(sortedHands)):
        if compare(i, sortedHands[j]):
            if j == len(sortedHands) - 1:
                sortedHands.append(i)
            continue
        else:
            sortedHands.insert(j, i)
            break
print(sortedHands)
result = 0
for i in range(len(sortedHands)):
    result += (i+1) * sortedHands[i][2]
print(result)
