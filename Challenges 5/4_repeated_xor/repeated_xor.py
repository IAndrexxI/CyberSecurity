with open('G:/Il mio Drive/UNIPD Andrea/CyberSecurity/Challenges 5/4_repeated_xor/encrypted.txt', 'r') as file:
    secret_hex=file.read()

def hex2dec(text):
    res=[]
    for i in range(len(text)//2):
        curr=text[i*2:(i+1)*2] #prende i caratteri da indice a fino a b (escluso)
        res.append(int(curr, 16)) #converte da base 16 a base 10 la coppia di caratteri
        #append aggiunge un elemento alla fine della lista
    return res

secret=hex2dec(secret_hex)

def shift(text, key_length):
    return text[key_length:]+text[:key_length] #ruota i caratteri da key_length in poi con quelli fino a key_length

def freq_counter(s1,s2):
    freq=sum([1 for (x, y) in zip(s1,s2) if x==y]) #somma tutti gli 1 per ogni x, y corrispondente
    return freq

for kl in range(5, 16):
    print(f"Length:\t{kl}\tFreq:\t{freq_counter(secret, shift(secret, kl))}")

def splitter(text, key_length):
    res=[]
    for i in range(key_length):
        res.append(text[i::key_length]) #Prendi tutti gli elementi di text partendo dall’indice i,
        #saltando ogni key_length elementi i=0: text[0], text[8], text[16]...
        #                                  i=1: ...
    return res

secret_=splitter(secret, 8)

from collections import Counter #speciale dizionario per contare quante volte appare ogni elemento in una sequenza
def k_char(text, k):
    freq=Counter(text) #conta quante volte si ripete ogni byte
    ordered=sorted(freq.items(),key=lambda x: x[1], reverse=True) #ordina in base al secondo elemento delle tuple (frequenza)
    return ordered[k][0] # ritorna il k-esimo byte più frequente

key_sec=[k_char(secret_[0], 0), k_char(secret_[1],0), k_char(secret_[2], 0), k_char(secret_[3], 0),
 k_char(secret_[4], 0), k_char(secret_[5], 0), k_char(secret_[6], 0), k_char(secret_[7], 0)] #trova il byte più frequente[0] della colonna

real_key=[k ^ord(' ') for k in key_sec] #nella colonna del testo cifrato, il byte più frequente corrisponde molto probabilmente allo spazio
real_message=''

for i, c in enumerate(secret): #enumerate(secret): indice + valore per ogni byte
    key_pos=i%8 #serve per rimanere nel range della chiave da ripetere ciclicaamente ogni 8 caratteri
    real_message+=chr(c ^real_key[key_pos])

print(real_message)