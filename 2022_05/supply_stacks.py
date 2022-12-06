from pathlib import Path
from typing import List
import copy

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    crate_stacks_part_1: List[str] = None
    crate_stacks_part_2: List[str] = None
    stack_initialization_lines: List[str] = None
    stack_ids: List[int] = None
    for line in input_file:
        if not line.startswith("move"):
            # Parse lines with initial state
            if line.strip():
                if line[1].isdigit():
                    # Line with the stack IDs
                    stack_ids = list(map(int, line.split()))
                    crate_stacks_part_1 = [[] for _ in range(len(stack_ids))]
                    for sil in reversed(stack_initialization_lines):
                        for stack_col in range(len(stack_ids)):
                            text_col: int = 1 + stack_col * 4
                            if text_col < len(sil) and sil[text_col].strip():
                                crate_stacks_part_1[stack_col].append(sil[text_col])
                    crate_stacks_part_2 = copy.deepcopy(crate_stacks_part_1)
                else:
                    # Lines with the initial crate locations
                    if not stack_initialization_lines:
                        stack_initialization_lines = []
                    stack_initialization_lines.append(line)
        else:
            # Parse lines with moves of crates
            moves, from_to = line[4:].split(" from ")
            from_stack, to_stack = from_to.split(" to ")
            moves = int(moves)
            from_stack = int(from_stack) - 1
            to_stack = int(to_stack) - 1

            # Part 1
            for i in range(moves):
                crate = crate_stacks_part_1[from_stack].pop()
                crate_stacks_part_1[to_stack].append(crate)

            # Part 2
            pile = crate_stacks_part_2[from_stack][-moves:]
            crate_stacks_part_2[to_stack].extend(pile)
            crate_stacks_part_2[from_stack] = crate_stacks_part_2[from_stack][:len(crate_stacks_part_2[from_stack])-moves]

crates_on_top_part_1: str = ""
crates_on_top_part_2: str = ""
assert(len(crate_stacks_part_1) == len(crate_stacks_part_2))
for i in range(len(crate_stacks_part_1)):
    crates_on_top_part_1 += crate_stacks_part_1[i][-1]
    crates_on_top_part_2 += crate_stacks_part_2[i][-1]

print("Result Part 1: {}".format(crates_on_top_part_1))
print("Result Part 2: {}".format(crates_on_top_part_2))
