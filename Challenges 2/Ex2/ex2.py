n1=int(input("inserisci il primo numero intero: "))
n2=int(input("inserisci il secondo numero intero: "))
operation=int(input("inserisci il numero associato all'operazione: "))

if operation==0:
    risultato=n1+n2
elif operation==1: 
    risultato=n1-n2
elif operation==2:
    risultato=n1*n2
elif operation==3:
    if n2!=0:
        risultato=n1/n2
    else:
        print("Errore: Divisione per zero non consentita.")
else:
    print("Operazione non valida.")

print(f"Risultato: {risultato}")
