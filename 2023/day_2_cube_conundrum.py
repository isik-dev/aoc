# Cube Conundrum

## Test
bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}
tFile = open("day_2.txt", "r")
def fTest():
    out = []
    for idx, game in enumerate(tFile):
        game = game.replace(" ", "")
        game = game.replace("\n", "")

        id = idx + 1

        head = game.find(':')
        body = game[head+1:]
        gameList = body.split(';')

        print('-- gameset --')
        gameObj = {"gameID": id, "passed": True}

        for gameSet in gameList:
            pairsList = gameSet.split(',')
            print(pairsList)
            for pair in pairsList:
                if "red" in pair:
                   clrIdx = pair.find("red")
                   qty = int(pair[:clrIdx])
                   if qty > bag["red"]:
                       print('qty', qty)
                       print(bag["red"])
                       gameObj["passed"] = False
                if "green" in pair:
                    clrIdx = pair.find("green")
                    qty = int(pair[:clrIdx])
                    if qty > bag["green"]:
                        gameObj["passed"] = False
                if "blue" in pair:
                    clrIdx = pair.find("blue")
                    qty = int(pair[:clrIdx])
                    if qty > bag["blue"]:
                        gameObj["passed"] = False
        if gameObj["passed"] == True:
            out.append(gameObj["gameID"])
        print("gameObj", gameObj)
    print("out", out)
    return out


#totalSum = sum(fTest())
#print("Sum of the IDs of possible games >", totalSum)

def questionTwo():
    out = []
    for game in tFile:
        gamePower = 0
        game = game.replace(" ", "")
        game = game.replace("\n", "")

        head = game.find(":")
        body = game[head+1:]
        gameList = body.split(";")

        #print('gameList >>', gameList)
        print('--- gameset ---')

        red = None
        blue = None
        green = None

        for gameSet in gameList:
            pairsList = gameSet.split(',')
            #print('pairsList', pairsList)

            for pair in pairsList:
                if "red" in pair:
                    idx = pair.find("red")
                    qty = int(pair[:idx])
                    if red == None or qty > red:
                        red = qty
                if "blue" in pair:
                    idx = pair.find("blue")
                    qty = int(pair[:idx])
                    if blue == None or qty > blue:
                        blue = qty
                if "green" in pair:
                    idx = pair.find("green")
                    qty = int(pair[:idx])
                    if green == None or qty > green:
                        green = qty
        print("red", red)
        print("green", green)
        print("blue", blue)
        print("set power is:", red * blue * green)
        gamePower += red*blue*green
        out.append(gamePower)
    return out




powerSum = sum(questionTwo())
print("This is the sum of the power of sets:", powerSum)
