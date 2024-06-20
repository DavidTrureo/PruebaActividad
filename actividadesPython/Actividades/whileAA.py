import os

os.system("cls")

# bandera = True

# while bandera:
#     print("hola como estas")
#     numero = int(input("ingrese un numero\n"))
#     if numero%2==0 :
#         print("es un numero par")
#         bandera = False
#     else:
#         print("es un numero impar")
        
# for x in range(10):
#     numero = int(input("ingrese un numero\n"))
#     if numero%2==0 :
#         print("es un numero par")
#         break
#     else:
#         print("es un numero impar")
while True:
    try:
        numero = int(input("ingrese numero\n"))
        print(f"tu numero es {numero}")
        break
    except:
        print("no existe ese numero")
