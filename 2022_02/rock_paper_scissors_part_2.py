from pathlib import Path

rps_scores = { 'X' : 1, 'Y' : 2, 'Z' : 3 }
score_total = 0

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:
        my_shape = ''
        score = 0
        if line[2] == 'X':   # I loose
            match line[0]:
                case 'A':
                    my_shape = 'Z'
                case 'B':
                    my_shape = 'X'
                case 'C':
                    my_shape = 'Y'
        if line[2] == 'Y':   # Draw
            score = 3
            match line[0]:
                case 'A':
                    my_shape = 'X'
                case 'B':
                    my_shape = 'Y'
                case 'C':
                    my_shape = 'Z'
        if line[2] == 'Z':   # I win
            score = 6
            match line[0]:
                case 'A':
                    my_shape = 'Y'
                case 'B':
                    my_shape = 'Z'
                case 'C':
                    my_shape = 'X'
        score_total = score_total + score + rps_scores[my_shape]

print("Result Part 2: {}".format(score_total))
