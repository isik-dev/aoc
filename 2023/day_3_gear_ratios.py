# ------ Gear Ratios ------
import math as m, re


### Test
def isSym(inp):
    if inp != "." and inp != None and not inp.isdigit():
        return True
    else:
        return False


def fTest():
    tFile = open("day_3_test.txt")
    out = []

    data = []
    for line in tFile:
        print("tFile >", line)
        line = line.replace("\n", "")
        data.append(line)

    for ridx, line in enumerate(data):
        pRow = None
        nRow = None
        if ridx > 0:
            pRow = list(data[ridx - 1])
        if ridx < len(data) - 1:
            nRow = list(data[ridx + 1])
        row = list(data[ridx])
        print("curr row", row)

        target = ""
        tStart = None
        tEnd = None

        lSym = False
        rSym = False
        tSym = False
        bSym = False

        for idx, col in enumerate(row):
            if col.isdigit():
                prev = row[(tStart or 0) - 1]
                nxt = row[(tEnd or 0) + 1]

                target += col
                if tStart is None:
                    tStart = idx

                if not prev == "." and not prev == None:
                    lSym = True

                if nxt.isdigit():
                    tEnd = idx + 1
                else:
                    if idx < len(row) - 1:
                        tEnd = idx + 1
                    else:
                        tEnd = idx
                    if nxt != "." and nxt != None:
                        rSym = True
                print("tStart", tStart)
                print("tEnd", tEnd)
                # Check above and below rows
                if tStart != None and tEnd != None:
                    if pRow != None:
                        for pVal in range(tStart - 1, tEnd + 1):
                            print("pVal", pVal)
                            if isSym(pRow[pVal]):
                                tSym = True
                    if nRow != None:
                        for pVal in range(tStart - 1, tEnd + 1):
                            if isSym(nRow[pVal]):
                                bSym = True
            else:
                if lSym or rSym or tSym or bSym:
                    print("target", target)
                    out.append(target)
                target = ""
                lSym = False
                rSym = False
                tSym = False
                bSym = False
                tStart = None
                tEnd = None

                # if ridx < len(data) - 1:
                #     nxtRow = data[ridx + 1]
                #     print('nxtRow', nxtRow)
                #     print('nxtRow[idx + 1]', nxtRow[idx + 1])
                #     if isSym(nxtRow[idx]) or isSym(nxtRow[tStart]) or isSym(nxtRow[idx + 1]):
                #         print('yaaaaaaaaaaaaaaaay')
                #         bSym = True
                #     print('lSym', lSym)
                #     print('rSym', rSym)
                #     print('bSym', bSym)

                # if lSym or rSym or bSym:
                #     print('target', target)
                #     out.append(target)
                # target = ''
                # lSym = False
                # rSym = False
                # bSym = False
                # tStart = None
                # tEnd = None
    return out

    # if ridx < len(data) - 1:
    #    nxtRow = data[ridx + 1]
    #    print("nr >>>", nxtRow)


# total = fTest()


def question():
    board = list(open("day_3.txt"))

    chars = {
        (r, c): []
        for r in range(140)
        for c in range(140)
        if board[r][c] not in "01234566789."
    }

    for r, row in enumerate(board):
        for n in re.finditer(r"\d+", row):
            edge = {
                (r, c)
                for r in (r - 1, r, r + 1)
                for c in range(n.start() - 1, n.end() + 1)
            }

            for o in edge & chars.keys():
                chars[o].append(int(n.group()))

    print(
        sum(sum(p) for p in chars.values()),
        sum(m.prod(p) for p in chars.values() if len(p) == 2),
    )


question()
