with open("input2.txt", 'r') as f:
    lines = f.readlines()

    wrapping = 0
    ribbon = 0

    
    for line in lines:
        l, w, h  = sorted(list(map(int, line.split('x'))))

        wrapping += 2 * sum([l * w, l * h, w * h]) + l * w
        ribbon += 2 * (l + w) + l * w * h

    print("Part 1 Solution:", wrapping)
    print("Part 2 Solution:", ribbon)

f.close()