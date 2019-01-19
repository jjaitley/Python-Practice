fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
''' Sort the dictionary by value'''
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))
lst.sort(reverse=True)

''' Get the first 10 most occuring words by count in a file'''
for key, val in lst[:10]:
    print(key, val)