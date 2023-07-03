

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    line = line.split()
    if line :
        if line[0] == "From" :
            counts[line[1]] = counts.get(line[1],0) + 1

# print("There were", counts, "lines in the file with From as the first word")

bigCount = None
bigWord = None

for k,v in counts.items():
    if bigCount is None or v > bigCount:
        bigCount = v
        bigWord = k

print(bigWord,bigCount)