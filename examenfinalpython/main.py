from functions import *

while True:
    menu()
    try:
       opcion = int(input("ingrese opcion\n")) 
       if opcion == 1:
           print("Registrar Estudiante")
           registrar_estudiante()
       elif opcion == 2:
           print("Buscar Estudiante")
           mostrar_estudiante()
       elif opcion == 3:
           print("Imprimir Certificados")
           imprimir_certificados()
       elif opcion == 4:
           print("Descargar Archivo")
           descargar_archivo()
       elif opcion == 5:
           print("Salir")
           break
    except:
        print("opcion ingresada no es valida")