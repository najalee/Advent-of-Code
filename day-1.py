# read the file
# make the first column l1 and second l2
# sort then compare index to index

f = open("day-1-input.txt")
# print(f.read())
mlist = []
for lines in f:
    lst = lines.split()
    mlist = mlist+lst

leftList = []
rightList = []
for idx in range(len(mlist)):
    if idx%2 == 0:
        leftList.append(mlist[idx])
    else:
        rightList.append(mlist[idx])

leftList.sort()
rightList.sort()

dist = 0
for idx in range(len(leftList)):
    val = int(leftList[idx]) - int(rightList[idx])
    dist = dist + abs(val)

print("Total distance: ")
print(dist)