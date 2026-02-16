puzzle='vhixoieemksktorywzvhxzijqni'

def caesar_cracker(text,from_=-30,to_=+30):
    for i in range(from_,to_):
        curr_step=''.join([chr(ord(c)+i) for c in text])
        print(f'Step={i}\t{curr_step}')
caesar_cracker(puzzle)

text='vhixoieemksktorywzvhxzijqni'

def vigenere(text,key):
    key=key*(len(text)//len(key)+1) #+1 perhè key deve essere più lunga del testo
    return ''.join([chr((ord(text[i])-ord(key[i]))%26+ord('a'))for i in range(len(text))])
print(vigenere(text,'caesar'))