import math
# --- Day 8: Haunted Wasteland ---


def questionOne():
    with open("day_8.txt", "r") as file:
        tFile = file.read()
        data = tFile.split("\n\n")
        directions = data[:1][0]
        nodes = data[1:][0].splitlines()
    ntw = {}

    for node in nodes:
        k = node[0:3]
        left = node[7:10]
        right = node[12:15]
        ntw[k] = {"L": left, "R": right}
    finished = False
    steps = 0
    drc = directions

    while not finished:
        nxt = None
        for idx, direction in enumerate(drc):
            if idx == 0:
                nxt = ntw["AAA"][direction]
            else:
                nxt = ntw[nxt][direction]
            steps += 1
            if nxt == "ZZZ":
                finished = True
                break
            if idx == len(drc) - 1 and not finished:
                steps = 0
                drc += directions
        print("steps", steps)


# questionOne()


def questionTwo():
    with open("day_8.txt", "r") as file:
        tFile = file.read()
        data = tFile.split("\n\n")
        directions = data[:1][0]
        nodes = data[1:][0].splitlines()
    print("directions", directions)
    ntw = {}

    ending_a = []

    for node in nodes:
        k = node[0:3]
        left = node[7:10]
        right = node[12:15]
        ntw[k] = {"L": left, "R": right}

        if k[-1] == "A":
            ending_a.append(k)

    print("ending_a", ending_a)
    # test case
    # path_1 = ending_a[0]
    # path_2 = ending_a[1]

    path_1 = ending_a[0]
    path_2 = ending_a[1]
    path_3 = ending_a[2]
    path_4 = ending_a[3]
    path_5 = ending_a[4]
    path_6 = ending_a[5]

    finished = False
    steps = 0
    drc = directions
    restart = False

    nxt_1 = None
    nxt_2 = None
    nxt_3 = None
    nxt_4 = None
    nxt_5 = None
    nxt_6 = None

    while not finished:
        for idx, direction in enumerate(drc):
            if idx == 0 and restart == False:
                nxt_1 = ntw[path_1][direction]
                nxt_2 = ntw[path_2][direction]
                nxt_3 = ntw[path_3][direction]
                nxt_4 = ntw[path_4][direction]
                nxt_5 = ntw[path_5][direction]
                nxt_6 = ntw[path_6][direction]
            else:
                nxt_1 = ntw[nxt_1][direction]
                nxt_2 = ntw[nxt_2][direction]
                nxt_3 = ntw[nxt_3][direction]
                nxt_4 = ntw[nxt_4][direction]
                nxt_5 = ntw[nxt_5][direction]
                nxt_6 = ntw[nxt_6][direction]
            steps += 1

            if idx == len(drc) - 1:
                if (
                    nxt_1[-1] == "Z"
                    and nxt_2[-1] == "Z"
                    and nxt_3[-1] == "Z"
                    and nxt_4[-1] == "Z"
                    and nxt_5[-1] == "Z"
                    and nxt_6[-1] == "Z"
                ):
                    finished = True
                    break
                else:
                    drc += directions
                    restart = True

    print("steps", steps)


# questionTwo()

with open("day_8.txt") as file:
    tFile = file.read().strip()
    data = tFile.split("\n\n")
    directions = list(data[0])
    ntw = {}


def questionTwoLCM():
    for k in data[1].split("\n"):
        key = k.split(" ")[0]
        left = k.split("(")[1].split(",")[0]
        right = k.split(" ")[3].split(")")[0]

        ntw[key] = (left, right)

    steps = 1
    for node in ntw:
        if node[-1] == "A":
            #        print("prev steps", steps)
            steps = math.lcm(steps, getStepsPerPath(node))
    #        print("node", node)
    print(steps)


def getStepsPerPath(node):
    next_node = node
    idx = 0
    while not next_node[-1] == "Z":
        d = directions[idx % len(directions)]
        next_node = ntw[next_node][0 if d == "L" else 1]
        idx += 1
    return idx


questionTwoLCM()
