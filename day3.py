from src.day3_functions import return_muls,multiply,return_muls_with_dos_and_donts,process_dos_and_donts
from src.aoc_general_functions import parse_input

input_list = parse_input("data/day3_part1.txt")
listmuls = return_muls_with_dos_and_donts(input_list)
processed_list = process_dos_and_donts(listmuls)
print(processed_list)
print(sum(processed_list))
