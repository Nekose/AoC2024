def buildlist(puzzle_input):
    leftlist = []
    rightlist = []
    with open(puzzle_input) as file:
        for row in file:
            row.strip("\n")
            splitrow = row.split("   ")
            leftlist.append(int(splitrow[0]))
            rightlist.append(int(splitrow[1]))
    return (leftlist,rightlist)

def sort_and_compare(leftlist,rightlist):
    distancelist = []
    leftlist.sort()
    rightlist.sort()
    for left,right in zip(leftlist,rightlist):
        distancelist.append(abs(left - right))
    return distancelist
def return_sum_of_distance_list(distancelist):
    return sum(distancelist)

def count_occurance(leftlist,rightlist):
    occurance_dict = {}
    for value in leftlist:
        occurance_dict[value] = rightlist.count(value)
    return occurance_dict

def return_sum_of_multiples(occurance_dict):
    sum = 0
    for key,value in occurance_dict.items():
        sum += key * value
    return sum