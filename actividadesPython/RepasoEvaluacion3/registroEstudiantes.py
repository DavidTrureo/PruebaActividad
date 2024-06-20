from functions1 import *

limpiar()

while True:
    imprimir_menu()
    try:
        opcion = int(input("ingrese opcion\n"))
        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            buscar_estudiante()
        elif opcion == 3:
            print("imprimir certificados")
        elif opcion == 4:
            print("descargar archivos (lo vemos despues de eva 3)")
        elif opcion == 5:
            salir()
            break
    except:
        print("opcion ingresada no existe")

