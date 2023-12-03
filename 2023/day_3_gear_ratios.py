# ------ Gear Ratios ------
### Test
def isSym(inp):
    if inp != '.' and inp != None and not inp.isdigit():
        return True
    else:
        return False

def fTest():
    tFile = open("day_3_test.txt")
    out = []

    data = []
    for line in tFile:
        line = line.replace("\n", "")
        data.append(line)

    for ridx, line in enumerate(data):
        row = list(data[ridx])
        print("row", row)

        target = ''
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

                if not prev == '.' and not prev == None:
                    lSym = True

                if nxt.isdigit():
                    tEnd = idx+1
                else:
                    print('col >>>', col)
                    print('target >>>', target)
                    tEnd = idx
                    if nxt != '.' and nxt != None:
                        rSym = True
                    if ridx < len(data) - 1:
                        nxtRow = data[ridx + 1]
                        print('nxtRow', nxtRow)
                        print('nxtRow[idx + 1]', nxtRow[idx + 1])
                        if isSym(nxtRow[idx]) or isSym(nxtRow[tStart]) or isSym(nxtRow[idx + 1]):
                            print('yaaaaaaaaaaaaaaaay')
                            bSym = True
                        print('lSym', lSym)
                        print('rSym', rSym)
                        print('bSym', bSym)

                    if lSym or rSym or bSym:
                        print('target', target)
                        out.append(target)
                    target = ''
                    lSym = False
                    rSym = False
                    bSym = False
                    tStart = None
                    tEnd = None
    return out

        #if ridx < len(data) - 1:
        #    nxtRow = data[ridx + 1]
        #    print("nr >>>", nxtRow)


total = fTest()
print("total", total)
