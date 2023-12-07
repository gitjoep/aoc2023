with open('input.txt') as f:
    lines = f.readlines()
    seeds = list(map(lambda n: int(n), lines[0][7:].split(" ")))
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
    # for i in seedMaps:
    #     print(i)
    for map in seedMaps:

        converted = []
        for mapping in map:
            
            for seed in range(len(seeds)):
                if seed in converted:
                    continue
                if seeds[seed] >= mapping[1] and seeds[seed] < (mapping[1] + mapping[2]):
                    seeds[seed] = seeds[seed] + (mapping[0] - mapping[1])
                    converted.append(seed)
    print(min(seeds))

