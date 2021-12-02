with open('input.txt') as input:
    lines = input.readlines()

distance = 0
depth = 0
for line in lines:
    cmd = line.strip()
    a = cmd.split(" ")
    action = a[0]
    num = int(a[1])
    if(action == "forward"):
        distance += num
    elif(action == "up"):
        depth -= num
    elif(action == "down"):
        depth += num

print("Horizontal: " + str(distance))
print("Depth: " + str(depth))

print(depth * distance)

# Part 2

distance = 0
depth = 0
aim = 0

for line in lines:
    cmd = line.strip()
    a = cmd.split(" ")
    action = a[0]
    num = int(a[1])
    if(action == "forward"):
        distance += num
        depth += aim*num
    elif(action == "up"):
        aim -= num
    elif(action == "down"):
        aim += num

print("Horizontal: " + str(distance))
print("Depth: " + str(depth))

print(depth * distance)