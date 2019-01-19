'''
Created on Feb 1, 2018

@author: JATINJA
'''
largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    
    if num == "done" : 
        break
    try:
        fval=float(num)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest=fval
    elif fval > largest:
        largest=fval
    if smallest is None:
        smallest = fval
    elif fval < smallest:
        smallest = fval
            
print("Maximum", largest)
print("Smallest", smallest)