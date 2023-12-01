elves_list = []
raw_data = open("day_1.txt", "r")
elve_load = 0
for idx, row in enumerate(raw_data):
    if row == '\n':
        elves_list.append(elve_load)
        elve_load = 0
    else:
        elve_load = elve_load + int(row)
print(elves_list)
elves_list.sort()
print(elves_list)
print("I am carrying the heavies load: ", max(elves_list))
top_three = elves_list[-3::]
print("We are the top 3 elves carrying the heaviest", top_three)
print("The total load we are carrying is: ", sum(top_three))
