"""9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
"""

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