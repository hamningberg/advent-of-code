from pathlib import Path

result_part_1 = 0
result_part_2 = 0

max_possible_red = 12
max_possible_green = 13
max_possible_blue = 14

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:
        # Part 1
        possible = True

        # Part 2
        fewest_red = 0
        fewest_green = 0
        fewest_blue = 0

        # Process
        head, tail = line.rstrip().split(": ")
        game_id = int(head[4:])
        drawings = tail.split("; ")
        for drawing in drawings:
            cubes = drawing.split(", ")
            for color_quantity in cubes:
                color = color_quantity.split(" ")[1]
                quantity = int(color_quantity.split(" ")[0])
                if color == "red":
                    if quantity > max_possible_red:
                        possible = False
                    if quantity > fewest_red:
                        fewest_red = quantity
                if color == "green":
                    if quantity > max_possible_green:
                        possible = False
                    if quantity > fewest_green:
                        fewest_green = quantity
                if color == "blue":
                    if quantity > max_possible_blue:
                        possible = False
                    if quantity > fewest_blue:
                        fewest_blue = quantity

        # Part 1
        if possible:
            result_part_1 += game_id

        # Part 2
        result_part_2 += fewest_red * fewest_green * fewest_blue

print("Result Part 1: ", result_part_1)
print("Result Part 2: ", result_part_2)
