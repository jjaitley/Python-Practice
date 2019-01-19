import re
fhand = open('regex_sum_72876.txt')
numlist=list()

for line in fhand:
    line = line.rstrip()
    
    x = re.findall('([0-9]+)', line)
    
    for numbers in x:
        if len(x) > 0:
            numlist.append(numbers)
        else:
            continue
#print(numlist)

for i in range(len(numlist)):
    numlist[i] = int(numlist[i])

#print(numlist)
print("There are", len(numlist),"values and the sum is",sum(numlist)) 