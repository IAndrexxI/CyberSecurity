with open("G:/Il mio Drive/UNIPD Andrea/CyberSecurity/Challenges 4/3_alphabet_soup/encrypted.txt") as file:
    text=file.read()

chr2freq={}
for c in text:
    if c not in chr2freq:
        chr2freq[c]=1
    else:
        chr2freq[c]+=1

sorted_x=sorted(chr2freq.items(), key=lambda k:k[1], reverse=True)
#.items() restituisce coppie(k[0]=chiave, k[1]=valore), key=kv[1]=valore, reverse=True ordina decrescente
print(sorted_x)

voc={'K':'i'}#è un dizionario associa i a K
#aggiunge una coppia chiave valore
voc['Q']='m'
voc['F']='a'
voc['W']='f'
voc['A']='l'
voc['I']='g'
voc['G']='d'
voc['P']='y'
voc['D']='o'
voc['T']='u'
voc['C']='r'
voc['M']='n'
voc['V']='w'
voc['H']='b'
voc['U']='e'
voc['N']='t'
voc['L']='h'
voc['B']='s'
voc['X']='c'
voc['S']='v'
voc['J']='p'
#si è presa la frequenza delle lettere e si è sostituita con quelle dell'alfabeto italiano in ordine di frequenza
dec=''.join(c if c not in voc else voc[c] for c in text)
print(voc, '\n', dec) 