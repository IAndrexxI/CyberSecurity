with open("G:/Il mio Drive/UNIPD Andrea/CyberSecurity/Challenges 3/3_ultraencoded/zero_one.txt") as text:
    input=text.read()

input=input.replace('ZERO', '0')
input=input.replace('ONE', '1')
input=input.replace(' ', '')

input=input.strip() #rimuovere spazi “inutili” all’inizio e alla fine di una stringa.

result=''.join(chr(int(input[i*8:i*8+8], 2))for i in range(len(input)//8))

import base64
decoded=base64.b64decode(result).decode('ascii')#prende quella Base64, la trasforma nei byte originali
#con .decode('ascii'): li trasformi in una stringa Python
print(decoded)

alpha2morse = {'A': '.-', 'B': '-...', 'C': '-.-.',
'D': '-..', 'E': '.', 'F': '..-.',
'G': '--.', 'H': '....', 'I': '..',
'J': '.---', 'K': '-.-', 'L': '.-..',
'M': '--', 'N': '-.', 'O': '---',
'P': '.--.', 'Q': '--.-', 'R': '.-.',
'S': '...', 'T': '-', 'U': '..-',
'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..',
'0': '-----', '1': '.----', '2': '..---',
'3': '...--', '4': '....-', '5': '.....',
'6': '-....', '7': '--...', '8': '---..',
'9': '----.' }

morse2alpha={value:key for key,value in alpha2morse.items()} #dictionary comprehension
#inverte il dizionario, alpha2morse.items() restituisce coppie (key, value)
#for(che scorre) key, value, value:key è la copia invertita
decoded2=''.join(morse2alpha.get(i) for i in decoded.split())#decoded.split() divide la stringa sugli spazi
# .get(i) cerca la chiave i nel dizionario e restituisce la lettera
print(decoded2)

