import base64
enc_b64='Q2Flc2FyCg=='

def base64tostring(text):
    return base64.b64decode(text).decode('UTF-8', errors='ignore')
    #Converte in una stringa in UTF-8, errors="ignore" significa: Se ci sono byte non validi per UTF-8 li salta
print(f"Decoding=\t{base64tostring(enc_b64)}")

puzzle='fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=='
print("the length of puzzle is:\t", len(puzzle)) #Verificare che sembri Base64 (multipla di 4)

puzzle_dec=base64tostring(puzzle)
print("Decoded puzzle:", puzzle_dec)

def caesar_cracker(text, from_=-30, to_=+30):
    for i in range(from_,to_):#key[-30,+30]
        current_step=''.join([chr(ord(c)+i) for c in text])
        # prende il codice ASCII del carattere lo sposta di i, torna a carattere
        print(f"Step{i}:\t{current_step}")
caesar_cracker(puzzle_dec)