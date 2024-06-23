import os, time 

pacientes = []
banderaMenu = True

while banderaMenu:
    os.system("clear")
    print("1) Registrar Paciente")
    print("2) Atencion Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            banderaPaciente = True
            while banderaPaciente:
                banderaRut = True
                banderaEdad = True
                print("Registrar Paciente")
                os.system("clear")
                while banderaRut:
                    rutS = input("ingrese rut\n")
                    while rutS == "":
                        rutS = input("ingrese rut, no debe venir vacio\n")
                    try:
                        rut = int(rutS)
                        while rut < 5000000 or rut > 30000000:
                            rut = int(input("ingrese rut, debe estar en rango 5M Y 30M\n"))
                        banderaRut = False
                    except:
                        print("en campo rut, no se aceptan caracteres")
                nombre = input("ingrese nombre\n")
                while nombre == "":
                    nombre = input("nombre no puede guardarse vacio\n")
                direccion = input("ingrese direccion\n")
                while direccion == "":
                    direccion = input("direccion no puede guardarse vacio\n")
                correo = input("ingrese correo\n")
                while "@" not in correo:
                    correo = input("campo correo debe contener al menos un @\n")
                while banderaEdad:
                    try:
                        edad = int(input("ingrese edad\n"))
                        while edad < 0 or edad > 110:
                            edad = int(input("ingrese edad, entre 0 110\n"))
                        banderaEdad = False
                    except:
                        print("en campo edad no se aceptan caracteres")
                sexo = input("ingrese sexo\n").lower()
                while sexo != 'f' and sexo != 'm':
                    sexo = input("ingrese sexo 'f' o 'm'\n").lower()
                #registro lo creare si el paciente asiste a la consulta
                prevision = input("ingrese su prevision\n").lower()
                while prevision != "fonasa" and prevision != "isapre":
                    prevision = input("ingrese su prevision\n").lower()
                paciente = [rut, nombre, direccion, correo, edad, sexo, prevision]
                pacientes.append(paciente)
                otroPaciente = int(input("deseas agregar otro paciente?  1.Si  2.No\n"))
                if otroPaciente == 1:
                    continue
                else:
                    banderaPaciente = False
                print(pacientes)
                x = input("enter para continuar")
        elif opcion == 2:
            os.system("clear")
            print("Atencion Paciente")
            banderaRut = True
            while banderaRut:
                rutS2 = input("ingrese rut\n")
                while rutS2 == "":
                    rutS2 = input("ingrese rut, no debe venir vacio\n")
                try:
                    rut2 = int(rutS2)
                    while rut2 < 5000000 or rut2 > 30000000:
                        rut2 = int(input("ingrese rut, debe estar en rango 5M Y 30M\n"))
                    banderaRut = False
                except:
                        print("en campo rut, no se aceptan caracteres")
            
            for paciente in pacientes:
                if paciente[0] == rut2:
                    print("adelante ", paciente[1])
                    registro = input("ingresar sintomas\n")
                    while registro == "":
                        registro = input("ingresar sintomas\n")
                    paciente.append(registro)
                    print(paciente)
                    input("enter para continuar")
        elif opcion == 3:
            print("Gestionar Paciente")
            banderaSubMenu = True
            while banderaSubMenu:
                print("1) Consultar datos Paciente")
                print("2) Modificar Paciente")
                print("3) Eliminar Paciente")
                print("4) Regresar Menu Principal")
                try:
                    opcion2 = int(input("ingrese opcion\n"))
                    if opcion2 == 1:
                        print("Consultar datos Paciente")
                        banderaConsultar = True  
                        while banderaConsultar:
                            rutConsultar = input("ingrese rut\n")
                            pacienteEncontrado = None
                            while rutConsultar == "":
                                rutConsultar = input("ingrese rut, no debe venir vacio\n")
                            try:
                                rutConsultarReal = int(rutConsultar)
                                while rutConsultarReal < 5000000 or rutConsultarReal > 30000000:
                                    rutConsultarReal = int(rutConsultar)
                                banderaConsultar = False
                            except:
                                print("en campo rut, no se aceptan caracteres")
                        for paciente in pacientes:
                            if paciente[0] == rutConsultarReal:
                                paciente_encontrado = paciente
                                break
                        if paciente_encontrado:
                            print("paciente encontrado...")
                            print("Rut: ", paciente_encontrado[0])
                            print("Nombre: ", paciente_encontrado[1])
                            print("Direccion: ", paciente_encontrado[2])
                            print("Correo: ", paciente_encontrado[3])
                            print("Edad: ", paciente_encontrado[4])
                            print("Sexo: ", paciente_encontrado[5])
                            print("Prevision: ", paciente_encontrado[6])
                            print("Registro: ", paciente_encontrado[7])  
                        else:
                            print("segun los registros, el rut no existe en nuestra bbdd")    
                        input("enter para continuar...")
                    elif opcion2 == 2:
                        print("2) Modificar Paciente")
                        banderaModificar = True  
                        while banderaModificar:
                            rutModificar = input("ingrese rut\n")
                            pacienteEncontrado = None
                            while rutModificar == "":
                                rutModificar = input("ingrese rut, no debe venir vacio\n")
                            try:
                                rutModificarReal = int(rutModificar)
                                while rutModificarReal < 5000000 or rutModificarReal > 30000000:
                                    rutModificarReal = int(rutModificar)
                                banderaModificar = False
                            except:
                                print("en campo rut, no se aceptan caracteres")
                        for paciente in pacientes:
                            if paciente[0] == rutModificarReal:
                                paciente_editado = paciente
                        if paciente_editado:
                            campo = input("ingrese el campo que desea editar (nombre, direccion, correo, edad, sexo, prevision)")
                            if campo in ['nombre', 'direccion', 'correo', 'edad', 'sexo', 'prevision']:
                                nuevo_valor = input(f"ingrese valor para el campo {campo}")
                                if campo == 'edad':
                                    nuevo_valor = int(nuevo_valor)
                                    paciente_editado[4] = nuevo_valor
                                if campo == 'nombre':
                                    paciente_editado[1] = nuevo_valor
                    elif opcion2 == 3:
                        print("Eliminar Paciente")
                        banderaEliminar = True  
                        while banderaEliminar:
                            rutEliminar = input("ingrese rut\n")
                            pacienteEncontrado = None
                            while rutEliminar == "":
                                rutEliminar = input("ingrese rut, no debe venir vacio\n")
                            try:
                                rutEliminarReal = int(rutEliminar)
                                while rutEliminarReal < 5000000 or rutEliminarReal > 30000000:
                                    rutEliminarReal = int(rutEliminar)
                                banderaEliminar = False
                            except:
                                print("en campo rut, no se aceptan caracteres")
                        for paciente in pacientes:
                            if paciente[0] == rutEliminarReal:
                                try:
                                    pacientes.remove(paciente)
                                    print("paciente eliminado con exito...")
                                    time.sleep(1)
                                except:
                                    print("segun los registros, no existe rut")  
                    elif opcion2 == 4:
                        print("regresando al menu principal...")
                        time.sleep(1)
                        banderaSubMenu = False
                except:
                    print("opcion ingresada no es valida")
                
                
        elif opcion == 4:
            print("Ha salido del sistema…")
            x = input("enter para salir...")
            banderaMenu = False
    except:
        print("opcion no es valida")