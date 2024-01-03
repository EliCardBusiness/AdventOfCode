with open("input1.txt", 'r') as f:
    string = f.read()

    total = 0
    pos = -1

    for i in range(len(string)):
        total += 1 if string[i] == '(' else -1
        
        if total == -1 and pos == -1:
            pos = i + 1

    print("Part 1 Solution:", total)
    print("Part 2 Solution:", pos)

f.close()
