from hashlib import md5

with open('input4.txt', 'r') as f:
    string = f.read()

    total = 1
    hash_string = ""

    while hash_string[0:5] != "00000":
        total += 1
        hash = md5(string.encode('utf-8'))
        hash.update(str(total).encode('utf-8'))
        hash_string = hash.hexdigest()

    print("Part 1 Solution:", total)

    while hash_string[0:6] != "000000":
        total += 1
        hash = md5(string.encode('utf-8'))
        hash.update(str(total).encode('utf-8')) 
        hash_string = hash.hexdigest()
            
    print("Part 2 Solution:", total)
