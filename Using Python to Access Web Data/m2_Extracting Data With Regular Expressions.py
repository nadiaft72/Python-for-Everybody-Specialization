
import re
fname ="regex_sum_1744152.txt"
fh = open(fname)
counts = dict()
sum = 0
for line in fh:
    line = line.rstrip()
    if line :
        listOfNumbers = re.findall('[0-9]+' , line)
        if listOfNumbers :
            
            for num in listOfNumbers:
                sum += int(num)
            
print(sum)