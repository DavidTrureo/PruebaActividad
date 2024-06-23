import os

os.system("clear")

#bandera = True

# while bandera:
#     print("hola como estas")
#     numero = int(input("ingreser un numero\n"))
#     if numero%2==0:
#         print("es un numero par")
#         bandera = False
#     else:
#         print("es un numero impar")
        
# a = 5
# num = int(input("ingrese numero"))
# while a > num:
#     print(f"el número {num} es menor a {a}")
#     a = a + 1

print("fin")

for x in range(10):
    numero = int(input("ingrese un numero\n"))
    if numero%2==0:
        print("es un numero par")
        break
    else:
        print("es un numero impar")
        
        