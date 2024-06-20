#Código 2° Evaluación David Trureo
import time, os
usuario = "assault"
contraseña = "assault"
banderaId = True
banderaNivel = True
banderaPuntos = True
banderaId2 = True

while True:
    os.system("clear")
    print("\t\t*** Sistema de Gestión de Jugadores - 'Epic Quest' ***")
    print()
    print("1) Registrar Jugador")
    print("2) Consultar Datos de Jugador")
    print("3) Salir")
    print()
    try:
        opcion = int(input("Ingrese una Opción:\n"))
        if opcion == 1:
            os.system("clear")
            print("\t\t*** Registrar Jugador ***")
            print()
            nombre= input("Ingrese Nombre:\n")
            while nombre == "" or nombre == " ":
                nombre= input("Ingrese Nombre, este campo no puede ir vacío:\n")            
            while banderaId:
                try:
                    idJugador = int(input("Ingrese ID de Jugador (Valor entre 10000 y 99999):\n"))
                    while idJugador <= 9999 or idJugador >= 100000:
                        idJugador = int(input("Ingrese ID de Jugador (Valor entre 10000 y 99999):\n"))
                    banderaId = False
                except:
                    print("Ingrese sólo números")
            while banderaNivel:
                try:
                    nivelJugador = int(input("Ingrese Nivel de Jugador (Valor entre 1 y 100):\n"))
                    while nivelJugador < 1 or nivelJugador > 100:
                        nivelJugador = int(input("Ingrese Nivel de Jugador (Valor entre 1 y 100):\n"))
                    banderaNivel = False
                except:
                    print("Ingrese sólo números")
            correo = input("Ingrese Correo:\n")
            while "@" not in correo:
                correo = input("Ingrese Correo válido (debe incluir '@' :\n")
            rol = input("Ingrese Rol de Jugador, debe elegir entre 'objective' - 'slayer' - 'support' - 'anchor':\n")
            while rol != "objective" and rol != "slayer" and rol != "support" and rol != "anchor":
                rol = input("Ingrese Rol de Jugador, debe elegir entre 'objective' - 'slayer' - 'support' - 'anchor':\n")
            while banderaPuntos:
                try:
                    puntos = int(input("Ingrese Puntos de Experiencia Acumulados:\n"))
                    while puntos < 1:
                        puntos = int(input("Ingrese Puntos de Experiencia Acumulados:\n"))
                    banderaPuntos = False    
                except:
                    print("Ingrese sólo números")
            print()
            print("\t\t*** Jugador Registrado Exitosamente ***")
            time.sleep(3)
        elif opcion == 2:
            os.system("clear")
            print("\t\t*** Consultar Datos de Jugador ***")
            print()
            print("\t(Para Acceder deberá ingresar sus Credenciales)")
            print()
            username = input("Ingrese Usuario:\n")
            password = input("Ingrese Contraseña:\n")
            if (usuario == username and contraseña == password):
                while banderaId2:
                    try:
                        idJuga2 = int(input("Ingrese ID de Jugador a Consultar:\n"))
                        while idJuga2 != idJugador:
                            idJuga2 = int(input("Ingrese ID de Jugador a Consultar:\n"))
                        banderaId2 = False
                    except:
                        print("*** Ingrese sólo números ***")
                        print()
                os.system("clear")
                print("\t\t*** Datos del Jugador Consultado ***")
                print()
                print(f"Nombre: \t\t{nombre}")
                print(f"ID: \t\t\t{idJugador}")
                print(f"Nivel: \t\t\t{nivelJugador}")
                print(f"Correo: \t\t{correo}")
                print(f"Rol Jugador: \t\t{rol}")
                print(f"Puntos Acumulados: \t{puntos}")
                print()
                if nivelJugador > 50 and puntos > 1000:
                    print("\t\t*** Es un Jugador Experimentado ***")
                else:
                    print("\t\t*** Jugador Novato ***")
                print()
                x=input("Presione Enter para continuar")
            else:
                print("*** Usuario y/o Contraseña Incorrectos ***")
                time.sleep(3)
        elif opcion == 3:
            os.system("clear")
            print("*** Ha salido del Sistema ***")
            print()
            break
    except:
        print("Opción no válida")
print("Bye")
        