from pathlib import Path

def get_priority(item_type: str) -> int:
    assert len(item_type) == 1
    assert 'A'<=item_type<='Z' or 'a'<=item_type<='z'
    if item_type.isupper():
        return ord(item_type) - ord('A') + 26 + 1
    else:
        return ord(item_type) - ord('a') + 1

priorities_sum_part_1: int = 0
priorities_sum_part_2: int = 0

line_counter: int = 0
rucksack_1: str = ""
rucksack_2: str = ""

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:

        # Part 1
        first_half, second_half = line[:len(line)//2], line[len(line)//2:]
        for item_type in first_half:
            if item_type in second_half:
                priorities_sum_part_1 += get_priority(item_type)
                break

        # Part 2
        line_counter += 1
        match line_counter % 3:
            case 1:
                rucksack_1 = line
            case 2:
                rucksack_2 = line
            case 0:
                for item_type in line:
                    if item_type in rucksack_1 and item_type in rucksack_2:
                        priorities_sum_part_2 += get_priority(item_type)
                        break

print("Result Part 1: {}".format(priorities_sum_part_1))
print("Result Part 2: {}".format(priorities_sum_part_2))
