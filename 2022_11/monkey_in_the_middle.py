from pathlib import Path
import copy

class Monkey:
    worry_levels = None
    operation = None
    test_divisible_by = None
    divisible_target = None
    indivisible_target = None
    inspections = 0

def get_monkey_business(monkeys, rounds, relief_divisor = 1, modulo_by_common_multiple = False):
    assert relief_divisor > 0

    if modulo_by_common_multiple:
        common_multiple = 1
        for monkey in monkeys:
            common_multiple *= monkey.test_divisible_by

    for _ in range(rounds):
        for monkey in monkeys:
            for worry_level in monkey.worry_levels:
                worry_level = monkey.operation(worry_level) // relief_divisor
                if modulo_by_common_multiple:
                    worry_level %= common_multiple
                if worry_level % monkey.test_divisible_by == 0:
                    monkeys[monkey.divisible_target].worry_levels.append(worry_level)
                else:
                    monkeys[monkey.indivisible_target].worry_levels.append(worry_level)
                monkey.inspections += 1
            monkey.worry_levels = []

    monkeys.sort(key = lambda m: m.inspections)
    return monkeys[-2].inspections * monkeys[-1].inspections

# Main
monkeys = []
with open(Path(__file__).parent.joinpath("input.txt"), "r") as input_file:
    for line in input_file:
        line = line.strip()
        if line:
            if line.startswith("Monkey"):
                monkey = Monkey()
                monkeys.append(monkey)
            else:
                key, value = line.split(":")
                match key:
                    case "Starting items":
                        monkey.worry_levels = list(map(int, value.split(", ")))
                    case "Operation":
                        monkey.operation = eval("lambda old:" + line.split("=")[1])
                    case "Test":
                        monkey.test_divisible_by = int(line.split()[-1])
                    case "If true":
                        monkey.divisible_target = int(line.split()[-1])
                    case "If false":
                        monkey.indivisible_target = int(line.split()[-1])

print("Result Part 1:", get_monkey_business(copy.deepcopy(monkeys), 20, relief_divisor = 3))
print("Result Part 2:", get_monkey_business(copy.deepcopy(monkeys), 10000, modulo_by_common_multiple = True))
