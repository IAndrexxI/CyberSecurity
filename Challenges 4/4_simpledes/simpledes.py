plaintext='blocks'
key='Mu'
r=2
ciphertext='01100101 00100010 10001100 01011000 00010001 10000101'

def string2binary(text):
    return ''.join(f'{ord(c):08b}' for c in text)#08b: trasforma il numero in binario

def splitblock(block):
    Lr=block[:6]
    Rr=block[6:]
    return Lr,Rr

def expanded_miniblock(block):
    return block[0]+block[1]+block[3]+block[2]+block[3]+block[2]+block[4]+block[5]

def xor(block, key):
    res=int(block, 2)^int(key, 2)#int converte la stringa in decimale, poi ^ (xor) lavora a livello di bit
    return f'{res:08b}'

def s1_box(s1):
    row=int(s1[0])
    col=int(s1[1:],2)#b[1:] prende tutti i bit tranne il primo 
    #prende il valore corrispondente della tabella

    matrix=[
        ['101', '010', '001', '110', '011',	'100', '111', '000'],
        ['001', '100', '110', '010', '000', '111', '101', '011']
    ]

    return matrix[row][col]

def s2_box(s2):
    row=int(s2[0])
    col=int(s2[1:],2)

    matrix=[
        ['100',	'000', '110', '101', '111', '001', '011', '010'],
        ['101',	'011', '000', '111', '110', '010', '001', '100']
    ]

    return matrix[row][col]

def encryption(plaintext, key, R):
    text_encr=''

    #Rule 1
    plaintext_bin=string2binary(plaintext)
    if(len(plaintext_bin)%12!=0):
        raise Exception(f'Regola 1 non rispettata')

    #Rule 2
    key_bin=string2binary(key)
    if(len(key_bin)<8):
        raise Exception(f'Regola 2 non rispettata')

    #Rule 3
    for bnum in range(len(plaintext_bin)//12): #bnum indice del blocco
        i=bnum

        #definizione blocco
        from_=0+12*bnum #inizio blocco
        to_=12*(bnum+1) #fine blocco
        block=plaintext_bin[from_:to_] #prende 12 bit per questo blocco

        #Rule 4
        for r in range(R):

            #Rule 5
            Lr, Rr=splitblock(block)

            #Rule 6
            Rr_expanded=expanded_miniblock(Rr)

            #Rule 7
            curr_key=key_bin[(i*R+r):((i*R+r)+8)]
            Rr_exp_xor_key=xor(Rr_expanded,curr_key)

            #Rule 8
            Rr_s1=Rr_exp_xor_key[:4]
            Rr_s2=Rr_exp_xor_key[4:]

            #Rule 9
            Rr_s1_box=s1_box(Rr_s1)
            Rr_s2_box=s2_box(Rr_s2)

            #Rule 10
            Rr_s_box=Rr_s1_box+Rr_s2_box

            #Rule 11
            Rr_alt=xor(Lr, Rr_s_box)[2:]#serve a scartare i due bit iniziali extra generati dalla funzione xor che produce sempre 8 bit

            #Rule 12
            block=Rr+Rr_alt

            #Rule 13 in automatico

        text_encr+=block #va qua e non sopra perchè sennò si 
        #aggiungerebbe il blocco cifrato ad ogni round, duplicando i dati.
    
    return text_encr

def decryption(plaintext, key, R):
    text_dec=''

    #Rule 1
    plaintext_bin=plaintext

    #Rule 2
    key_bin=string2binary(key)
    if(len(key_bin)<8):
        raise Exception(f'Regola 2 non rispettata')

    #Rule 3
    for bnum in range(len(plaintext_bin)//12): #bnum indice del blocco
        i=bnum

        #definizione blocco
        from_=0+12*bnum #inizio blocco
        to_=12*(bnum+1) #fine blocco
        block=plaintext_bin[from_:to_] #prende 12 bit per questo blocco

        #Rule 4
        for r in reversed(range(R)):

            #Rule 5
            Rr, Rr_alt=splitblock(block)

            #Rule 6
            Rr_expanded=expanded_miniblock(Rr)

            #Rule 7
            curr_key=key_bin[(i*R+r):((i*R+r)+8)]
            Rr_exp_xor_key=xor(Rr_expanded,curr_key)

            #Rule 8
            Rr_s1=Rr_exp_xor_key[:4]
            Rr_s2=Rr_exp_xor_key[4:]

            #Rule 9
            Rr_s1_box=s1_box(Rr_s1)
            Rr_s2_box=s2_box(Rr_s2)

            #Rule 10
            Rr_s_box=Rr_s1_box+Rr_s2_box

            #Xor inversa
            Lr=xor(Rr_alt, Rr_s_box)[2:]
            block=Lr+Rr

        text_dec += block

    res=''
    for i in range(len(text_dec)//8):
        res+=(chr(int(text_dec[(i*8):((i+1)*8)], 2)))
    
    print(res)

decryption(encryption(plaintext, key, r), key, r)