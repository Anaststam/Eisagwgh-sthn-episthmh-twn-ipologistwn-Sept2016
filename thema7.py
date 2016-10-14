number=input("Give a number please:")
r=number/2 + 1 #+1 for ceil

a=[]
for i in range(0,r+1):
    a.append(i)
    


first=0; #binary search

last=len(a)-1


found=False
square=[]

while (first<=last and found==False):
    midpoint=(first+last)/2
    
    if (a[midpoint]**2==number):
        found=True
        square=a[midpoint]
        
    else :
        if (a[midpoint]**2<number):
            first=midpoint+1
        else:
            last=midpoint-1
        
if (found==False):
    print "False.This number is not square"
else:
    print " True. %d is the square of %d or -%d" %(number,square,square)
    


