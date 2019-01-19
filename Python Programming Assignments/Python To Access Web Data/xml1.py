import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


url = input('Enter location: ')
# 'http://python-data.dr-chuck.net/comments_42.xml'
# 'http://py4e-data.dr-chuck.net/comments_72880.xml'

print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)

results = tree.findall('comments/comment')
print('#No of count under comment:', len(results))    
sum=0
for citem in results:
    cnt=int(citem.find('count').text)
    sum=sum + cnt
print('Sum:',sum)    
        