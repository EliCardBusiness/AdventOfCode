import re

with open("input5.txt", 'r') as f:
    lines = f.readlines()

    total_nice = 0
    for line in lines:
        has_vowels = re.search(r'[aeiou]\w*[aeiou]\w*[aeiou]', line)
        has_pair = re.search(r'([a-z])\1', line)
        has_invalid = re.search(r'(?:ab|cd|pq|xy)', line)

        if (
            has_vowels is not None 
            and has_pair is not None 
            and has_invalid is None
        ):
            total_nice += 1

    print("Part 1 Solution:", total_nice)

    total_nice = 0
    for line in lines:
        has_dual_pair = re.search(r'(\w\w)\w*\1', line)
        has_repeat = re.search(r'(\w)\w\1', line)

        if (
            has_dual_pair is not None 
            and has_repeat is not None 
        ):
            total_nice += 1

    print("Part 2 Solution:", total_nice)