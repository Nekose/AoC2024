
def parse_input(puzzle_input):
    puzzle_input_list = []
    with open(puzzle_input) as file:
        for row in file:
            puzzle_input_list.append(row.strip("\n"))
    return puzzle_input_list