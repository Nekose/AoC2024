def generate_reactor_reports(puzzle_input_list):
    output_list = []
    for row in puzzle_input_list:
        rowlist = row.split(" ")
        intlist = [int(x) for x in rowlist]
        output_list.append(intlist)
    return output_list

def determine_safe(reactor_row):
    if reactor_row[0] - reactor_row[1] > 0:
        increasing = False
    else:
        increasing = True
    if increasing:
        for pos,value in enumerate(reactor_row):
            if pos == 0:
                continue
            if value - reactor_row[pos-1] > 3 or value - reactor_row[pos-1] <= 0:
                return False
    if not increasing:
        for pos,value in enumerate(reactor_row):
            if pos == 0:
                continue
            if value - reactor_row[pos-1] < -3 or value - reactor_row[pos-1] >= 0:
                return False
    return True

def determine_safe_dampered(reactor_row):
    failcount = 0
    if reactor_row[0] - reactor_row[1] > 0:
        increasing = False
    else:
        increasing = True
    if increasing:
        for pos,value in enumerate(reactor_row):
            if pos == 0:
                continue
            if value - reactor_row[pos-1] > 3 or value - reactor_row[pos-1] <= 0:
                failcount += 1
    if not increasing:
        for pos,value in enumerate(reactor_row):
            if pos == 0:
                continue
            if value - reactor_row[pos-1] < -3 or value - reactor_row[pos-1] >= 0:
                failcount += 1
    if failcount > 1:
        return False
    else:
        return True

def count_safe(reactor_reports):
    count = 0
    for row in reactor_reports:
        if determine_safe(row):
            count += 1
    return count

def count_safe_dampered(reactor_reports):
    count = 0
    for row in reactor_reports:
        if determine_safe_dampered(row):
            count += 1
    return count