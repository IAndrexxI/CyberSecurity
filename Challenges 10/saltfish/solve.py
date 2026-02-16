import requests 
import string 

for i in string.ascii_letters: 
    url = f"http://127.0.0.1:9000/?pass={i}" 
    r = requests.get(url, headers={'User-Agent': str(i)}) 
    print(r.text) 