file = open("day-2-input.txt")

# check if each line is increasing/decreasing between 1-3

def checkSeq(row):
    inc = False
    dec = False
    for idx in range(1, len(row)):
        if row[idx] < row[idx-1] and inc != True:
            dec = True
        elif row[idx] > row[idx-1] and dec != True:
            inc = True
        else:
            return 0

        if inc and (row[idx] - row[idx-1]) <=3:
            continue
        elif dec and (row[idx-1] - row[idx]) <=3:
            continue
        else:
            return 0
    
    return 1
    

safe = 0
for line in file:
    rowStr = line.split()
    rowInt = list(map(int, rowStr))
    safe = safe + checkSeq(rowInt)

print(safe)
