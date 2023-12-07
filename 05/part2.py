def copyList(listToCopy):
    copied = []
    for i in listToCopy:
        copied.append(i)
    return copied

with open('input.txt') as f:
    lines = f.readlines()
    seeds = list(map(lambda n: int(n), lines[0][7:].split(" ")))
    seeds = [(seeds[x*2], seeds[x*2+1]) for x in range(len(seeds)//2)]
    seedMaps = []
    curMap = []


    for i in lines[3:]:
        if i[0].isalpha() or i[0] == "\n":
            if curMap != []:
                seedMaps.append(curMap)
                curMap = []
        else:
            curMap.append(list(map(lambda n: int(n), i.split(" "))))
    seedMaps.append(curMap)
    for seedMap in seedMaps:
        converted = []
        for mapping in seedMap:
            toAdd = []
            for i in range(len(seeds)):
                seed = seeds[i]
                if i in converted:
                    continue
                if (seed[0] >= mapping[1] and seed[0] + seed[1] <= mapping[1] + mapping[2]):
                    converted.append(i)
                    seeds[i] = (seed[0] + (mapping[0] - mapping[1]), seeds[i][1])
                elif (seed[0] < mapping[1] and seed[0] + seed[1] > mapping[1] + mapping[2]):
                    converted.append(i)
                    seeds[i] = (mapping[0], mapping[2])
                    toAdd.append((seed[0], mapping[1] - seed[0]))
                    toAdd.append((mapping[1] + mapping[2], seed[1] - (mapping[1] + mapping[2])))
                elif (seed[0] < mapping[1] and seed[0] + seed[1] >= mapping[1] and seed[0] + seed[1] <= mapping[1] + mapping[2]):
                    converted.append(i)
                    seeds[i] = (mapping[0], seeds[i][1] + (seeds[i][0] - mapping[1]))
                    toAdd.append((seed[0], mapping[1] - seed[0]))
                elif (seed[0] > mapping[1] and seed[0] < mapping[1] + mapping[2] and seed[0] + seed[1] > mapping[1] + mapping[2]):
                    converted.append(i)
                    seeds[i] = (seed[0] + (mapping[0] - mapping[1]), (mapping[1] + mapping[2]) - seed[0])
                    toAdd.append((mapping[1]+mapping[2], seed[1] + (seed[0] - (mapping[1] + mapping[2]))))

            for i in toAdd:
                seeds.append(i)
    print(seeds)
    seeds = list(map(lambda n: n[0], seeds))
    print(min(seeds))

