# Program který bude šifrovat (Caesarova šifra)

def zakoduj(zpravu):
   encode = ""
   for i in zpravu:
       encode = encode + chr(ord(i)+3)
   return encode

def dekoduj(zpravu):
   decode = ""
   for i in zpravu:
       decode = decode + chr(ord(i)-3)
   return decode

encrypt = zakoduj("Radek má nejlepší kurzy! Pozor, je to tajné.")
print("\n\nZde je zašifrovaná zpráva:\n",encrypt,"\n")
decrypt = dekoduj(encrypt)
print("Zde je dešifrovaná zpráva:\n",decrypt)
print("\n\n\n\n\n")