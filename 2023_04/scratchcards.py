from pathlib import Path

# Variables to capture results
result_part_1 = 0
result_part_2 = 0

# Ingest input file
with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    data = input_file.read()
    lines = data.splitlines()

# Quantity of each card for puzzle part 2 
card_quantities = [1] * len(lines)

# Main loop
for index, line in enumerate(lines):
    after_colon = line.split(": ")[1]
    left, right = after_colon.split(" | ")
    winning = set(left.split())
    haves = set(right.split())
    matches_quantity = len(winning.intersection(haves))

    # Puzzle part 1
    if matches_quantity > 0:
        result_part_1 += 2 ** (matches_quantity - 1)

    # Puzzle part 2
    for next in range(index + 1, min(index + matches_quantity + 1, len(lines))):
        card_quantities[next] += card_quantities[index]
    result_part_2 += card_quantities[index]

print("Result Part 1: ", result_part_1)
print("Result Part 2: ", result_part_2)
