import re
# --- Day 7: Camel Cards ---

#############################
# ------- Hand Types -------
# a: Five of a kind:  AAAAA - 5 same
# b: Four of a kind:  AA8AA - 4 same 1 diff
# c: Full house:      23332 - 3 same 2 same
# d: Three of a kind: TTT98 - 3 same 2 diff
# e: Two pair:        23432 - 2 same 2 same 1 diff
# f: One pair:        A23A4 - 2 same 3 diff
# g: High card:       23456 - 5 diff

# Rule 1: Hands are ordered by type, the order follows above

# Rule 2: If two hands have the same type, we compare first
# card in each hand. If these cards are different, the hand
# with stronger first card wins, else we move on to compare
# seconds card of each hand, and so on and so forth until
# fifth card.
#############################

strength = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "J": 3,
    "T": 4,
    "9": 5,
    "8": 6,
    "7": 7,
    "6": 8,
    "5": 9,
    "4": 10,
    "3": 11,
    "2": 12,
}


def questionOne():
    inp = []
    out = 0

    with open("day_7.txt", "r") as file:
        tFile = file.read()
        data = tFile.split("\n")[:-1]

    for pair in data:
        pair = pair.split()
        inp.append({"hand": pair[0], "bid": pair[1], "category": None, "rank": None})

    # Categorize them into Hand Types
    for k in inp:
        hand = list(k["hand"])
        # print("hand >>> ", hand)
        ctg = None

        uniques = {}
        for char in hand:
            if char not in uniques:
                uniques[char] = 1
            else:
                uniques[char] = uniques[char] + 1
        # print("uniques", uniques)
        if len(uniques) == 5:
            ctg = "g"
        elif len(uniques) == 4:
            ctg = "f"
        elif len(uniques) == 3:
            if max(uniques.values()) == 3:
                ctg = "d"
            else:
                ctg = "e"
        elif len(uniques) == 2:
            if max(uniques.values()) == 4:
                ctg = "b"
            else:
                ctg = "c"
        else:
            ctg = "a"
        k["category"] = ctg

    inp.sort(key=lambda x: x.get("category"))

    # Bubble Sort implementation
    n = len(inp)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # iterate over hand and compare strengths
            if inp[j]["category"] == inp[j + 1]["category"]:
                for idc, c in enumerate(inp[j]["hand"]):
                    if (
                        strength[inp[j]["hand"][idc]]
                        > strength[inp[j + 1]["hand"][idc]]
                    ):
                        inp[j], inp[j + 1] = inp[j + 1], inp[j]
                        swapped = True
                        print("<<<<<< swapped >>>>>>")
                    elif (
                        strength[inp[j]["hand"][idc]]
                        == strength[inp[j + 1]["hand"][idc]]
                    ):
                        continue
                    else:
                        break
                    if swapped:
                        break
    for i in range(n):
        inp[i]["rank"] = n - i
        out = out + int(inp[i]["rank"]) * int(inp[i]["bid"])
    print("bubble sorted inp", inp)
    return out


# res = questionOne()
# print("result", res)

new_strength = {
    "A": 0,
    "K": 1,
    "Q": 2,
    "T": 3,
    "9": 4,
    "8": 5,
    "7": 6,
    "6": 7,
    "5": 8,
    "4": 9,
    "3": 10,
    "2": 11,
    "J": 12,
}

#############################
# ------- Hand Types -------
# a: Five of a kind:  AAAAA - 5 same
# b: Four of a kind:  AA8AA - 4 same 1 diff
# c: Full house:      23332 - 3 same 2 same
# d: Three of a kind: TTT98 - 3 same 2 diff
# e: Two pair:        23432 - 2 same 2 same 1 diff
# f: One pair:        A23A4 - 2 same 3 diff
# g: High card:       23456 - 5 diff

# Updated Rule: J now acts like joker, wildcard that can act
# like whatever card would make the hand the strongest type
# possible.

# Now instead J is the weakest

# Rule 1: Hands are ordered by type, the order follows above

# Rule 2: If two hands have the same type, we compare first
# card in each hand. If these cards are different, the hand
# with stronger first card wins, else we move on to compare
# seconds card of each hand, and so on and so forth until
# fifth card.
#############################


def questionTwo():
    inp = []
    out = 0

    with open("day_7.txt", "r") as file:
        tFile = file.read()
        data = tFile.split("\n")[:-1]

    for pair in data:
        pair = pair.split()
        inp.append({"hand": pair[0], "bid": pair[1], "category": None, "rank": None})

    # Categorize them into Hand Types
    for k in inp:
        hand = list(k["hand"])
        # print("hand >>> ", hand)
        ctg = None

        uniques = {}
        for char in hand:
            if char not in uniques:
                uniques[char] = 1
            else:
                uniques[char] = uniques[char] + 1
        # print("uniques", uniques)
        if len(uniques) == 5:
            # AKT9J
            if "J" in uniques:
                ctg = "f"
            else:
                ctg = "g"
        elif len(uniques) == 4:
            # AKT99
            # AKJ99 -> AK999
            if "J" in uniques:
                ctg = "d"
            else:
                ctg = "f"
        elif len(uniques) == 3:
            # QQQK8 -> d
            # AAKKJ -> AAKKK -> c
            # AAAKJ -> AAAKA -> b
            # AAJKJ -> AAAKA -> b
            # JAJKJ -> AAAKA -> b
            if max(uniques.values()) == 3:
                if "J" in uniques:
                    ctg = "b"
                else:
                    ctg = "d"
            else:
                if "J" in uniques:
                    j_inst = [m.start() for m in re.finditer('J', k["hand"])]
                    if len(j_inst) > 1:
                        ctg = "b"
                    else:
                        ctg = "c"
                else:
                    ctg = "e"
        elif len(uniques) == 2:
            # AAAA1 -> b
            # AAAKK -> c
            # AAAKJ -> AAAKA -> b
            # AAAJJ -> AAAAA -> a
            if max(uniques.values()) == 4:
                if "J" in uniques:
                    ctg = "a"
                else:
                    ctg = "b"
            else:
                if "J" in uniques:
                    j_inst = [m.start() for m in re.finditer('J', k["hand"])]
                    if len(j_inst) > 1:
                        ctg = "a"
                    else:
                        ctg = "b"
                else:
                    ctg = "c"
        else:
            ctg = "a"
        k["category"] = ctg

    inp.sort(key=lambda x: x.get("category"))
    #print("inp", inp)

    # Bubble Sort implementation
    n = len(inp)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # iterate over hand and compare strengths
            if inp[j]["category"] == inp[j + 1]["category"]:
                for idc, c in enumerate(inp[j]["hand"]):
                    if (
                        new_strength[inp[j]["hand"][idc]]
                        > new_strength[inp[j + 1]["hand"][idc]]
                    ):
                        inp[j], inp[j + 1] = inp[j + 1], inp[j]
                        swapped = True
                        print("<<<<<< swapped >>>>>>")
                    elif (
                        new_strength[inp[j]["hand"][idc]]
                        == new_strength[inp[j + 1]["hand"][idc]]
                    ):
                        continue
                    else:
                        break
                    if swapped:
                        break
    for i in range(n):
        inp[i]["rank"] = n - i
        out = out + int(inp[i]["rank"]) * int(inp[i]["bid"])
    print(inp)
    return out


res = questionTwo()
print("result", res)
