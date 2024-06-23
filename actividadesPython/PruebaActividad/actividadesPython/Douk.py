#repaso evaluacion 2 30%
#crear un menu
#opcion tengo que registrar un alumno
#validar todos los campos
#opcion 2 tengo que ver el resumen de la ficha
#tengo que validar 1: que el usuario se admin, 2: que el rurt exista en el fiormulario
#ademas , tengo que condicionar el NEM para enviar un mensaje
#opcion salir


import time, os
user =admin
P
while True:
    os.system ("clear")
    print("\t\tSistema de Gestión de Alumnos")
    print("1. Registrar Alumno")
    print("2. Consultar Datos de Alumno")
    print("3. Salir")
    Try:
        opcion = int(input("Ingrese una Opción\n"))
        if opcion == 1:
            os.system("clear")
            print("REGISTRO ALUMNO")
            #solicitar nombre y validad que no venga vacío
            
            nombre = input("Ingrese su Nombre\n")
            while nombre == "":
                nombre = input("Ingrese su Nombre, no acepta cadena vacía")
                
            direccion = input("Ingrese su Dirección\n")
            while direccion == "":
                direccion = input("Ingrese su Dirección, no acepta cadena vacía")
                
            rut = input("Ingrese su Rut, sin puntos ni Digito Verificador\n")
            while rut <= 5000000 or rut >= 39999999:
                rut = int(input("Ingrese su Rut, >= 5Millones y =< 39.999.999"))
                
            edad = int(input("Ingrese su Edad\n")
            while edad < 17 or edad > 90:
                edad = int(input("Ingrese su Edad\n"))
                
            #solicitar correo y validar que exista al menos 1 arroba (@)    
            correo = input("Ingrese su Correo\n")
            while "@" not in correo:
                correo = input("Ingrese su Correo, debe incluir "@"")    
                
            #solicitar NEM (debe ser decimal)
            nem = float(input("ingrese NEM\n"))
            
        elif opcion == 2:
            os.system("clear")
            print("Consulta Datos Alumnos")
            username = input("Ingrese Usuario\n")
            password = input("Ingrese Password\n")
            if(user == "username" and password == "password")
                rut_alumno = int(input("Ingrese Rut de alumno a buscar\n"))
                if rut_alumno == rut:
                    print(f"Nombre: {nombre}")
                    print(f"Dirección: {direccion}")
                    print(f"Edad: {edad}")
                    print(f"Correo: {correo}")
                    print(f"Edad: {edad}")
                    print(f"NEM: {nem}")
                    if nem <= 520:
                        print("Alumno no cumple con Requisitos")
                    else:
                        print("Alumno cumple con requisitos")
                
            else:
                print("El rut ingresado no existe")
        
        
        elif opcion == 3:
            os.system("clear")
            print("Salir")
            print("Ha salido del sistema")
            
    except: