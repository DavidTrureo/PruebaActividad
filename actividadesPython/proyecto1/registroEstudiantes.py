from functions1 import *

limpiar()

while True:
    imprimir_menu()
    try:
        print(" ")
        opcion = int(input("Ingrese Opción:\n"))
        if opcion == 1:
            registrar_estudiante()
        elif opcion == 2:
            buscar_estudiante()
        elif opcion == 3:
            imprimir_certificados()
        # elif opcion == 4:
        #     print("descargar archivos (lo vemos despues de eva 3)")
        elif opcion == 4:
            salir()
            break
    except:
        print("Opción Ingresada no Existe")

