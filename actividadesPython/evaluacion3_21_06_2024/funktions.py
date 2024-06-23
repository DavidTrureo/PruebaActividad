import random, time, os, datetime
ciudadanos = []

def limpiar():
    os.system("clear")
    
def obtener_nif(contador_ids):
    limpiar()
    info = input("Ingrese Ciudad 'madrid', 'barcelona', 'sevilla', 'xxx'\n").lower()
    while info not in ['madrid', 'barcelona', 'sevilla', 'xxx']:
        info = input("Ingrese Ciudad 'madrid', 'barcelona', 'sevilla', 'xxx'\n").lower()
    if info == "madrid":
        info_id = 'MAD'
    elif info == "barcelona":
        info_id = 'BAR'
    elif info == "sevilla":
        info_id = 'SEV'
    elif info == "xxx":
        info_id = 'XXX'
    id_final = '0000000' + str(contador_ids)+ "-" + info_id
    contador_ids += 1
    return id_final

def obtener_nombre():
    nombre_ciudadano = input("Ingrese Nombre y Apellido:\n")
    while len(nombre_ciudadano) < 8:
        nombre_ciudadano = input("Ingrese Nombre y Apellido:\n")
    return nombre_ciudadano

def obtener_nacionalidad():
    nacionalidad_ciudadano = input("Ingrese Nacionalidad:\n")
    while len(nacionalidad_ciudadano) < 4:
        nacionalidad_ciudadano = input("Ingrese Nacionalidad:\n")
    return nacionalidad_ciudadano

def obtener_edad():
    while True:
        try:
            edad_ciudadano = int(input("Ingrese Edad:\n"))
            while not edad_ciudadano >= 15: #or edad_ciudadano < 12 or edad_estudiante > 18:
                edad_ciudadano = int(input("Ingrese Edad, debe ser igual o mayor a 15 años:\n"))
            break
        except:
            print("Campo EDAD solo acepta valores numéricos")
    return edad_ciudadano

def obtener_ano_nacimiento(edad):
    ano_actual = datetime.datetime.now().year
    ano_nacimiento = ano_actual - edad
    return ano_nacimiento

def registrar_ciudadano():
    limpiar()
    contador_ids = 1
    while True:
        nif_ciudadano = obtener_nif(contador_ids)
        contador_ids += 1
        nombre = obtener_nombre()
        nacionalidad = obtener_nacionalidad()
        edad = obtener_edad()
        ano_nacimiento = obtener_ano_nacimiento(edad)
        opciones = ["casado", "soltero", "viudo", "separado"]
        estado_conyugal = random.choice(opciones)
        salario_mensual = random.randint(100000,10000000)
        ciudadano = [nif_ciudadano, nombre, nacionalidad, edad, ano_nacimiento, estado_conyugal, salario_mensual]
        ciudadanos.append(ciudadano)
        print(" ")
        print(ciudadanos)
        print(" ")
        try:
            otro_ciudadano = int(input("Desea agregar otro Ciudadano? 1.si  2.no:\n"))
            while not otro_ciudadano:
                otro_ciudadano = input("Desea agregar otro Ciudadano? 'si' o 'no':\n").lower()
                while otro_ciudadano not in ['si', 'no']:
                    otro_ciudadano = input("Desea agregar otro Ciudadano? 'si' o 'no':\n").lower()
            if otro_ciudadano !=2:
                continue
            else:
                break
        except:
            print("Sólo acepta como opción 1.si  y 2.no")

def imprimir_menu():
    limpiar()
    print("*** SISTEMA REGISTRO DE CIUDADANOS ***")
    print(" ")
    print("1) Registrar Ciudadano")
    print("2) Buscar Ciudadano")
    print("3) Imprimir Certificados")
    print("4) Salir")

def salir():
    limpiar()
    print("Saliendo.")
    print(" ")
    print("Powered by David Trureo")
    print("Version 2.0")
    time.sleep(1)
    limpiar()
    print("Saliendo..")
    print(" ")
    print("Powered by David Trureo")
    print("Version 2.0")
    time.sleep(1)
    limpiar()
    print("Saliendo...")
    print(" ")
    print("Powered by David Trureo")
    print("Version 2.0")
    time.sleep(1)

def buscar_ciudadano():
    limpiar()
    print("*** CONSULTAR DATOS DE CIUDADANO ***")
    print(" ")
    nif_buscar = input("Ingrese NIF del Ciudadano a buscar:\n")
    for ciudadano in ciudadanos:
        if ciudadano[0] == nif_buscar:
            print(" ")
            print(f"NIF: {ciudadano[0]}")
            print(f"Nombre: {ciudadano[1]}")
            print(f"Nacionalidad: {ciudadano[2]}")
            print(f"Edad: {ciudadano[3]}")
            print(f"Año Nacimiento: {ciudadano[4]}")
            print(f"Estado Conyugal: {ciudadano[5]}")
            print(f"Salario Mensual: {ciudadano[6]} Euros")
            print(" ")
    input("Enter para continuar...")
    
def imprimir_certificados():
    limpiar()
    while True:
        limpiar()
        print("*** MENÚ IMPRIMIR CERTIFICADOS ***")
        print(" ")
        print("1) Certificado de Nacimiento")
        print("2) Certificado de Estado Conyugal")
        print("3) Certificado de Salario Mensual")
        print("4) Volver al Menú Principal")
        print(" ")
        opc2 = input("Ingrese Opción:\n")
        if opc2 == "1":
            limpiar()
            print("****** CERTIFICADO DE NACIMIENTO ******")
            print(" ")
            nif_buscar = input("Ingrese NIF de Ciudadano:\n")
            print(" ")
            for ciudadano in ciudadanos:
                if  ciudadano[0] == nif_buscar:
                    limpiar()
                    print("****** CERTIFICADO DE NACIMIENTO ******")
                    print(" ")
                    print("NIF:", ciudadano[0])
                    print("Nombre:", ciudadano[1])
                    print("Nacionalidad:", ciudadano[2])
                    print("Edad:", ciudadano[3])
                    print(" ")
                    print(f"Certifico que Don(a) {ciudadano[1]} nació en el año '{ciudadano[4]}'")
                    print(" ")
                    print("****************************************")
                    print(" ")
            input("Enter para continuar...")
        elif opc2 == "2":
            limpiar()
            print("****** CERTIFICADO DE ESTADO CONYUGAL ******")
            print(" ")
            nif_buscar = input("Ingrese NIF de Ciudadano:\n")
            for ciudadano in ciudadanos:
                if  ciudadano[0] == nif_buscar:
                    limpiar()
                    print("****** CERTIFICADO DE ESTADO CONYUGAL ******")
                    print(" ")
                    print("NIF:", ciudadano[0])
                    print("Nombre:", ciudadano[1])
                    print("Nacionalidad:", ciudadano[2])
                    print("Edad:", ciudadano[3])
                    print(" ")
                    print(f"Certifico que el Estado Conyugal de {ciudadano[1]} es '{ciudadano[5]}'")
                    print(" ")
                    print("****************************************")
                    print(" ")
            input("Enter para continuar...")
        elif opc2 == "3":
            limpiar()
            print("****** CERTIFICADO DE SALARIO MENSUAL ******")
            print(" ")
            nif_buscar = input("Ingrese NIF de Ciudadano:\n")
            for ciudadano in ciudadanos:
                if ciudadano[0] == nif_buscar:
                    limpiar()
                    print("****** CERTIFICADO DE SALARIO MENSUAL ******")
                    print(" ")
                    print("NIF:", ciudadano[0])
                    print("Nombre:", ciudadano[1])
                    print("Nacionalidad:", ciudadano[2])
                    print("Edad:", ciudadano[3])
                    print(" ")
                    print(f"Certifico que el Salario Mensual de Don(a) {ciudadano[1]} es de '{ciudadano[6]}' Euros")
                    print(" ")
                    print("****************************************")
                    print(" ")
            input("Enter para continuar...")
        elif opc2 == "4":
            print("Saliendo al menu principal...\n")
            time.sleep(1)
            break
        else:
            print("Opción Ingresada no es Válida")
            print("Volviendo al Menú Principal...\n")
            time.sleep(1)
            break