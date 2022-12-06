from pathlib import Path

rps_scores = { 'X' : 1, 'Y' : 2, 'Z' : 3 }
score_total = 0

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:
        score = 0
        if line == 'C X\n' or line == 'A Y\n' or line == 'B Z\n':
            score = 6
        elif line == 'A X\n' or line == 'B Y\n' or line == 'C Z\n':
            score = 3
        score_total = score_total + score + rps_scores[line[2]]

print("Result Part 1: {}".format(score_total))