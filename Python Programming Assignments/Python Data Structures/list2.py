fname = input("Enter file name: ")

if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    word=line.rstrip().split()
    if len(word) < 1 or word[0]!='From': #Guardian code to handle empty line#
        continue
    
    print(word[1])
    count=count+1
print("There were", count, "lines in the file with From as the first word")