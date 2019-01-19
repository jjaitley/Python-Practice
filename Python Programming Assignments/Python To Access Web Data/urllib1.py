import urllib
import re
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Input prompts
url = input('Enter URL: ')
print(url)
count = input('Enter count: ')
count = int(count)
position = input('Enter position: ')
position = int(position)

# repeat count number of times
for i in range(0, count+1):

    #read in url and soup it
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    if i < count:
        print("Retrieving: "),url
    else:
        print("Last Url: "), url
        break

    # Retrieve all of the anchor tags
    tags = soup('a')

    # loop through tags and find the tag at position
    pos = 0
    for tag in tags:
        if pos == position-1:
            url = str(tag.get('href', None))
            break
        pos += 1