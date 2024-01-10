import re

def determine_command(string: str):
    commands = ["AND", "OR", "LSHIFT", "RSHIFT", "NOT"]

    for command in commands:
        if command in string:
            return command
    
    return 'ASSIGN'

def add_command(assignments: dict, string: str, command: str):
    if command in ["AND", "OR", "LSHIFT", "RSHIFT"]:
        match = re.match(r'(\d+|\w+) \w+ (\d+|\w+) \-\> (\w+)', string)
        input1, input2, output = match.groups()

        if input1.isnumeric():
            input1 = int(input1)
        if input2.isnumeric():
            input2 = int(input2)

        assignments[output] = (command, input1, input2)
    elif command == "NOT":
        match = re.match(r'NOT (\d+|\w+) \-\> (\w+)', string)
        input, output = match.groups()

        if input.isnumeric():
            input = int(input)

        assignments[output] = (command, input)
    elif command == "ASSIGN":
        match = re.match(r'(\d+|\w+) \-\> (\w+)', string)
        input, output = match.groups()

        if input.isnumeric():
            input = int(input)

        assignments[output] = (command, input)

    return assignments

def run_procedure(assignments: dict, procedure: tuple):
    command, *inputs = procedure

    for i in range(len(inputs)):
        inputs[i] = inputs[i] if type(inputs[i]) == int else traverse(assignments, inputs[i])

    if command == "AND":
        return inputs[0] & inputs[1]
    elif command == "OR":
        return inputs[0] | inputs[1]
    elif command == "LSHIFT":
        return inputs[0] << inputs[1]
    elif command == "RSHIFT":
        return inputs[0] >> inputs[1]
    elif command == "NOT":
        return ~inputs[0]
    elif command == "ASSIGN":
        return inputs[0]

def traverse(assignments, variable: str):
    procedure = assignments[variable]
    
    val = run_procedure(assignments, procedure)
    assignments[variable] = ("ASSIGN", val)
    return val

with open('input7.txt', 'r') as f:
    lines = f.readlines()

    assignments = {}
    for line in lines:
        command = determine_command(line)
        assignments = add_command(assignments, line, command)

    val = traverse(assignments, "a")
    print("Part 1 Solution:", val)

    assignments2 = {}
    for line in lines:
        command = determine_command(line)
        assignments2 = add_command(assignments2, line, command)

    assignments2['b'] = ("ASSIGN", val)
    print("Part 2 Solution:", traverse(assignments2, "a"))