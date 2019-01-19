'''
Created on Jan 30, 2018

@author: JATINJA
'''
try:
    hrs = float(input("Enter Hours:"))
    rate = float(input("Enter Rate:"))
    
except:
    print("Please enter a valid numeric input ")
    quit()

def computepay(h,r):
    if hrs > 40:
        TP= (40 * r) + (h-40) * 1.5 * r

    else:
        TP =(h * r)
        
    return TP

p = computepay(hrs,rate)
print("Pay",p)