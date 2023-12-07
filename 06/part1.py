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

with open('input.txt') as f:
    lines = f.readlines()
    lines = list(map(lambda n: n.split(":")[1], lines))
    lines = list(map(lambda n: getNums(n), lines))
    
    result = 1
    for i in range(len(lines[0])):
        combinations = 0
        for j in range(lines[0][i]+1):
            if j * (lines[0][i] - j) > lines[1][i]:
                print(f"{j}, {lines[0][i] - j}")
                combinations += 1
        print(combinations)
        result *= combinations
    print(result)
            