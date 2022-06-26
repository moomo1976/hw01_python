#def cipher_columns(text, n):
#    for i in range(n):
#for j in range(len(text) // n + 1):
#position = j * n + i
#if position < len(text):
#print(text[position], end="")
#print()

def caesar_cipher(text, n):
    result = ""
    text = text.upper()
    for i in range(len(text)):
        if text[i] =='': result = result + ''
    
        else:
            c = ord(text[i]) + n

            if (c > ord('Z')): c = c - 26
            result = result + chr(c)
    return result