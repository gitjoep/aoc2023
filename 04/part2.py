lines = open('input.txt', 'r').readlines()
lines = list(map(lambda n: n[:-1].split(': ')[1], lines))
lines = list(map(lambda n: n.split(" | "), lines))



def getNums(line):
    nums = []
    num = 0
    for i in line:
        if i.isnumeric():
            num = num * 10 + int(i)
        else:
            if num != 0:
                nums.append(num)
                num = 0
    if num != 0:
        nums.append(num)
    return nums

lines = list(map(lambda n: [getNums(n[0]), getNums(n[1])], lines))
hitList = []
result = 0

for i in lines:
    hits = 0
    for j in i[0]:
        if j in i[1]:
            hits += 1
    hitList.append(hits)

instanceList = []
for _ in range(len(hitList)):
    instanceList.append(1)

for i in range(len(hitList)):
    hits = hitList[i]
    instances = instanceList[i]

    for j in range(hits):
        if j+i+1 >= len(instanceList):
            continue
        instanceList[i+j+1] += instances
    
print(instanceList)
print(sum(instanceList))
