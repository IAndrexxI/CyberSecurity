import hashlib

for i in range(0, 100000000):
    hash_object=hashlib.md5(str(i).encode())#converte il numero in stringa e poi in bytes,  hashlib.md5 funziona su bytes
        #crea un oggetto hash MD5
    if hash_object.hexdigest()=='365d38c60c4e98ca5ca6dbc02d396e53': #hash_object.hexdigest() restituisce la rappresentazione esadecimale a 32 caratteri dell’MD5
        print(i)
        break #esce immmediatamente dal for