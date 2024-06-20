import time, os
os.system("clear")
usuario = "seller"
contraseña = "123"
banderaReserva = True
banderaAcompanantes = True
banderaEdad = True

while True:
    os.system("clear")
    print("\t \t*** Bienvenido a Hotel 'Paradise Dreams' ***\n")
    print("1. Registrar Huésped")
    print("2. Consultar Datos del Huésped")
    print("3. Salir")
    print()
    try:
        opcion = int(input("Ingrese una Opción\n"))
        if opcion == 1:
            os.system("clear")
            while banderaReserva:
                try:
                    reserva = int(input("Ingrese N° Reserva entre 1000 y 9999\n"))
                    while reserva < 1000 or reserva > 9999:
                        reserva = int(input("Ingrese N° Reserva entre 1000 y 9999\n"))
                    banderaReserva = False
                except ValueError:
                    print("Ingrese sólo números")
                  
            nombre = input("Ingrese Nombre de Huésped\n")
            while nombre == "":
                nombre = input("Ingrese un nombre de huésped, este campo no puede ir vacío\n")
                      
            direccion = input("Ingrese Dirección\n")
            while direccion == "":
                direccion = input("Ingrese Dirección, este campo no puede ir vacío\n")
                      
            correo = input("Ingrese Correo Electrónico\n")
            while "@" not in correo:
                correo = input("Ingrese un correo Electrónico Válido\n")
            
            while banderaEdad:
                try:
                    edad = int(input("Ingrese Edad (Entre 18 y 120 años)\n"))
                    while edad < 18 or edad > 120:
                        edad = int(input("ingrese edad (Entre 18 y 120 años)\n"))
                    banderaEdad = False
                except:
                    print("Debe ingresar un número")
            
            while banderaAcompanantes:
                try:          
                    acompanantes = int(input("Ingrese N° de Acompañantes\n"))
                    while acompanantes < 0:
                        acompanantes = int(input("Ingrese un número de acompañantes válido\n"))
                    banderaAcompanantes = False
                except:
                    print("Debe ingresar un valor numérico, si no hay acompañantes debe ingresar '0' (Cero)")
            
            print("*** Huésped registrado satisfactoriamente ***")
            time.sleep (4)
            
        elif opcion == 2:
            os.system("clear")
            print("CONSULTA RESERVAS")
            username = input("Ingrese Usuario\n")
            psswrd = input("Ingrese Password\n")
            if(usuario == username and contraseña == psswrd):
                nreserva = int(input("Ingrese N° de Reserva a Consultar\n"))
                if nreserva == reserva:
                    print(f"Nombre: {nombre}")
                    print(f"Dirección:  {direccion}")
                    print(f"Correo: {correo}")
                    print(f"Edad: {edad}")
                    print(f"N° acompañantes: {acompanantes}")
                    if acompanantes > 3:
                        print("Huésped con demasiados acompañantes")
                    else:
                        print("Huésped dentro de límite de acompañantes")
                    print()
                    x=input("Presione Enter para Continuar")
            else:
                os.system("clear")
                print("Usuario y/o Contraseña no existen")
                time.sleep (4)
                
        elif opcion == 3:
            os.system("clear")
            print("Gracias por preferir Hotel 'Paradise Dreams'")
            print()
            break    
    except:
        print("Opción no Valida, hasta luego")
        
print("Usted ha Salido del Sistema")