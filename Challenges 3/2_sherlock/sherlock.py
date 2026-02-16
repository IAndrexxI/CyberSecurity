with open("G:/Il mio Drive/UNIPD Andrea/CyberSecurity/Challenges 3/2_sherlock/challenge.txt") as file:
    challenge=file.read()

insight=''.join([c for c in challenge if c.isupper()]) #crea una nuova stringa insight, non si usa c: perchè è una struttura list comprehension

insight=insight.replace('ZERO', '0') 
insight=insight.replace('ONE', '1')

result=''.join(chr(int(insight[i*8:i*8+8], 2))for i in range(len(insight)//8)) #int converte un numero(insight[]) binario(2) in decimale
#non si usa len(insight)/8 perchè =2.0 (float)
print(result)