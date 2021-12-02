with open('input.txt') as input:
    lines = input.readlines()

numIncreasing = 0

prev = None
for line in lines:
    num = int(line.strip())
    if(prev != None):
        if(num > prev):
            numIncreasing += 1
    
    prev = num

print(numIncreasing)

numIncreasingB = 0
for i in range(2,len(lines)):
    totalNow = int(lines[i].strip()) + int(lines[i-1].strip()) + int(lines[i-2].strip())
    totalPrev = int(lines[i-1].strip()) + int(lines[i-2].strip()) + int(lines[i-3].strip())
    if(totalNow > totalPrev):
        numIncreasingB += 1


print(numIncreasingB)
