from pathlib import Path

writtenout_2_digit: dict[str, str] = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

result_part_1: int = 0
result_part_2: int = 0

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:
        part1_digit_first: str = ""
        part1_digit_last: str = ""
        part2_digit_first: str = ""
        part2_digit_last: str = ""
        for i in range(len(line)):
            part1_character: str = ""
            part2_character: str = ""
            if line[i].isdigit():
                part1_character: str = line[i]
                part2_character: str = line[i]
            else:
                for writtenout in writtenout_2_digit.keys():
                    if line[i:].startswith(writtenout):
                        part2_character: str = writtenout_2_digit[writtenout]
            if not part1_digit_first and part1_character:
                part1_digit_first: str = part1_character
            if part1_character:
                part1_digit_last: str = part1_character
            if not part2_digit_first and part2_character:
                part2_digit_first: str = part2_character
            if part2_character:
                part2_digit_last: str = part2_character
        result_part_1 += int(part1_digit_first + part1_digit_last)
        result_part_2 += int(part2_digit_first + part2_digit_last)

print("Result Part 1: ", result_part_1)
print("Result Part 2: ", result_part_2)
