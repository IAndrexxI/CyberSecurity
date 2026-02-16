import base64

original_data="El Psy Congroo" 
encrypted_data="IFhiPhZNYi0KWiUcCls=" 
encrypted_flag="I3gDKVh1Lh4EVyMDBFo=" 

def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors='ignore')

string_data=base64tostring(encrypted_data)
string_flag=base64tostring(encrypted_flag)

key=''.join([chr(ord(x)^ord(y)) for x,y in zip(original_data,string_data)]) #zip prende una coppia di caratteri
print('key:\t',key)

flag=''.join([chr(ord(x)^ord(y)) for x,y in zip(string_flag,key)])
print('flag:\t',flag)