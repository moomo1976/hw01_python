print('Jednoduchý cyklus:')
for i in [1,2,3,4,5]:
    print('Hurá!')
    print(i)

print("ŘÍDÍCÍ PROMĚNÁ \'i\':")
for i in [1,2,3,4,5]:
    print("Hurá!")
    print(i)
    
# Využití range, nepoužívá se seznam,ale range
print("Využití range:")
for i in range(10):
    print("i")

print("Používání rozsahu (od 2 do 8)  2.parametr u range")
for i in range(2,8):
    print("i")

print("3. parametr u rangeje krok a směr")
for i in range(10,1,-1):
    print("i")

print("Výpis seznamu:")
ovoce = ["jablko", "ananas", "banan", "kivi", "zelenina"]
index = 2
print(ovoce[index])
for index in range(5):
    print(index, ovoce[index])    

print("Iterace přes řetězec:")
string = "Hello World"
for x in string:
    print(x, end=" ")

print("\n")

print("Cyklus typu while:")
i=10
while i  !=0:
    print(i)
    i = i-1
    
    
    







#for x in range(10,20):
#    print(x**3)
#    
#for x in range(10,21):
#    print(x**3)    
#    
#i = 1
#print("start:", i)
#while i < 3:
#    print("x")
#    i = i + 1
#print("stop:", i)
#
#i = 0
#while i < 20:
#    i = i + 5
#print(i)
#
#x = 100
#while x > 0:
#    print("mrkev")
#    x -= 1
#x = 100
#while x > 0 and x % 5 != 1:
#    print("celer")
#    x -= 1

x = 4
#while x > 0:
#    x -= 1
#    print("celer")        
#print("celer")