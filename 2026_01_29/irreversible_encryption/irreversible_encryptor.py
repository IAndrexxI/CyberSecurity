#!/usr/bin/env python3

import base64
import string
import binascii
import sys

ALPHABET = list(string.printable)   # len = 100
LEN = len(ALPHABET)

# Get flag from command line argument
if len(sys.argv) != 2:
    print("Usage: python irreversible_encryptor.py <FLAG>")
    sys.exit(1)

FLAG = sys.argv[1]

# b64 encoding is safe and my flag secure
def base64encode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64encode(message_bytes)
    b64_message = b64_bytes.decode('ascii')
    return b64_message

# same for b32
def base32encode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32encode(message_bytes)
    b32_message = b32_bytes.decode('ascii')
    return b32_message

# I think I'm forgetting something important to remove here
def XORencode(message, KEY="S3cur3K3y!"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

# Easy-to-use function, that looks useful
def ROTencode(message, pos):
    rot_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot_enc += ALPHABET[(i+pos)%LEN]
    return rot_enc

# a useless method that could be replaced by a single line of code
# why not?
def ascii_to_hex(message):
    encoded = binascii.hexlify(message).decode()
    return encoded

# Shuffle the operations for extra security!
encrypted = "Ultra secure flag: " + FLAG

# encrypt encrypt encrypt !!!!!
for i in range(5):
    b64_encrypted = base64encode(encrypted)
    rot23_encrypted = ROTencode(b64_encrypted, 23)
    b32_encrypted = base32encode(rot23_encrypted)
    encrypted = ROTencode(b32_encrypted, 5)

for i in range(5):
    rot11_encrypted = ROTencode(encrypted, 11)
    b64_encrypted = base64encode(rot11_encrypted)
    rot29_encrypted = ROTencode(b64_encrypted, 29)
    encrypted = base32encode(rot29_encrypted)

#  I was told that XOR is a secure operation
final_xor = XORencode(encrypted, "F1n4lK3y!").encode('ascii')

# hopefully also the hex encoding will strengthen the encryption operation
hex_encrypted = ascii_to_hex(final_xor)

# save the result for later use
# one will decrypt it anyway
with open("encrypted_flag.txt", "w") as f:
    f.write(hex_encrypted)
    f.close()

print("[+] Flag encrypted successfully!")
print("[+] Output saved to: encrypted_flag.txt")