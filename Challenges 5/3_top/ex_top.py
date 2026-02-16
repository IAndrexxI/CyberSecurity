import random
import sys
import time

cur_time=str(time.time()).encode('ASCII') #Restituisce il tempo corrente come numero (float)
random.seed(cur_time) #inizializza il generatore di numeri casuali

with open('G:/Il mio Drive/UNIPD Andrea/CyberSecurity/Challenges 5/3_top/top_secret', 'rb') as f: #rb read binary
    secret=f.read()

sec_time=secret[-len(cur_time):] #Dammi gli ultimi N byte di secret, senza - sarebbe dammi tutto tranne i primi N caratteri
plain_time=''.join([chr(m^k)for m,k in zip(sec_time, [0x88]*len(cur_time))]) #0x88 è un numero esadecimale moltiplicato per la lunghezza
print(f"Plain time:\t{plain_time}") 

random.seed(plain_time.encode('ASCII')) #il seme (valore iniziale) è tempo decifrato con XOR convertito in byte

keys_secret=[random.randrange(256) for _ in secret[:-len(cur_time)]] #genera un numero casuale da 0 a 255, dammi tutto tranne gli ultimi N caratteri
plain_text=''.join([chr(m^k)for m,k in zip(secret[:-len(cur_time)], keys_secret)])
print(plain_text)