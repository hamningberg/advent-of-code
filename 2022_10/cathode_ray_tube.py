from pathlib import Path

register_values = []

with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    register = 1
    for line in input_file:
        if line == "noop\n":
            register_values.append(register)
        else:
            register_values.append(register)
            register_values.append(register)
            summand = int(line.split()[1])
            register += summand

def get_signal_strength_sum(register_values):
    signal_strength_sum = 0
    for cycle in [20, 60, 100, 140, 180, 220]:
        signal_strength_sum += cycle * register_values[cycle - 1]
    return (signal_strength_sum)

def get_screen_buffer(register_values):
    screen_buffer = ""
    for pos_y in range(0, len(register_values), 40):
        for pos_x in range(40):
            register = register_values[pos_x + pos_y]
            if (register == pos_x - 1) or (register == pos_x) or (register == pos_x + 1):
                screen_buffer += "\u2588"
            else:
                screen_buffer += " "
        screen_buffer += "\n"
    return screen_buffer

print("Result Part 1:", get_signal_strength_sum(register_values))
print("Result Part 2:")
print(get_screen_buffer(register_values))

