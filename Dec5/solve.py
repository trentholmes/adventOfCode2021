with open('input.txt') as input:
    lines = input.readlines()

vectors = []
for line in lines:
    l = line.strip()
    sep = l.split(" -> ")
    start = sep[0].split(",")
    end = sep[1].split(",")
    vectors.append(((int(start[0]), int(start[1])),(int(end[0]), int(end[1])) ))

#print(vectors)

#maxX = 0
#maxY = 0
#for v in vectors:
#    if(v[0][0] == v[1][0] or v[0][1] == v[1][0]):
#        if(v[0][0] > maxX):
#            maxX = v[0][0]
#        if(v[0][1] > maxY):
#            maxY = v[0][1]
#        
#        if(v[1][0] > maxX):
#            maxX = v[0][0]
#        if(v[1][1] > maxY):
#            maxY = v[0][1]
#
#print(maxX)
#print(maxY)

grid = []
for i in range(1000):
    a = []
    for j in range(1000):
        a.append(0)
    grid.append(a)

#print(grid)

for v in vectors:
    start, end = v
    if start[0] == end[0]:
        if start[1] > end[1]:
            for j in range(end[1],start[1]+1):
                grid[start[0]][j] += 1
        else:
            for j in range(start[1],end[1]+1):
                grid[start[0]][j] += 1
    elif start[1] == end[1]:
        if start[0] > end[0]:
            for j in range(end[0],start[0]+1):
                grid[j][start[1]] += 1
        else:
            for j in range(start[0],end[0]+1):
                grid[j][start[1]] += 1
    else: #remove this else for part a
        if start[0] > end[0]:
            if(start[1] > end[1]):
                otherIndex = end[1]
                for i in range(end[0], start[0]+1):
                    grid[i][otherIndex] += 1
                    otherIndex += 1
            else:
                otherIndex = end[1]
                for i in range(end[0], start[0]+1):
                    grid[i][otherIndex] += 1
                    otherIndex -= 1
            
        else:
            if(start[1] > end[1]):
                otherIndex = start[1]
                for i in range(start[0], end[0]+1):
                    grid[i][otherIndex] += 1
                    otherIndex -= 1
            else:
                otherIndex = start[1]
                for i in range(start[0], end[0]+1):
                    grid[i][otherIndex] += 1
                    otherIndex += 1

counter = 0
for row in grid:
    for col in row:
        if(col > 1):
            counter += 1

print(counter)

