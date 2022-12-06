from pathlib import Path
from typing import Set

def get_marker_position(many_chars: str, unique_chars_qty: int) -> int:
    for i in range(unique_chars_qty, len(many_chars)):
        set_of_chars: Set[str] = set()
        for j in range(i - unique_chars_qty, i):
            set_of_chars.add(many_chars[j])
        if len(set_of_chars) == unique_chars_qty:
            return i

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    datastream: str = input_file.read()

print("Result Part 1: {}".format(get_marker_position(datastream,  4)))
print("Result Part 2: {}".format(get_marker_position(datastream, 14)))
