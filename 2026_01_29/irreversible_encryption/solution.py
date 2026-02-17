import base64
import string
import binascii
import sys

ALPHABET = list(string.printable)   # len = 100
LEN = len(ALPHABET)

def ROTdecode(message, pos):
    return ''.join([ALPHABET[(ALPHABET.index(c)-pos)%LEN] for c in message])

def XORdecode(message, KEY):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)]
    return ''.join([chr(ord(a)^ord(b)) for a,b in zip(message, key)])

with open("C:/Users/andre/Documents/2026_01_29/irreversible_encryption/encrypted_flag.txt")as text:
    hex_encrypted=text.read()

final_xor = binascii.unhexlify(hex_encrypted).decode('ascii')

encrypted = XORdecode(final_xor, "F1n4lK3y!")

for _ in range(5):
    b32_decoded = base64.b32decode(encrypted).decode('ascii')
    rot29_decoded = ROTdecode(b32_decoded, 29)
    b64_decoded = base64.b64decode(rot29_decoded).decode('ascii')
    encrypted = ROTdecode(b64_decoded, 11)

for _ in range(5):
    encrypted = ROTdecode(encrypted, 5)
    b32_decoded = base64.b32decode(encrypted).decode('ascii')
    rot23_decoded = ROTdecode(b32_decoded, 23)
    encrypted = base64.b64decode(rot23_decoded).decode('ascii')

print("Recovered message:", encrypted)