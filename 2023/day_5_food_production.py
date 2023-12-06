# --- If you give a seed a fertilizer ---


def questionOne():
    # fTest = open("day_5_test.txt", "r")

    # # extract seeds and rest
    # seeds, *data_blocks = fTest.read().split("\n\n")

    # print("seeds", seeds)
    # print("data_blocks", data_blocks)
    with open("day_5.txt", "r") as file:
        data = file.read()
        seeds, *data_blocks = data.split("\n\n")
        # print("seeds", seeds)
    # print("data_blocks", data_blocks)

    seeds = list(map(int, seeds.split(":")[1].split()))

    for data_block in data_blocks:
        ranges_list = []
        for line in data_block.splitlines()[1:]:
            print("line", line)
            ranges_list.append(list(map(int, line.split())))
        print("ranges_list", ranges_list)

        ns = []

        for s in seeds:
            for destination, source, length in ranges_list:
                if s in range(source, source + length + 1):
                    ns.append(s - source + destination)
                    break
            else:
                ns.append(s)

        seeds = ns
        print("seeds", seeds)

    return seeds


# print("This is the min of seeds", min(questionOne()))


def questionTwo():
    # with open("day_5_test.txt", "r") as file:
    with open("day_5.txt", "r") as file:
        data = file.read()
        seeds, *data_blocks = data.split("\n\n")
        # print("seeds", seeds)
    # print("data_blocks", data_blocks)

    seed_inputs = list(map(int, seeds.split(":")[1].split()))
    seeds = []

    for i in range(0, len(seed_inputs), 2):
        seeds.append([seed_inputs[i], seed_inputs[i] + seed_inputs[i + 1]])

    print("seeds mid >> ", seeds)

    for data_block in data_blocks:
        ranges_list = []
        for line in data_block.splitlines()[1:]:
            ranges_list.append(list(map(int, line.split())))

        ns = []

        while len(seeds) > 0:
            start, end = seeds.pop()

            for destination, source, length in ranges_list:
                overlap_start = max(start, source)
                overlap_end = min(end, source + length)

                if overlap_start < overlap_end:
                    ns.append(
                        [
                            overlap_start - source + destination,
                            overlap_end - source + destination,
                        ]
                    )
                    if overlap_start > start:
                        seeds.append([start, overlap_start])
                    if overlap_end < end:
                        seeds.append([overlap_end, end])

                    break
            else:
                ns.append([start, end])

        seeds = ns
    # print("seeds >>>", seeds)
    return seeds


print(
    "Lowest location number that corresponds to any of the initial seed numbers:",
    min(questionTwo())[0],
)
