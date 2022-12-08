from pathlib import Path
from typing import List

def is_visible(grid: List, curr_x: int, curr_y: int) -> bool:
    curr_height: int = grid[curr_y][curr_x]
    visible_from_left: bool = True
    visible_from_right: bool = True
    visible_from_top: bool = True
    visible_from_bottom: bool = True

    # Is current tree visible from the left?
    for x in range(curr_x):
        if curr_height <= grid[curr_y][x]:
            visible_from_left = False
            break

    # Is current tree visible from the right?
    if not visible_from_left:
        for x in range(curr_x + 1, len(grid[curr_y])):
            if curr_height <= grid[curr_y][x]:
                visible_from_right = False
                break

    # Is current tree visible from the top?
    if not visible_from_left and not visible_from_right:
        for y in range(curr_y):
            if curr_height <= grid[y][curr_x]:
                visible_from_top = False
                break

    # Is current tree visible from the bottom?
    if not visible_from_left and not visible_from_right and not visible_from_top:
        for y in range(curr_y + 1, len(grid)):
            if curr_height <= grid[y][curr_x]:
                visible_from_bottom = False
                break

    return visible_from_left or visible_from_right or visible_from_top or visible_from_bottom


def get_score(grid: List, curr_x: int, curr_y: int) -> int:
    curr_height: int = grid[curr_y][curr_x]
    score_left: int = 0
    score_right: int = 0
    score_top: int = 0
    score_bottom: int = 0

    # Scenic score to the left
    for x in range(curr_x - 1, -1, -1):
        score_left += 1
        if curr_height <= grid[curr_y][x]:
            break

    # Scenic score to the right
    for x in range(curr_x + 1, len(grid[curr_y])):
        score_right += 1
        if curr_height <= grid[curr_y][x]:
            break

    # Scenic score to the top
    for y in range(curr_y - 1, -1, -1):
        score_top += 1
        if curr_height <= grid[y][curr_x]:
            break

    # Scenic score to the bottom
    for y in range(curr_y + 1, len(grid)):
        score_bottom += 1
        if curr_height <= grid[y][curr_x]:
            break

    return score_left * score_right * score_top * score_bottom


# Main
grid: List = []
with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:
        grid.append(list(map(int, line.strip())))

result_part_1: int = 0
result_part_2: int = 0
for curr_y in range(len(grid)):
    for curr_x in range(len(grid[curr_y])):
        if is_visible(grid, curr_x, curr_y):
            result_part_1 += 1
        score: int = get_score(grid, curr_x, curr_y)
        result_part_2 = max(result_part_2, score)

print("Result Part 1: ", result_part_1)
print("Result Part 2: ", result_part_2)
