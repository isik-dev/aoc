# ----- Scratchcards -----

## Test
def fTest():
    tFile = open("day_4.txt", "r")

    matchOut = []
    cardPoints = []

    for idx, card in enumerate(tFile):
        headIdx = card.find(":")
        bodyIdx = card.find("|")

        wCards = card[headIdx + 1 : bodyIdx].split()
        mC = card[bodyIdx + 1 :].split()

        myCards = set(mC)

        match = 0
        for c in wCards:
            if c in myCards:
                print("matched value:", c)
                match += 1
                matchOut.append(int(c))
        if match >= 1:
            if match == 1:
                cardPoints.append(1)
            else:
                cardPoints.append(2 ** (match - 1))
        print("match", match)
        match = 0
        print("matchOut", matchOut)
    return cardPoints


# res = fTest()
# print("res >>>>>> ", res)
# print("res sum >> ", sum(res))


def questionTwo():
    out = []
    details = {}

    # create starter dict
    mFile = open("day_4.txt", "r")
    for idx, card in enumerate(mFile):
        gameIdx = idx + 1

        details[gameIdx] = {"original": 1, "match": 0, "copies": 0}

    tFile = open("day_4.txt", "r")
    for idx, card in enumerate(tFile):
        gameIdx = idx + 1

        headIdx = card.find(":")
        bodyIdx = card.find("|")

        wC = card[headIdx + 1 : bodyIdx].split()
        mC = card[bodyIdx + 1 :].split()

        mC = set(mC)

        match = 0
        copies = 0

        for c in wC:
            if c in mC:
                match += 1
        details[gameIdx]["match"] = match

        for i, m in enumerate(range(match)):
            next = i + 1
            details[gameIdx + next]["copies"] += 1
            copies += 1
        print("gameIdx", gameIdx)

        print('details[gameIdx]["copies"]', details[gameIdx]["copies"])
        out.append(details[gameIdx]["copies"] + 1)

        for cidx, copy in enumerate(range(details[gameIdx]["copies"])):
            for mi, m in enumerate(range(match)):
                next = mi + 1
                details[gameIdx + next]["copies"] += 1

        print("details", details)

    return out


total = questionTwo()
print("This is the total sum", sum(total))
