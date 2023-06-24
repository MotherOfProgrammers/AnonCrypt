import random
import os
import secrets
import string
import time

import artwork
flnam = input("Enter File Name: ")
digit = " ".join(string.digits+string.ascii_letters+string.punctuation)
print("[=]  Reading The File....")
time.sleep(2)
print("[INFO] This Will Get Sometime Wait Patiently...")
print("[+] Encrypting The File....")
for digitf in digit:
	global digits
	digits = " ".join(format(ord(digitf)))
#	print("Digits",digits)
for conts in flnam:
	with open(flnam,"rb") as fl:
		content = fl.read()
		content = " ".join(format(ord(conts)))
encrypt = " ".join(random.choices(digits+content,k=10))
for enc in encrypt:
	enct = "".join(format(ord(enc),"b") for i in range(1024*24))
	encr = "".join(random.choices(enc+string.digits+string.punctuation+string.ascii_letters,k=1000*10000))
	encry = " ".join(random.choices(encr+enct,k=100*90))
#print(enct)
	with open(flnam,"wb") as file:
		file.write(bytes(encry,encoding="ascii"))
print("[SUCCESS] FILE ENCRYPTED SUCCESSFULLY!")

