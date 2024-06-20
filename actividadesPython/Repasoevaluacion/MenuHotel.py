import os, time

os.system("clear")
nombre = ""
direc = ""
user_admin = "Admin"
passw_admin = "12345"
banMenu1 = True
while banMenu1:
    print("\n**********Paradise Dreams**********")
    print("---Sistema de gestión de huesped---")
    print("1) Registrar Huesped")
    print("2) Consultar Datos de Huésped")
    print("3) Salir")
    try:
        opc1 = int(input("Ingrese la opción: "))
        if opc1 == 1:
            nombre = input("\nIngrese su nombre: ")
            while nombre == "" or nombre == " ":
                nombre = input("\nIngrese un nombre válido: ")
                
            direc = input("\nIngrese su dirección: ")
            while direc == "" or direc == " ":
                direc = input("\nIngrese una dirección válida: ")
            
            try:
                banReser = True
                while banReser:
                    num_res = int(input("\nIngrese su número de reserva (De 1000 a 9999): "))
                    if num_res > 999 and num_res < 10000:
                        print("\n¡Número de reserva registrado exitosamente!")
                        banReser = False
                    else:
                        os.system("cls")
                        print("El número de reserva no es válido, intente nuevamente.")
            except:
                print("\nNúmero de reserva no válido, intente con números enteros.")
                
            try:
                banEdad = True
                while banEdad:
                    edad = int(input("\nIngrese su edad (De 18 a 120): "))
                    if edad > 17 and edad < 121:
                        print("\n¡Edad registrada exitosamente!")
                        banEdad = False
                    else:
                        os.system("cls")
                        print("\nLa edad no es válida, intente nuevamente.")
            except:
                print("\nLa edad no es válida, intente con números enteros.")
            
            correo = input("\nIngrese su correo (Debe de tener un @): ")
            while "@" not in correo:
                correo = input("\nIngrese su correo nuevamente (Debe de tener un @): ")
            
            try:
                banAcom = True
                while banAcom:
                    acomp = int(input("\nIngrese el número de acompañantes (Debe ser mayor a 0): "))
                    if acomp >= 0:
                        print("\n¡Número de acompañantes registrado exitosamente!")
                        banAcom = False
                    else:
                        os.system("cls")
                        print("\nEl número de acompañantes no es válido, intente nuevamente.")
            except:
                print("\nEl número de acompañantes no es válido, intente con números enteros mayores o iguales a 0.")
                
        elif opc1 == 2:
            user = input("\nIngrese usuario de admin: ")
            password = input("Ingrese contraseña de admin: ")
            if user == user_admin and password == passw_admin:
                os.system("cls")
                print("\n¡Credenciales confirmadas!")
                if acomp > 3:
                    print("\n--------------Datos de Huesped--------------")
                    print(f"Nombre: {nombre}")
                    print(f"Dirección: {direc}")
                    print(f"Número de reserva: {num_res}")
                    print(f"Edad: {edad}")
                    print(f"Correo electrónico: {correo}")
                    print(f"Número de acompañantes: {acomp}")
                    print("*** Huesped con demasiados acompañantes ***")
                    time.sleep(3)
                else:
                    print("\n------------Datos de Huesped------------")
                    print(f"Nombre: {nombre}")
                    print(f"Dirección: {direc}")
                    print(f"Número de reserva: {num_res}")
                    print(f"Edad: {edad}")
                    print(f"Correo electrónico: {correo}")
                    print(f"Número de acompañantes: {acomp}")
                    print("*** Huesped dentro del límite de acompañantes ***")
                    time.sleep(3)
            else:
                os.system("cls")
                print("\nCredenciales no válidas, intente nuevamente.")
                
        elif opc1 == 3:
            os.system("cls")
            print("\nGracias por preferir Hotel 'Paradise Dreams'")
            banMenu1 = False
        
        else:
            os.system("cls")
            print("\nHa ingresado una opción no válida, intente nuevamente.")
                
    except:
        os.system("cls")
        print("\nHa ingresado una opción inválida.")
