import requests,json

movie=raw_input("Give a movie name please:")

url="http://www.omdbapi.com/"

payload = {'t': movie, 'r':'json'}


r=requests.get('http://www.omdbapi.com/',params=payload)
dict_data= json.loads(r.text) #converts json to a python dictionary

if dict_data['Response']== 'True' :
    
    
    print "The IMDB score is:",dict_data['imdbRating']
    print "The Awards are:",dict_data['Awards']
    

else:
    
    
    print (r.text)
    r.raise_for_status()

