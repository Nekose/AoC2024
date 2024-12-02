from src.day2_functions import generate_reactor_reports, count_safe, count_safe_dampered
from src.aoc_general_functions import parse_input

parsed_input = parse_input("data/day2_part1.txt")
print(parsed_input)
reactor_reports = generate_reactor_reports(parsed_input)
print(reactor_reports)

print(count_safe(reactor_reports))
print(count_safe_dampered(reactor_reports))