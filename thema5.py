import requests,json

payload = {'key':'cef8cf2db3dfaf833316d2037b478ea3','format':'json'}

r1=requests.get('http://api.brewerydb.com/v2/categories',params=payload)

j1=r1.json()

print "The categories are:"

for en in j1['data']:
     print en['name']
     

btype=raw_input("Give a Category please:")

payload = {'key':'cef8cf2db3dfaf833316d2037b478ea3','q':btype,'type':'beer','format':'json'}


r=requests.get('http://api.brewerydb.com/v2/search',params=payload)
j=r.json()

if('data' in j):
    
    
   
    
    print "The beers that belong to %s are:" %(btype)

    for i in range(1,j['numberOfPages']+1):
        
        

           payload = {'key':'cef8cf2db3dfaf833316d2037b478ea3','q':btype,'type':'beer','p':i,'format':'json'}


           r=requests.get('http://api.brewerydb.com/v2/search',params=payload)
           j=r.json()
           
           
           for entry in j['data']:
               try:
                   i=1
                   print entry['nameDisplay']
                   print "*** ABV of %s is:%s " %(entry['nameDisplay'],entry['abv'])
                   

               except:
                    pass
                   
             
           
            
else:
    if ('data' not in j and j['status']=='success'):
         print "This category does not exist"
    
    print (r.text)
    r.raise_for_status() # If response code is not ok (200), print the resulting http error code with description

