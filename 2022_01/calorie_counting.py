from pathlib import Path

calories_max_1 = 0
calories_max_2 = 0
calories_max_3 = 0
calories_elf = 0

with open(Path(__file__).parent.joinpath("input.txt"), "r") as calories_file:
    for line in calories_file:
        line = line.strip()
        if line:
            calories_elf = calories_elf + int(line)
        else:
            if calories_elf > calories_max_3:
                if calories_elf > calories_max_2:
                    calories_max_3 = calories_max_2
                    if calories_elf > calories_max_1:
                        calories_max_2 = calories_max_1
                        calories_max_1 = calories_elf
                    else:
                        calories_max_2 = calories_elf
                else:
                        calories_max_3 = calories_elf
            calories_elf = 0

print("Result Part 1: {}".format(calories_max_1))
print("Result Part 2: {}".format(calories_max_1 + calories_max_2 + calories_max_3))