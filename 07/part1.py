lines = ""
with open("input.txt") as f:
    lines = f.readlines()

lines[len(lines) - 1] = lines[len(lines) - 1] + "\n"
lines = list(map(lambda n : n[:-1].split(" "), lines))
lines = list(map(lambda n: (n[0], int(n[1])), lines))

order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
def findType(hand):
    handDict = {}
    for i in hand:
        if i in handDict:
            handDict[i] += 1
        else:
            handDict[i] = 1
    typeDict = {}
    for i in handDict.values():
        if i in typeDict:
            typeDict[i] += 1
        else:        
            typeDict[i] = 1
    if 5 in typeDict:
        return 1
    if 4 in typeDict:
        return 2
    elif 3 in typeDict and 2 in typeDict:
        return 3
    elif 3 in typeDict:
        return 4
    elif 2 in typeDict and typeDict[2] == 2:
        return 5
    elif 2 in typeDict:
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
