
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
fh = open(name)
counts = dict()
for line in fh:
    line = line.split()
    if line :
        if line[0] == "From" :
            time = line[5].split(":")[0]
            
            counts[time] = counts.get(time,0) + 1

# print("There were", counts, "lines in the file with From as the first word")

bigCount = None
bigWord = None

for k,v in sorted(counts.items()):
    print(k,v)
