with open('input.txt') as input:
    lines = input.readlines()

#print(lines)
nums = lines[0].split(",")

map = {}
for i in range(9):
    map[i] = 0
#print(map)

for n in nums:
    map[int(n)] += 1

print(map)

# Part 1 use 80 #Part 2 use 256
for i in range(256):
    newMap = {}
    for i in range(9):
        newMap[i] = 0
    
    for key in map:
        if(key == 0):
            newMap[6] += map[key]
            newMap[8] += map[key]
        else:
            newMap[key-1] += map[key]
    
    map = newMap

print(map)

total = 0
for key in map:
    total += map[key]

print(total)
