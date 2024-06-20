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
            print("*** REGISTRO PACIENTES ***")
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
                correo = input("Ingrese Correo Electrónico Válido:\n")
            
            while banderaEdad:
                try:
                    edad = int(input("Ingrese edad de Paciente:\n"))
                    while edad < 0 or edad > 110:
                        edad = int(input("ingrese numeros validos entre 0 y 110 años\n"))        
                    banderaEdad = False
                except:
                    print("Ingrese sólo Numeros")
            
            #Inicio bucle Sexo
            def femenino_o_masculino(valor1, valor2):
                while banderaSexo:
                    entrada = input(f"Elija sexo utilizando '{valor1}' (Femenino) y '{valor2}' (Masculino):\n")
                    if entrada == valor1:
                        return valor1
                    elif entrada == valor2:
                        return valor2
                    else:
                        print("Error. Por favor, elija uno de los valores proporcionados")

            opcionSexo = femenino_o_masculino("f", "m")
            #Fin bucle Sexo
            
            #Inicio bucle Prevision
            def isapre_o_fonasa(valor3, valor4):
                while banderaPrevision:
                    entrada = input(f"Elija entre '{valor3}' y '{valor4}':\n")
                    if entrada == valor3:
                        return valor3
                    elif entrada == valor4:
                        return valor4
                    else:
                        print("Error. Por favor, elija uno de los valores proporcionados")

            opcionPrevision = isapre_o_fonasa("isapre", "fonasa")
            #Fin bucle prevision
            print()
            x = input("*** Paciente Registrado Satisfactoriamente ***")
            
        elif opcion == 2:
            os.system("clear")
            print("*** ATENCION PACIENTES ***")
            print()
            nrut = int(input("Ingrese RUT a Consultar:\n"))
            print()
            if nrut == rut:
                print("Paciente Existente en nuestro Sistema")
                print()
                while banderaObservaciones:
                    try: 
                        observaciones = int(input("Desea agregar Observaciones de la Visita? 1.SI 2.NO\n"))
                        while observaciones > 2 or observaciones < 1:
                            observaciones = int(input("Debe seleccionar 1 (si es SI) ó 2 (si es NO)\n"))
                        banderaObservaciones = False
                    except:
                        print("Debe escoger una opción, ingresando 1 ó 2")
                        
                    if observaciones == 1:
                        #print("Ingrese Fecha de Atención")
                        fechaDia = input("Ingrese fecha Atención en el siguiente formato DD/MM/AAAA\n")
                        #fechaMes = int(input("ingrese mes en formato 'MM' (Imgrese Valor entre 1 y 12):\n"))
                        #fechaAno = int(input("ingrese año en formato 'AAAA':\n"))                   
                        observaciones1 = input("Ingrese las Observaciones de Visita del Paciente:\n")
                        
                        print()
                        x=input("*** Observación Registrada Satisfactoriamente ***")
                        
                    elif observaciones == 2:
                        print("*** No se han Registrado Observaciones ***")
                        x=input("Presione Enter para Continuar")    
            else:
                print("Paciente No Existe en nuestros Sistemas")

        elif opcion == 3:
            os.system("clear")
            print("*** CONSULTAR DATOS ***")
            print()
            nrut = int(input("Ingrese RUT a Consultar:\n"))
            if nrut == rut:
                nombreMayusculas = nombre.upper()
                print(f"Nombre: \t\t{nombreMayusculas}")
                direccionMayusculas = direccion.upper()
                print(f"Dirección: \t\t{direccionMayusculas}")
                print(f"Correo: \t\t{correo}")
                print(f"Edad: \t\t\t{edad}")
                if opcionSexo == "f":
                    opcionSexo = "femenino"
                elif opcionSexo == "m":
                    opcionSexo = "masculino"
                sexoMayusculas = opcionSexo.upper()
                print(f"Sexo: \t\t\t{sexoMayusculas}")                
                previsionMayusculas = opcionPrevision.upper()
                print(f"Previsión de Salud: \t{previsionMayusculas}")
                if observaciones == 0 or observaciones == 2:
                    print("Observaciones: \t\tPaciente sin Observaciones")
                else:
                    obserMayuscula = observaciones1.upper()
                    print(f"Observaciones: \t\t{fechaDia}\n \t\t\t{obserMayuscula}")
                #print(f"Observaciones: \t\t{observaciones1}")
                print()
                x = input("Presione Enter para Continuar")
            else:
                #os.system("clear")
                print("Rut Paciente no Existe")
                x = input("h")
                time.sleep (4)
                                
        elif opcion == 4:
            print("Usted ha salido del Sistema")
            time.sleep(3)
            break
    except:
        print("Opción no Valida, Elija una opción")
        time.sleep(3)
        

        