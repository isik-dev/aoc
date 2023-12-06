import time
# --- Day: 6 Wait for it ---


def questionOne():
    # file = open("day_6_test.txt", "r")
    file = open("day_6.txt", "r")

    data = {}
    out = []
    product = 1
    for line in file:
        c = line.find(":")
        head = line[:c]
        tail = line[c + 1 :]
        data[head.lower()] = [int(x) for x in tail.strip().split()]
    print("data", data)

    for raceIdx, total_duration in enumerate(data["time"]):
        ways_to_win = 0
        print("total_duration", total_duration)
        for hold_time in range(0, int(total_duration) + 1):
            print("hold_time", hold_time)
            dist = (total_duration - hold_time) * hold_time
            if dist > data["distance"][raceIdx]:
                # out.append({ "race": raceIdx, "hold_time": hold_time, "travel_distance": dist })
                ways_to_win += 1
        out.append(ways_to_win)
        product = product * ways_to_win
    print("out", out)
    print("product", product)


# questionOne()


def questionTwo():
    #file = open("day_6_test.txt", "r")
    file = open("day_6.txt", "r")

    start_time = time.time()

    data = {}
    out = 0
    for line in file:
        c = line.find(":")
        head = line[:c]
        tail = line[c + 1 :]
        data[head.lower()] = int(tail.replace(" ", "").strip())

    for hold_time in range(0, data["time"] + 1):
        #print("hold_time", hold_time)
        dist = (data["time"] - hold_time) * hold_time

        if dist > data["distance"]:
            out += 1

    print("--- %s seconds ---" % (time.time() - start_time))
    print("data", data)
    print("out", out)


questionTwo()
