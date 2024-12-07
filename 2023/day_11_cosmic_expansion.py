# --- Day 11: Cosmic Expansion ---
def partOne():
    with open("day_11_test.txt", "r") as txtFile:
        txtReader = txtFile.read()

    ###############################
    # 1. Create 2d Array
    # 2. 2x rows & columns that have no galaxies, i.e. "#"
    # 3. Replace "#" with digits
    ###############################

    # 1.
    twoD = []
    tempRow = []
    for row in txtReader:
        if row == "\n":
            twoD.append(tempRow)
            tempRow = []
        else:
            tempRow.append(row)

    # 2.1
    # Loop through rows and check for galaxy empty rows
    # Append right after the found idx
    noGalIdx = []
    noGalRow = None
    for idx, row in enumerate(twoD):
        if "#" not in row:
            noGalIdx.append(idx+1)
            noGalRow = row

    for i in noGalIdx:
        twoD.insert(i, noGalRow)

    # 2.2
    # Loop through each item of the first row in 2d array
    # Loop through each column and check if
    # there is a galaxy
    # if yes, break
    # if no, save idx of that column
    noGalColIdx = []
    for idx, col in enumerate(twoD[0]):
        hasGal = False
        for row in twoD:
            if row[idx] == '#':
                hasGal = True

        if not hasGal:
            noGalColIdx.append(idx+1)
    print(noGalColIdx)
    # 2.3 insert new col next to empty col
    for i in noGalColIdx:
        for row in twoD:
            row.insert(i, '.')

    # 3.
    dig = 1
    for rIdx, row in enumerate(twoD):
        for cIdx, col in enumerate(row):
            if col == "#":
                print("col", col)
                twoD[rIdx][cIdx] = dig
                dig +=1

    print(twoD)

partOne()

sample = [['.', '.', '1'], ['.', '2', '3'], ['.', '.', '.']]

def pairFinder(n):
    out = []
    k = None
    v = None
    for r in n:
        for c in r:
            if c.isdigit():
                if k is None:
                    k = c
                else:
                    v = c
            if k is not None and v is not None:
                out.append({ k:v })
                k = None
                v = None
    return out

print(pairFinder(sample))

