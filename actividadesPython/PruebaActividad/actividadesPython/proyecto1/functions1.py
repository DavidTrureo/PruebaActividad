import random, time, os

estudiantes = []
#id autoincremental, debe venir en formato 01-AB o 01-AM
def limpiar():
    os.system("clear")

def obtener_id(contador_ids):
    limpiar()
    info = input("Ingrese grado Académico 'basica' o 'media'\n").lower()
    while info not in ['basica', 'media']:
        info = input("Ingrese grado Académico 'basica' o 'media'\n").lower()
    if info == "basica":
        info_id = 'AB'
    elif info == "media":
        info_id = 'AM'
    id_final = '0' + str(contador_ids)+ "-" + info_id
    contador_ids += 1
    return id_final

def obtener_nombre():
    nombre_estudiante = input("Ingrese Nombre y Apellido:\n")
    while len(nombre_estudiante) < 5:
        nombre_estudiante = input("Ingrese Nombre y Apellido:\n")
    return nombre_estudiante

def obtener_edad():
    while True:
        try:
            edad_estudiante = int(input("Ingrese Edad:\n"))
            while not edad_estudiante or edad_estudiante < 12 or edad_estudiante > 18:
                edad_estudiante = int(input("Ingrese Edad:\n"))
            break
        except:
            print("Campo EDAD solo acepta valores numéricos")
    return edad_estudiante

def registrar_estudiante():
    limpiar()
    contador_ids = 1
    while True:
        id_estudiante = obtener_id(contador_ids)
        contador_ids += 1
        nombre = obtener_nombre()
        edad = obtener_edad()
        asistencia = random.randint(1,100)
        nota = random.randint(10,70)
        conducta = random.randint(1,100)
        estudiante = [id_estudiante, nombre, edad, asistencia, nota, conducta]
        estudiantes.append(estudiante)
        print(" ")
        print(estudiantes)
        print(" ")
        try:
            otro_estudiante = int(input("Desea agregar otro Estudiante? 1.si  2.no:\n"))
            while not otro_estudiante:
                otro_estudiante = input("Desea agregar otro Estudiante? 'si' o 'no':\n").lower()
                while otro_estudiante not in ['si', 'no']:
                    otro_estudiante = input("Desea agregar otro Estudiante? 'si' o 'no':\n").lower()
            if otro_estudiante !=2:
                continue
            else:
                break

        except:
            print("Sólo acepta como opción 1.si  y 2.no")

def imprimir_menu():
    limpiar()
    print("*** SISTEMA DE REGISTRO DE ESTUDIANTES ***")
    print(" ")
    print("1) Registrar Estudiante")
    print("2) Buscar Estudiante")
    #print("3) Imprimir Estudiante")
    print("3) Imprimir Certificados")
    print("4) Salir")

def salir():
    limpiar()
    print("Saliendo.")
    time.sleep(1)
    limpiar()
    print("Saliendo..")
    time.sleep(1)
    limpiar()
    print("Saliendo...")
    time.sleep(1)

def obtener_campo_no_vacio(campo):
    valor = input(f"Ingrese {campo}:\n")
    while not valor:
        valor = input(f"{campo} no puede guardarse vacío. Ingrese {campo} nuevamente:\n")
    return valor

def buscar_estudiante():
    limpiar()
    print("*** CONSULTAR DATOS DE ALUMNO ***")
    print(" ")
    id_buscar = input("Ingrese ID del Alumno a buscar:\n")
    for estudiante in estudiantes:
        if estudiante[0] == id_buscar:
            print(" ")
            print(f"ID: {estudiante[0]}")
            print(f"Nombre: {estudiante[1]}")
            print(f"Edad: {estudiante[2]}")
            print(f"Asistencia: {estudiante[3]}%")
            print(f"Notas: {estudiante[4]/10}")
            print(f"Conducta: {estudiante[5]}/100\n")
    input("Enter para continuar...")
    
def imprimir_certificados():
    limpiar()
    while True:
        limpiar()
        print("*** MENÚ IMPRIMIR CERTIFICADOS ***")
        print(" ")
        print("1) Certificado de Asistencia")
        print("2) Certificado de Notas")
        print("3) Certificado de Conducta")
        print("4) Volver al Menú Principal")
        print(" ")
        opc2 = input("Ingrese Opción:\n")
        if opc2 == "1":
            limpiar()
            print("-------CERTIFICADO DE ASISTENCIA-------")
            print(" ")
            id_buscar = input("Ingrese ID de Alumno a buscar\n")
            print(" ")
            for estudiante in estudiantes:
                if  estudiante[0] == id_buscar:
                    limpiar()
                    print("-------CERTIFICADO DE ASISTENCIA-------")
                    print(" ")
                    print("ID:", estudiante[0])
                    print("Nombre:", estudiante[1])
                    print("Edad:", estudiante[2])
                    if estudiante[3] < 70:
                        print(f"La Asistencia de {estudiante[1]} es del {estudiante[3]}%")
                        print("REPROBADO POR BAJA ASISTENCIA ")
                        print("---------------------------------------")
                        #input("Enter para continuar...")
                    else:
                        print(f"La Asistencia de {estudiante[1]} es del {estudiante[3]}%")
                        print("APROBADO POR BUENA ASISTENCIA")
                        print("---------------------------------------")
            input("Enter para continuar...")
        elif opc2 == "2":
            limpiar()
            print("*** CERTIFICADO DE NOTAS ***")
            print(" ")
            id_buscar = input("Ingrese ID de Alumno a buscar\n")
            for estudiante in estudiantes:
                if  estudiante[0] == id_buscar:
                    limpiar()
                    print("-------CERTIFICADO DE NOTAS-------")
                    print(" ")
                    print("ID:", estudiante[0])
                    print("Nombre:", estudiante[1])
                    print("Edad:", estudiante[2])
                    if estudiante[4] < 40:
                        print(f"La Nota de {estudiante[1]} es {estudiante[4]/10}")
                        print("ESTUDIANTE REPROBADO")
                        print("---------------------------------------")
                        #x = input("Enter para continuar...")
                    else:
                        print(f"La Nota de {estudiante[1]} es {estudiante[4]/10}")
                        print("ESTUDIANTE APROBADO")
                        print("---------------------------------------")
            input("Enter para continuar...")
        elif opc2 == "3":
            limpiar()
            print("*** CERTIFICADO DE ASISTENCIA ***")
            print(" ")
            id_buscar = input("Ingrese ID de Alumno a buscar\n")
            for estudiante in estudiantes:
                if  estudiante[0] == id_buscar:
                    limpiar()
                    print("-------CERTIFICADO DE ASISTENCIA-------")
                    print(" ")
                    print("ID:", estudiante[0])
                    print("Nombre:", estudiante[1])
                    print("Edad:", estudiante[2])
                    if estudiante[5] < 40:
                        print(f"La Conducta de {estudiante[1]} es del {estudiante[5]}%")
                        print("EL ESTUDIANTE TIENE MALA CONDUCTA")
                        print("---------------------------------------")
                        #x = input("Enter para continuar...")
                    elif estudiante[5] >= 40 and estudiante[5] <= 80:
                        print(f"La Conducta de {estudiante[1]} es del {estudiante[5]}%")
                        print("EL ESTUDIANTE TIENE BUENA CONDUCTA")
                        print("---------------------------------------")
                        #x = input("Enter para continuar...")
                    else:
                        print(f"La Conducta de {estudiante[1]} es del {estudiante[5]}%")
                        print("EL ESTUDIANTE TIENE EXCELENTE CONDUCTA")
                        print("---------------------------------------")
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