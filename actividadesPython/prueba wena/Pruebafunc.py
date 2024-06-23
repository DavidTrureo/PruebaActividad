import random
contador_id=1
estudiantes=[]
def menu():
    print("MENU")
    print("(1) Registrar Estudiante")
    print("(2) Buscar Estudiante")
    print("(3) Imprimir Certificados")
    print("(4) Salir\n")

def salir():
    print("")
    print("Saliendo del programa...")
    print("Camilo Romero.")
    print("Version 1.0")

def obtener_id(contador_id):
    while True:
        info = input("ingrese grado academico (basica o media): ").lower()
        if info=="basica":
            id_final = '0' + str(contador_id) + "-AB"
            break
        elif info=="media":
            id_final = '0' + str(contador_id) + "-AM"
            break
        else:
            print("debe ingresar basica o media\n")
    return id_final

def obtener_nombre():
    while True:
        nombre=input("ingrese nombre: ")
        if nombre!="" and nombre!=" " and not "  " in nombre:
            if len(nombre)>=5:
                break
            else:
                print("nombre debe tener minimo 5 caracteres\n")
        else:
            print("nombre no puede estar vacio\n")
    return nombre

def obtener_edad():
    while True:
        try:
            edad=int(input("ingrese edad: "))
            if edad>=12 and edad<=18:
                print(edad)
                break
            else:
                print("edad debe ser mayor o igual a 12 y menor o igual a 18\n")
        except:
            print("edad debe ser un valor entero\n")
    return edad

def registar_estudiante():
    contador_id=1
    while True:
        id_estudiante=obtener_id(contador_id)
        contador_id+=1
        nombre=obtener_nombre()
        edad=obtener_edad()
        asistencia=random.randint(1,100)
        nota=random.randint(10,70)
        conducta=random.randint(1,100)
        estudiante=[id_estudiante,nombre,edad,asistencia,nota,conducta]
        estudiantes.append(estudiante)
        print(estudiantes)
        agregar = input("Desea agregar otro estudiante? si para coninuar...\n").lower()
        if agregar == "si":
            continue
        else:
            print("volviendo al menu principal...\n")
            break

def buscar_estudiante():
    id_buscar = input("ingrese id del alumno a buscar\n")
    for estudiante in estudiantes:
        if  estudiante[0] == id_buscar:
            print("ID:", estudiante[0])
            print("NOMBRE:", estudiante[1])
            print("EDAD:", estudiante[2])
            print(f"ASISTENCIA: {estudiante[3]}%")
            print(f"NOTAS: {estudiante[4]/10}")
            print(f"CONDUCTA: {estudiante[5]}/100\n")




def imprimir_certificados():
    while True:
        print("Menu imprimr certificado")
        print("(1) Certificados asistencia")
        print("(2) Certificados nota")
        print("(3) Certificados conducta")
        print("(4) Volver al menu principal")
        opc2 = input("ingrese opcion\n")
        if opc2 == "1":
            id_buscar = input("ingrese id del alumno a buscar\n")
            for estudiante in estudiantes:
                if  estudiante[0] == id_buscar:
                    print("-------CERTIFICADO DE ASISTENCIA-------")
                    print("ID:", estudiante[0])
                    print("NOMBRE:", estudiante[1])
                    print("EDAD:", estudiante[2])
                    if estudiante[3]<70:
                        print(f"La asistencia de {estudiante[1]} es de {estudiante[3]}%")
                        print("REPROBADO POR BAJA ASISTENCIA ")
                        print("---------------------------------------")
                    else:
                        print(f"La asistencia de {estudiante[1]} es de {estudiante[3]}%")
                        print("APROBADO POR BUENA ASISTENCIA")
                        print("---------------------------------------")
        elif opc2 == "2":
            id_buscar = input("ingrese id del alumno a buscar\n")
            for estudiante in estudiantes:
                if  estudiante[0] == id_buscar:
                    print("-------CERTIFICADO DE NOTA-------")
                    print("ID:", estudiante[0])
                    print("NOMBRE:", estudiante[1])
                    print("EDAD:", estudiante[2])
                    if estudiante[4]<40:
                        print(f"La nota de {estudiante[1]} es {estudiante[4]/10}")
                        print("ESTUDIANTE REPROBADO")
                        print("---------------------------------------")
                    else:
                        print(f"La nota de {estudiante[1]} es {estudiante[4]/10}")
                        print("ESTUDIANTE APROBADO")
                        print("---------------------------------------")
        elif opc2 == "3":
            id_buscar = input("ingrese id del alumno a buscar\n")
            for estudiante in estudiantes:
                if  estudiante[0] == id_buscar:
                    print("-------CERTIFICADO DE ASISTENCIA-------")
                    print("ID:", estudiante[0])
                    print("NOMBRE:", estudiante[1])
                    print("EDAD:", estudiante[2])
                    if estudiante[5]<40:
                        print(f"La conducta de {estudiante[1]} es de {estudiante[5]}%")
                        print("EL ESTUDIANTE TIENE MALA CONDUCTA")
                        print("---------------------------------------")
                    elif estudiante[5]>=40 and estudiante[5]<=80:
                        print(f"La conducta de {estudiante[1]} es de {estudiante[5]}%")
                        print("EL ESTUDIANTE TIENE BUENA CONDUCTA")
                        print("---------------------------------------")
                    else:
                        print(f"La conducta de {estudiante[1]} es de {estudiante[5]}%")
                        print("EL ESTUDIANTE TIENE EXELENTE CONDUCTA")
                        print("---------------------------------------")
        elif opc2 == "4":
            print("Saliendo al menu principal...\n")
            break
        else:
            print("opcion ingresada no es valida")
            print("volviendo al menu principal...\n")
            break