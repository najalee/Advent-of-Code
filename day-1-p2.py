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

similarity = 0
# count how many times an ele in left exists in right
for num in leftList:
    count = rightList.count(num)
    similarity = similarity + (count * int(num))

print("Similarity: ")
print(similarity)