from pathlib import Path

subset_counter: int = 0
any_overlap_counter: int = 0

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:

        elf_1, elf_2 = line.split(",")
        elf_1_start, elf_1_end = elf_1.split("-")
        elf_2_start, elf_2_end = elf_2.split("-")
        elf_1_start, elf_1_end, elf_2_start, elf_2_end = [int(x) for x in [elf_1_start, elf_1_end, elf_2_start, elf_2_end]]

        elf_1_start = int(elf_1_start)
        elf_1_end = int(elf_1_end)
        elf_2_start = int(elf_2_start)
        elf_2_end = int(elf_2_end)

        # Part 1
        if (elf_1_start <= elf_2_start and elf_1_end >= elf_2_end) or (elf_2_start <= elf_1_start and elf_2_end >= elf_1_end):
            subset_counter += 1
    
        # Part 2
        if not(elf_1_end < elf_2_start or elf_1_start > elf_2_end):
            any_overlap_counter += 1

print("Result Part 1: {}".format(subset_counter))
print("Result Part 2: {}".format(any_overlap_counter))
