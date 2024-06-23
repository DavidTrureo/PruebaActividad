import os, time

banderaRut = True
banderaEdad = True
banderaPrevision = True
banderaSexo = True
banderaObservaciones = True
observaciones = 0

while True:
    os.system("clear")
    print("*** CENTRO MEDICO DUOC ***")
    print()
    print("1) Registrar Paciente")
    print("2) Atención Paciente")
    print("3) Consultar Datos Paciente")
    print("4) Salir")
    print()
    try:
        opcion = int(input("Ingrese Opción\n"))
        if opcion == 1:
            os.system("clear")
            print("*** REGISTRAR PACIENTE ***")
            print()
            while banderaRut:
                try:
                    rut = int(input("Ingrese RUT (sin puntos ni Dígito Verificador):\n"))
                    while rut < 5000000 or rut > 99999999:
                        rut = int(input("Ingrese Rut Válido, entre 5000000 y 99999999\n"))
                        banderaRut = False
                except:
                    print("Ingrese sólo numeros")

            nombre = input("Ingrese Nombre:\n")
            while nombre == "" or nombre == " ":
                nombre = input("Ingrese Dirección Válida (Este Campo no debe ir Vacío):\n")
                                    
            direccion = input("Ingrese Dirección:\n")
            while direccion == "" or direccion == " ":
                direccion = input("Ingrese Dirección Válida (Este Campo no debe ir Vacío):\n")
                    
            correo = input("Ingrese Correo Electrónico:\n")
            while "@" not in correo:
                correo = input("Ingrese Correo Electrónico Válido (inlcuyendo el @):\n")
            
            while banderaEdad:
                try:
                    edad = int(input("Ingrese edad de Paciente:\n"))
                    while edad < 0 or edad > 110:
                        edad = int(input("ingrese numeros validos entre 0 y 110 años\n"))        
                        banderaEdad = False
                except:
                    print("Ingrese sólo Números")
            
            sexo = input("Ingrese su Sexo ('f' ó 'm')\n")
            while sexo != "f" and sexo != "F" and sexo != "m" and sexo != "M":
                correo = input("Ingrese su Sexo ('f' ó 'm')\n")
            
            prevision = input("Ingrese su Previsión de Salud 'isapre' o 'fonasa'\n")
            while prevision != "isapre" and prevision != "fonasa":
                prevision = input("Ingrese su Previsión de Salud 'isapre' ó 'fonasa'\n")                
            print()
            print("*** Paciente Registrado Satisfactoriamente ***")
            time.sleep(3)
            
        elif opcion == 2:
            os.system("clear")
            print("*** ATENCION PACIENTES ***")
            print()
            nrut = int(input("Ingrese RUT a Consultar:\n"))
            print()
            if nrut == rut: #Busca si el valor ingresado en "nrut" es igual al valor almacenado en rut
                print("Paciente Existente en nuestro Sistema")
                print()
                while banderaObservaciones: #banderaObservaciones tiene almacenado el valor "True"
                    try: #quiere decir "intentar" y en este caso mantendrá en un loop a la variable observaciones hasta que se ingrese un valor valido
                        observaciones = int(input("Desea agregar Observaciones de la Visita? 1.SI 2.NO\n"))
                        while observaciones > 2 or observaciones < 1:
                            observaciones = int(input("Debe seleccionar 1 (si es SI) ó 2 (si es NO)\n"))
                            banderaObservaciones = False
                    except:
                        print("Debe escoger una opción, ingresando 1 ó 2")
                        
                    if observaciones == 1:
                        fechaDia = input("Ingrese fecha Atención en el siguiente formato DD/MM/AAAA\n")            
                        observaciones1 = input("Ingrese las Observaciones de Visita del Paciente:\n")
                        print()
                        print("*** Observación Registrada Satisfactoriamente ***")
                        time.sleep(3)
                        
                    elif observaciones == 2:
                        print("*** No se han Registrado Observaciones ***")
                        x=input("Presione Enter para Continuar")    
            else:
                print("Paciente No Existe en nuestros Sistemas")

        elif opcion == 3:
            os.system("clear")
            print("*** CONSULTAR DATOS ***")
            print()
            nrut = int(input("Ingrese RUT a Consultar:\nRUT:\t\t\t"))
            if nrut == rut:
                nombreMayusculas = nombre.upper()
                print(f"Nombre: \t\t{nombreMayusculas}")
                direccionMayusculas = direccion.upper()
                print(f"Dirección: \t\t{direccionMayusculas}")
                print(f"Correo: \t\t{correo}")
                print(f"Edad: \t\t\t{edad}")
                if sexo == "f":
                    sexo = "femenino"
                elif sexo == "m":
                    sexo = "masculino"
                sexoMayusculas = sexo.upper()
                print(f"Sexo: \t\t\t{sexoMayusculas}")                               
                previsionMayusculas = prevision.upper()
                print(f"Previsión de Salud: \t{previsionMayusculas}")
                
                if observaciones == 0 or observaciones == 2:
                    print("Observaciones: \t\tPaciente sin Observaciones")
                else:
                    obserMayuscula = observaciones1.upper()
                    print(f"Observaciones: \t\t{fechaDia}\n \t\t\t{obserMayuscula}")

                print()
                x = input("Presione Enter para Continuar")
            else:
                print("Rut Paciente no Existe")
                x = input("")
                time.sleep (4)
                                
        elif opcion == 4:
            print("Usted ha salido del Sistema")
            time.sleep(3)
            break
    except:
        print("Opción no Valida, Elija una opción")
        time.sleep(3)
        

        