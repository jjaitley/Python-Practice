# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
Total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line=line.rstrip()
    numb=float(line[20:20+6])
    Total = Total + numb
    count = count +1
print("Average spam confidence:", Total/count)