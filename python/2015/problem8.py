with open("input8.txt", 'r') as f:
    lines = f.readlines()

    total_chars = 0
    total_memory = 0
    for line in lines:
        if '\n' in line:
            total_chars += len(line) - 1
        else:
            total_chars += len(line)

        total_memory += len(eval(line))

    print("Part 1 Solution:", total_chars - total_memory)

    total_encoded_chars = 0
    total_chars = 0
    for line in lines:
        encoded_string = line.replace('\n', '')
        encoded_string = encoded_string.replace('\\', '\\\\')
        encoded_string = encoded_string.replace('"', '\\"')
        encoded_string = f'"{encoded_string}"'

        if '\n' in line:
            total_chars += len(line) - 1
        else:
            total_chars += len(line)
        
        total_encoded_chars += len(encoded_string)

    print("Part 2 Solution:", total_encoded_chars - total_chars)