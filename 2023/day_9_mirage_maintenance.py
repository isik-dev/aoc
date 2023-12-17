# --- Day 9: Mirage Maintenance ---

def questionOne():
    with open("day_9_test.txt", "r") as file:
        tFile = file.read()
        data = tFile.strip().split("\n\n")[0].splitlines()
    report = []
    for i in data:
        report.append([int(n) for n in i.split(" ")])

    print(report)

    sum_of_extrapolated_values = 0
    # loop 2d array
    for child_arr in report:
        # loop child array
        curr_arr = child_arr 
        updated = []
        last = []
        diff = []
        
        complete = False

        print("curr_arr", curr_arr)
        while not complete:
            for i in range(0, len(curr_arr) - 1):
                diff.append(curr_arr[i+1] - curr_arr[i])

            print("diff", diff)
            if len(diff) != 0 and all(el == 0 for el in diff):
                print("<<<<<< all zero >>>>>>")
                last.append(0)
                total = 0
                print("last", last)
                for i in range(len(last) - 1, 0, -1):
                    print(last[i], last[i-1])
                    total = total + last[i-1]
                    updated.append(total)
                complete = True
                break
            else:
                last.append(diff[-1])
                #decrement += 1
                curr_arr = diff
                diff = []
        updated.append(child_arr[0] - updated[-1])
        print("child_arr[0]", child_arr[0])
        print("updated[-1]", updated[-1])
        print("updated", updated)
        sum_of_extrapolated_values += updated[-1]
    print(sum_of_extrapolated_values)
    return sum_of_extrapolated_values

#questionOne()



def questionTwo():
    with open("day_9.txt", "r") as file:
        tFile = file.read()
        data = tFile.strip().split("\n\n")[0].splitlines()
    report = []
    for i in data:
        report.append([int(n) for n in i.split(" ")])

    print(report)

    sum_of_extrapolated_values = 0
    # loop 2d array
    for child_arr in report:
        # loop child array
        curr_arr = child_arr 
        updated = []
        last = []
        diff = []
        
        complete = False

        print("curr_arr", curr_arr)
        while not complete:
            for i in range(len(curr_arr) - 1, 0, - 1):
                diff.append(curr_arr[i] - curr_arr[i-1])

            print("diff", diff)
            if len(diff) != 0 and all(el == 0 for el in diff):
                print("<<<<<< all zero >>>>>>")
                last.append(0)
                total = 0
                print("last", last)
                for i in range(len(last) - 1, -1, -1):
                    print(last[i], last[i-1])
                    total = last[i] - total
                    updated.append(total)
                print("before break >>", updated)
                complete = True
                break
            else:
                last.append(diff[-1])
                #decrement += 1
                curr_arr = list(reversed(diff))
                diff = []
        updated.append(child_arr[0] - updated[-1])
        print("updated", updated)
        sum_of_extrapolated_values += updated[-1]
    print(sum_of_extrapolated_values)
    return sum_of_extrapolated_values

questionTwo()
