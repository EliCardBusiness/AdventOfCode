def travel(instructions: str):
    coord = (0, 0)
    coords = set()
    coords.add(coord)

    for c in instructions:
        if c == '^':
            coord = (coord[0], coord[1] + 1)
        elif c == 'v':
            coord = (coord[0], coord[1] - 1)
        elif c == '>':
            coord = (coord[0] + 1, coord[1])
        elif c == '<':
            coord = (coord[0] - 1, coord[1])
        
        coords.add(coord)

    return coords

with open("input3.txt", 'r') as f:
    string = f.read()

    print("Part 1 Solution:", len(travel(string)))
    
    dual_paths = set.union(
        travel(string[::2]), 
        travel(string[1::2])
    )
    print("Part 2 Solution:", len(list(dual_paths)))
