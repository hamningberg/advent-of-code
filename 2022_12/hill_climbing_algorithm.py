from pathlib import Path
from collections import deque


def breadth_first_search(grid, dest_square):
    unvisited_squares = deque([dest_square])
    distance_by_square = dict()
    distance_by_square[dest_square] = 0

    while unvisited_squares:
        current = unvisited_squares.popleft()
        for reachable in get_reachable_squares(grid, current):
            if reachable not in distance_by_square:
                distance_by_square[reachable] = distance_by_square[current] + 1
                unvisited_squares.append(reachable)

    return distance_by_square


def get_reachable_squares(grid, square):
    x, y = square
    reachable_squares = []
    square_elevation = grid[x][y] - 1

    if (0 < x) and (square_elevation <= grid[x - 1][y]):
        reachable_squares.append((x - 1, y))
    if (x < len(grid) - 1) and (square_elevation <= grid[x + 1][y]):
        reachable_squares.append((x + 1, y))
    if (0 < y) and (square_elevation <= grid[x][y - 1]):
        reachable_squares.append((x, y - 1))
    if (y < len(grid[0]) - 1) and (square_elevation <= grid[x][y + 1]):
        reachable_squares.append((x, y + 1))

    return reachable_squares


# Main
start_square = None
dest_square = None
grid = []
starting_squares = []
with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for x, line in enumerate(input_file):
        grid.append([])
        for y, letter in enumerate(line.strip()):
            match letter:
                case "S":
                    grid[-1].append(ord("a") - 97)
                    start_square = (x, y)
                case "E":
                    grid[-1].append(ord("z") - 97)
                    dest_square = (x, y)
                case _:
                    grid[-1].append(ord(letter) - 97)
            # Record starting squares for part 2
            if letter == "S" or letter == "a":
                starting_squares.append((x, y))


distance_by_square = breadth_first_search(grid, dest_square)
distance_from_start = distance_by_square[start_square]

distance_min = distance_from_start
for square in starting_squares:
    distance_min = min(distance_min, distance_by_square.get(square, distance_from_start))

print("Result Part 1:", distance_from_start)
print("Result Part 2:", distance_min)
