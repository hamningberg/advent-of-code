from pathlib import Path

# Returns True if character at position is a symbol.
# Used for puzzle part 1.
def is_symbol(y, x, lines):
    if 0 <= y < len(lines) and 0 <= x < len(lines[0]):
        return lines[y][x] != "." and not lines[y][x].isdigit()
    else:
        return False

# Returns the passed dictionary after adding the part number to the dictionary if it sits adjacent to a gear.
# Used for puzzle part 2.
def record_part_number_for_gear(y, x, lines, part_num, gear_2_adjacent_part_nums):
    if 0 <= y < len(lines) and 0 <= x < len(lines[0]):
        if lines[y][x] == "*":
            gear_pos = str(y) + " " + str(x)
            adjacent_part_nums = gear_2_adjacent_part_nums.get(gear_pos, [])
            adjacent_part_nums.append(part_num)
            gear_2_adjacent_part_nums[gear_pos] = adjacent_part_nums
    return gear_2_adjacent_part_nums

# Variables to capture results
result_part_1 = 0
result_part_2 = 0

# Ingest input file
with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    data = input_file.read()
    lines = data.splitlines()

# Mapping of gear location to adjacent part numbers for puzzle part 2
gear_2_adjacent_part_nums = {}

# Process input line by line
for y, line in enumerate(lines):
    x = 0
    while x < len(lines[0]):
        start_num = x
        part_num = ""
        while x < len(lines[0]) and line[x].isdigit():
            # Compose part number string
            part_num += line[x]
            x += 1

        if not part_num:
            # No digit at current position, so step to the right
            x += 1
        else:
            # Part number composed; now look around
            part_num = int(part_num)

            # Puzzle part 1: If symbol is adjacent left or right of part number, add it to result
            if is_symbol(y, start_num - 1, lines) or is_symbol(y, x, lines):
                result_part_1 += part_num

            # Puzzle part 1: If symbol is adjacent above or below of part number, add it to result
            for x_adj in range(start_num - 1, x + 1):
                if is_symbol(y - 1, x_adj, lines) or is_symbol(y + 1, x_adj, lines):
                    result_part_1 += part_num

            # Puzzle part 2: If gear is adjacent left or right of part number, record it
            gear_2_adjacent_part_nums = record_part_number_for_gear(y, start_num - 1, lines, part_num, gear_2_adjacent_part_nums)
            gear_2_adjacent_part_nums = record_part_number_for_gear(y, x, lines, part_num, gear_2_adjacent_part_nums)

            # Puzzle part 2: If gear is adjacent above or below of part number, record it
            for x_adj in range(start_num - 1, x + 1):
                gear_2_adjacent_part_nums = record_part_number_for_gear(y - 1, x_adj, lines, part_num, gear_2_adjacent_part_nums)
                gear_2_adjacent_part_nums = record_part_number_for_gear(y + 1, x_adj, lines, part_num, gear_2_adjacent_part_nums)

# Puzzle part 2: If two part numbers are adjacent a gear, multiply them and add them to result
for adjacent_part_nums in gear_2_adjacent_part_nums.values():
    if len(adjacent_part_nums) == 2:
        result_part_2 += adjacent_part_nums[0] * adjacent_part_nums[1]

print("Result Part 1: ", result_part_1)
print("Result Part 2: ", result_part_2)
