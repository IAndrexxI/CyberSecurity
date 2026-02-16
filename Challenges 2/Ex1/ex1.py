def shift_by_two(s):
    risultato=""
    for char in s:
        if 'a'<=char<='z':
            risultato+=chr((ord(char)-ord('a')+2)%26+ord('a')) #chr trasforma il numero nel carattere ASCII
        elif 'A'<=char<='Z':                                   #ord è l'opposto di chr
            risultato+=chr((ord(char)-ord('A')+2)%26+ord('A')) 
            #ord('a') Porta la lettera in un intervallo 0–25:, %26 serve a restare entro i limiti alfabetici A-Z
        else:
            risultato+=char
    return risultato

input_str="abc"
output_str=shift_by_two(input_str)
print(output_str)