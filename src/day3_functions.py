import re
def return_muls(list_of_lines,regex = r"mul\(\d{1,3},\d{1,3}\)"):
    resultlist = []
    for line in list_of_lines:
        results = re.findall(regex,line)
        for result in results:
            resultlist.append(result)
    return resultlist

def return_muls_with_dos_and_donts(list_of_lines, regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"):
    resultlist = []
    for line in list_of_lines:
        results = re.findall(regex,line)
        for result in results:
            resultlist.append(result)
    return resultlist

def multiply(mulsequence):
    stripped = mulsequence.strip("mul(").strip(")")
    left,right = stripped.split(',')
    left = int(left)
    right = int(right)
    return left * right

def process_dos_and_donts(mulsequence):
    returnlist = []
    do = True
    for value in mulsequence:
        if value == "do()":
            do = True
        elif value == "don't()":
            do = False
        else:
            if do == True:
                print(value)
                returnlist.append(multiply(value))
            if do == False:
                continue
    return returnlist
