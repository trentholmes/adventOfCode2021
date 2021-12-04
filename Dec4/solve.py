def checkBingo(card):
    cols = [0,0,0,0,0]
    rows = [0,0,0,0,0]
    for i, row in enumerate(card):
        for j, num in enumerate(row):
            if num == "X":
                rows[i] += 1
                cols[j] += 1
    
    if(5 in cols or 5 in rows):
        return True
    
    return False

with open('input.txt') as input:
    lines = input.readlines()

nums = lines.pop(0).strip().split(',')
#print(nums)

lines.pop(0)

cards = []
for i in range(100):
    cards.append([])

counter = 0
for line in lines:
    l = line.strip()
    if(l == ""):
        counter += 1
        continue

    row = []
    for n in l.split(" "):
        if(n != ""):
            row.append(n)
    
    cards[counter].append(row)

lastWin = (None, None)
firstWin = True
while(len(nums) > 0):
    n = nums.pop(0)
    for card in cards:
        for row in card:
            for i in range(len(row)):
                if(row[i] == n):
                    row[i] = "X"
    
    winners = []
    for card in cards:
        if(checkBingo(card)):
            lastWin = (n, card)
            winners.append(card)
            if(firstWin):
                total = 0
                for row in card:
                    for num in row:
                        if(num != "X"):
                            total += int(num)
                print(int(n)*total)
                firstWin = False

    for card in winners:
        cards.remove(card)

total = 0

n, card = lastWin
#print(n)
#print(card)
for row in card:
    for num in row:
        if(num != "X"):
            total += int(num)
print(int(n)*total)  

#print(cards)

   