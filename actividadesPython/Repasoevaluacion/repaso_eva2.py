#repaso evaluacion 2 30%
#crear un menu
#opcion tengo que registra un alumno
#validar todos los campos
#opcion 2 tengo que ver el resumen de la ficha
#tengo que validar 1: que el usuario sea admin, 2: que el rut exista en el formulario
#ademas, tengo que condicionar el nme para enviar un mensaje
#opcion salir
import time, os
user = "admin"
password = "admin"
while True:
    os.system("clear")
    print("\t\tSistema de Gestión de Alumnos")
    print("1. Registrar Alumno")
    print("2. Consultar Datos de Alumno")
    print("3. Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            os.system("clear")
            print("REGISTRO ALUMNO")
            #solicitar nombre y validar que no venga vacio
            nombre = input("ingrese su nombre\n")
            while nombre == "":
                nombre = input("ingrese su nombre, no acepta cadena vacia\n")
            #solicitar direccion y validar que no venga vacio
            direccion = input("ingrese su direccion\n")
            while direccion == "":
                direccion = input("ingrese su direccion, no acepta cadena vacia\n")
            #solicitar y validar rut que este entre los valores mencionados
            rut = int(input("ingrese su rut\n"))
            while rut <= 5000000 or rut >= 39999999:
                rut = int(input("ingrese su rut, >= a 5M y =< 39.9M \n"))
            #solicitar edad y validar rangos etarios
            edad = int(input("ingrese edad\n"))
            while edad < 17 or edad >90:
                edad = int(input("ingrese edad\n"))
            #solicitar correo y validar que exista al menos 1 arroba(@)
            correo = input("ingrese su correo\n")
            while '@' not in correo:
                correo = input("ingrese su correo\n")
            #solicitar NEM (debe ser decimal)
            nem = float(input("Ingrese NEM\n"))
            
        elif opcion == 2:
            os.system("clear")
            print("CONSULTA DATOS ALUMNO")
            username = input("ingrese usuario\n")
            psswrd = input("ingrese password\n")
            if(user == username and password == psswrd):
                rut_alumno = int(input("ingrese rut de alumno a buscar\n"))
                if rut_alumno == rut:
                    print(f"Nombre: {nombre}")
                    print("Direccion: ", direccion)
                    print(f"Edad: {edad}")
                    print("Correo: ", correo)
                    print(f"NEM: {nem}")
                    if nem <= 520:
                        print("alumno no cumple con requisitos")
                    else:
                        print("alumno cumple con requisitos")
                else:
                    print("el rut ingresado no existe")
                    time.sleep(3)
                print("pulse tecla para continuar")
                x = input()#que significa esto????
                
        elif opcion == 3:
            os.system("clear")
            print("SALIR")
            break
            
    except:
        print("opcion no existe")
        
    time.sleep(4)
        
print("Ha salido del sistema")