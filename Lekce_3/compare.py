def compare(a, b):
    if a < b:
        print(b,"je vetsi nez", a)
        return True
    if a == b:
        print(a,"stejna", b)
        return True
    if a > b:
        print(a,"je vetsi nez", b)
        return True



compare(3, 5)
compare(3, 3)
compare(6, 5)
