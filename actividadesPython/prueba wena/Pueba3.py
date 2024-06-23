from Pruebafunc import *
banderaMenu=True
while banderaMenu:
    menu()
    opc=input("ingrese una opcion del menu: ")
    if opc=="1":
        registar_estudiante()
    elif opc=="2":
        buscar_estudiante()
    elif opc=="3":
        imprimir_certificados()
    elif opc=="4":
        salir()
        banderaMenu=False
    else:
        print("opcion del menu no valida\n")
