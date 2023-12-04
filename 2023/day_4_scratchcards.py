# ----- Scratchcards -----

## Test
def fTest():
    tFile = open("day_4.txt", "r")

    matchOut = []
    cardPoints = []

    for idx, card in enumerate(tFile):

        headIdx = card.find(":")
        bodyIdx = card.find("|")

        wCards = card[headIdx+1:bodyIdx].split()
        mC = card[bodyIdx+1:].split()

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
                cardPoints.append(2**(match-1))
        print("match", match)
        match = 0
        print("matchOut", matchOut)
    return cardPoints




res = fTest()
print("res >>>>>> ", res)
print("res sum >> ", sum(res))
