import random
import string
# import string serve per usare il modulo string
length=10
caratteri=string.ascii_letters+string.digits
password=''.join(random.choice(caratteri) for _ in range(length))
#join serve a unire elementi di una lista in una stringa
#il _ è una variabile che non 'mi' interessa usare
print(password)