n=input("Give a number please:")
a=[int(i) for i in str(n)]

n1=1
st=0
for i in range(len(a)):
    n1=n1*a[i]
    print n1

st=st+1

if(n1>=0 and n1<=9):
   print"You need to multiply the digits: %d time" %(st)
   

else:
    
    while(not(n1>=0 and n1<=9)):
        
        a=[int(i) for i in str(n1)]
        print a
        
        n1=1
        for i in range(len(a)):
            n1=n1*a[i]
            print n1



        st=st+1
        
    

  
    
    
if (st>1):
    print "You need to multiply the digits: %d times" %(st)
    

