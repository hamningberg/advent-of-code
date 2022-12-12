from pathlib import Path

class Knot:
    pos_x = 0
    pos_y = 0

    def __init__(self, next_knot):
        self.next_knot = next_knot

    @staticmethod
    def create_rope(num_of_knots):
        i = 0
        rope_head = None
        for i in range(num_of_knots):
            rope_head = Knot(rope_head)
        return rope_head

    def move(self, direction):
        if direction == "U":
            self.pos_y += 1
        if direction == "R":
            self.pos_x += 1
        if direction == "D":
            self.pos_y -= 1
        if direction == "L":
            self.pos_x -= 1
        if self.next_knot:
            return self.next_knot.follow(self)
        else:
            # Not used for puzzle but covers edge case of only one knot
            return tuple((self.pos_x, self.pos_y))

    def follow(self, previous_knot):
        # The following commented code handles diagonal moves.
        # If you uncomment it, replace the following two lines
        #    if abs(previous_knot.pos_x - self.pos_x) > 1:
        #    if abs(previous_knot.pos_y - self.pos_y) > 1:
        # by
        #    elif abs(previous_knot.pos_x - self.pos_x) > 1:
        #    elif abs(previous_knot.pos_y - self.pos_y) > 1:
        # This code is better understandable but not needed any
        # more after adding below the following two conditions:
        #    ... and not abs(previous_knot.pos_y - self.pos_y) > 1:
        #    ... and not abs(previous_knot.pos_y - my_pos_y_before_move) > 1:
#        if abs(previous_knot.pos_x - self.pos_x) > 1 and abs(previous_knot.pos_y - self.pos_y) > 1:
#            if previous_knot.pos_x > self.pos_x:
#                self.pos_x = previous_knot.pos_x - 1
#            else:
#                self.pos_x = previous_knot.pos_x + 1
#            if previous_knot.pos_y > self.pos_y:
#                self.pos_y = previous_knot.pos_y - 1

        # Remember original self.pos_x and self.pos_y because the 1st 'if'
        # might change them but the 2nd 'if' needs the original values
        my_pos_x_before_move = self.pos_x
        my_pos_y_before_move = self.pos_y

        if abs(previous_knot.pos_x - self.pos_x) > 1:
            if previous_knot.pos_x > self.pos_x:
                self.pos_x = previous_knot.pos_x - 1
            else:
                self.pos_x = previous_knot.pos_x + 1
            # The 'and not abs(...)' ensures that self.pos_y is only updated
            # for moves that are not diagonal
            if (previous_knot.pos_y != self.pos_y) and not abs(previous_knot.pos_y - self.pos_y) > 1:
                self.pos_y = previous_knot.pos_y

        if abs(previous_knot.pos_y - my_pos_y_before_move) > 1:
            if previous_knot.pos_y > my_pos_y_before_move:
                self.pos_y = previous_knot.pos_y - 1
            else:
                self.pos_y = previous_knot.pos_y + 1
            # The 'and not abs(...)' ensures that self.pos_x is only updated
            # for moves that are not diagonal
            if (previous_knot.pos_x != my_pos_x_before_move) and not abs(previous_knot.pos_x - my_pos_x_before_move) > 1:
                self.pos_x = previous_knot.pos_x

        if self.next_knot:
            # Make next knot to follow this node
            return self.next_knot.follow(self)
        else:
            # Tail knot returns position
            return tuple((self.pos_x, self.pos_y))


# Main
positions_tail_knot_part_1 = set()
positions_tail_knot_part_2 = set()

rope_with_2_knots = Knot.create_rope(2)
rope_with_10_knots = Knot.create_rope(10)

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:
        direction_of_moves = line[0]
        num_of_moves = int(line[2:])
        for m in range(num_of_moves):
            positions_tail_knot_part_1.add(rope_with_2_knots.move(direction_of_moves))
            positions_tail_knot_part_2.add(rope_with_10_knots.move(direction_of_moves))

print("Result Part 1: ", len(positions_tail_knot_part_1))
print("Result Part 2: ", len(positions_tail_knot_part_2))
