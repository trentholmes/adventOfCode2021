with open('input.txt') as input:
    lines = input.readlines()

a_1s = [0,0,0,0,0,0,0,0,0,0,0,0]
a_0s = [0,0,0,0,0,0,0,0,0,0,0,0]

for line in lines:
    l = line.strip()
    for i, c in enumerate(l):
        if(int(c) == 0):
            a_0s[i] +=1
        elif(int(c) == 1):
            a_1s[i] += 1

#print(a_0s)
#print(a_1s)

g = ""


for i in range(len(a_0s)):
    if(a_1s[i] > a_0s[i]):
        g += "1"
    else:
        g += "0"

e = ""
for c in g:
    if(c == "1"):
        e += "0"
    else:
        e += "1"

#print(g)
#print(e)

gD = 1174
eD = 2921

print(gD*eD)

#part b

#print()
#print()

b = []
for line in lines:
    l = line.strip()
    b.append(l)

counter = 0
while(len(b) > 1):
    #print(counter)
    ones = 0
    zeros = 0
    for num in b:
        if(int(num[counter]) == 1):
            ones += 1
        else:
            zeros += 1
    
    #print(ones)
    #print(zeros)
    
    removeChar = 1
    if(zeros > ones):
        removeChar = 0
    
    removeList = []
    for i in range(len(b)):
        if(int(b[i][counter]) == removeChar):
            removeList.append(i)

    subCounter = 0
    for i in removeList:
        b.pop(i-subCounter)
        subCounter += 1
    
    counter += 1


c = []
for line in lines:
    l = line.strip()
    c.append(l)

counter = 0
while(len(c) > 1):
    #print(counter)
    ones = 0
    zeros = 0
    for num in c:
        if(int(num[counter]) == 1):
            ones += 1
        else:
            zeros += 1
    
    #print(ones)
    #print(zeros)
    
    removeChar = 0
    if(zeros > ones):
        removeChar = 1
    
    removeList = []
    for i in range(len(c)):
        if(int(c[i][counter]) == removeChar):
            removeList.append(i)

    subCounter = 0
    for i in removeList:
        c.pop(i-subCounter)
        subCounter += 1
    
    counter += 1

o = b[0]
c = c[0]

oD = int(o,2)
cD = int(c,2)

print(oD*cD)