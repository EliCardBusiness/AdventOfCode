import re

def flip_lights(arr, command, point1, point2):

    for row in range(point1[1], point2[1] + 1):
        for col in range(point1[0], point2[0] + 1):
            if command == 'toggle':
                arr[row][col] = 1 if arr[row][col] == 0 else 0
            elif command == 'on':
                arr[row][col] = 1
            elif command == 'off':
                arr[row][col] = 0

def adjust_lights(arr, command, point1, point2):
    for row in range(point1[1], point2[1] + 1):
        for col in range(point1[0], point2[0] + 1):
            if command == 'toggle':
                arr[row][col] += 2
            elif command == 'on':
                arr[row][col] += 1
            elif command == 'off':
                arr[row][col] -= 0 if arr[row][col] == 0 else 1


with open("input6.txt", 'r') as f:
    lines = f.readlines()

    lights = [[0 for j in range(1000)] for i in range(1000)]
    brightness = [[0 for j in range(1000)] for i in range(1000)]

    for line in lines:
        match = re.match(r'(?:turn )?(\w+) (\d+),(\d+) through (\d+),(\d+)', line)
        command, x1, y1, x2, y2 = match.groups()

        flip_lights(lights, command, (int(x1), int(y1)), (int(x2), int(y2)))
        adjust_lights(brightness, command, (int(x1), int(y1)), (int(x2), int(y2)))

    total_lights = 0
    for arr in lights:
        total_lights += sum(arr)
        
    total_brightness = 0
    for arr in brightness:
        total_brightness += sum(arr)

    print("Part 1 Solution:", total_lights)
    print("Part 2 Solution:", total_brightness)