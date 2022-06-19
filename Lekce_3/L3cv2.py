#CV2: zadat 2 čísla na vstupu programu 
#(příkaz: input() ) porovnat
from tkinter import Y


x = input("Zadej 1.číslo (x):")
#print("zadané číslo x je: ", x)

y = input("Zadej 1.číslo (y):")
#print("zadané číslo y je: ", y)
if x < y:
    print("Číslo x je menší, než číslo y:", x,"<",y)
if y < x:
    print("Číslo y je menší, než číslo x:", y,"<",x)
if x == y:
    print("Číslo x je rovno číslu y:", x,"=",y)
