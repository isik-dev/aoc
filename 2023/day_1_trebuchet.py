# --------- Trebuchet --------
### Warmup
# data = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


# def warmup():
#     calibrationValues = []
#     for txt in data:
#         fD = None
#         lD = None
#         for char in txt:
#             if char.isdigit() and fD is None:
#                 fD = char
#                 break
#         for char in reversed(txt):
#             if char.isdigit() and lD is None:
#                 lD = char
#                 break
#         calibrationValues.append(int(fD + lD))
#         fD = None
#         lD = None
#     # print(calibrationValues)
#     return sum(calibrationValues)


### Question 1:
# input = open("day_1.txt", "r")


# def questionOne():
#     decipheredList = []

#     fDig = None
#     lDig = None
#     for line in input:
#         for char in line:
#             if char.isdigit() and fDig is None:
#                 fDig = char
#                 break

#         for char in reversed(line):
#             if char.isdigit() and lDig is None:
#                 lDig = char
#                 break
#         decipheredList.append(int(fDig + lDig))
#         fDig = None
#         lDig = None
#     # print(decipheredList)
#     return sum(decipheredList)


# print("Answer for question #1:", questionOne())

input = open("day_1.txt", "r")
testFile = open("day_1_test.txt", "r")
mixed = ["sevenine", "txb3qfzsbzbxlzslfourone1vqxgfive"]
nL = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
mappedNL = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

def questionTwo():
    out = []
    fdig = ''
    ldig = ''
    fidx = None
    lidx = None

    for char in input:
        print('current char', char)
        for nm in nL:
            res = char.find(nm)
            if res == -1:
                continue
            if fidx == None or res < fidx:
                fidx = res
                fdig = nm
            if lidx == None or res > lidx:
                lidx = res
                ldig = nm

        print('1 fdig', fdig)
        print('1 ldig', ldig)
        # we are fished with numbers list
        if not fdig.isdigit():
            fdig = mappedNL[fdig]
        if not ldig.isdigit():
            ldig = mappedNL[ldig]
        out.append(int(fdig + ldig))
        print('fdig >> ', fdig)
        fdig = ''
        ldig = ''
        fidx = None
        lidx = None
    print('out', out)
    return sum(out)

sumOfCalVals = questionTwo()
print("This is the sum of all of the calibration values:", sumOfCalVals)



import re
n = "one two three four five six seven eight nine".split()
p = "(?=(" + "|".join(n) + "|\\d))"
def f(x):
    if x in n:
        return str(n.index(x) + 1)
    return x


def questionTwoV2():

    t = 0
    for x in input:
        digits = [*map(f, re.findall(p, x))]
        t += int(digits[0] + digits[-1])
    return t
#print(questionTwoV2())

#def questionTwo():
#    out = []
#    fDig = None
#    lDig = None
#
#    for line in mixed:
#        print("current line", line)
#        for char in line:
#            print("current char", char)
#            if char.isdigit():
#                # print("found first digit", char)
#                if fDig is None:
#                    fDig = char
#                    break
#            else:
#                ltrNum = ""
#                for nmbr in nL:
#                    print("nmbr", nmbr)
#                    for nmbrChar in nmbr:
#                        print("nmbrChar", nmbrChar)
#                        if char == nmbrChar:
#                            ltrNum += char
#                        else:
#                            break
#                    if ltrNum == nmbr and fDig is None:
#                        fDig = mappedNL[ltrNum]
#                    ltrNum = ""
#            print("created ltrNum", ltrNum)
#        for char in reversed(mixed):
#            if char.isdigit():
#                if lDig is None:
#                    lDig = char
#                    break
#            else:
#                ltrNum = ""
#                for nmbr in nL:
#                    for nmbrChar in reversed(nmbr):
#                        if char == nmbrChar:
#                            ltrNum = char + ltrNum
#                        else:
#                            break
#                    if ltrNum == nmbr and lDig is None:
#                        lDig = mappedNL[ltrNum]
#                        ltrNum = ""
#            print("second created ltrNum", ltrNum)
#        out.append(int(fDig + lDig))
#    print("output for 2 >>> ", out)
#
#
## questionTwo()
## print("Answer for question #2:", questionTwo())
