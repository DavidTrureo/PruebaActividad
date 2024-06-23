from funktions import *

limpiar()

while True:
    imprimir_menu()
    try:
        print(" ")
        opcion = int(input("Ingrese Opción:\n"))
        if opcion == 1:
            registrar_ciudadano()
        elif opcion == 2:
            buscar_ciudadano()
        elif opcion == 3:
            imprimir_certificados()
        elif opcion == 4:
            salir()
            break
    except:
        print("Opción Ingresada no Existe")

