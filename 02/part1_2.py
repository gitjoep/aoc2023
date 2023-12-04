lines = open('input.txt', 'r').readlines()

lines = list(map(lambda n: n[:-1].split(": ")[1].split("; "), lines))
lines = list(map(lambda n: list(map(lambda b: b.split(", "), n)), lines))
lines = list(map(lambda n: sum(n, []), lines))
lines = list(map(lambda n: list(map(lambda b: b.split(" "), n)), lines))
print(lines[0])
result1 = 0

for i in range(len(lines)):
    valid = True
    for j in lines[i]:    
        num = int(j[0])
        col = j[1]
        if col =="red" and num > 12 or col == "green" and num > 13 or col == "blue" and num > 14:
            valid = False
            break
    
    if valid:
        result1 += (i+1)
print(result1)

result2 = 0
for i in range(len(lines)):
    minblue = 0
    minred = 0
    mingreen = 0
    
    for j in lines[i]:
        num = int(j[0])
        col = j[1]
        if col == "blue" and num > minblue:
            minblue = num
        if col == "red" and num > minred:
            minred = num
        if col == "green" and num > mingreen:
            mingreen = num

    result2 += mingreen * minblue * minred

print(result2)