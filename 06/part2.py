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
    time = 0
    for i in lines[0]:
        time *= 10**len(str(i))
        time += i 
    dist = 0
    for i in lines[1]:
        dist *= 10**len(str(i))
        dist += i

    minQuad = (-time + (time**2 - 4 * -1 * -dist)**0.5)/-2
    maxQuad = (-time - (time**2 - 4 * -1 * -dist)**0.5)/-2
    print(minQuad)
    print(maxQuad)
    print(int(maxQuad-minQuad))
    # combinations = 0
    # for j in range(time):
    #     if j * (time - j) > dist:
    #         print(j)
    #         combinations = time - j*2 + 1
    #         break
    # print(combinations)