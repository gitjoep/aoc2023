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

result = 0
for i in lines:
    hits = 0
    for j in i[0]:
        if j in i[1]:
            hits += 1
    if hits > 0:
        result += 2**(hits-1)

print(result)
