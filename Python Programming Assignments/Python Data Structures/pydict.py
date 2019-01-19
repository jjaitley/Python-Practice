name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    words=line.split()
    if len(words) < 1 or words[0]!='From': #Guardian code to handle empty line#
        continue
    email=words[1]
    counts[email]= counts.get(email,0) + 1  # If the key is not there the count is 0 and add 1
print(counts)

largest=-1
Maxemails=None
 
for k,v in counts.items():
    if v > largest:
        largest=v
        Maxemails=k
print(Maxemails,largest)

                    

               

        