import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')

print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None
#print(json.dumps(js, indent=4)) 
sum=0
num=0
for citem in js['comments']:   #It is imp 2 knw that which part of js ur itrating
    #print('Count', citem['count'])
    cnt=int(citem['count'])
    num=num+1
    sum=sum + cnt
print('Count',num)    
print('Sum:',sum)   