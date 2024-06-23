import os
import time

pacientes = []

def limpiar_pantalla():
    os.system("clear")

#sin argumento y sin retorno
def menu_principal():
    limpiar_pantalla()
    print("1) Registrar Paciente")
    print("2) Atencion Paciente")
    print("3) Gestionar Paciente")
    print("4) Salir")

def obtener_rut():
    while True:
        rutS = input("Ingrese RUT: \n")
        while not rutS: #while rutS == "" and rutS == " "
            rutS = input("Ingrese RUT, no debe venir vacío: \n")
        try:
            rut = int(rutS)
            while rut < 5000000 or rut > 30000000:
                rut = int(input("Ingrese RUT, debe estar en rango 5M Y 30M \n"))
            return rut
        except:
            print("En campo RUT, no se aceptan caracteres.")

#la ocuparemos n veces que necesitemos solicitar alguna variable y que no venga vacia
def obtener_campo_no_vacio(campo):
    valor = input(f"Ingrese {campo}: \n")
    while not valor:
        valor = input(f"{campo} no puede guardarse vacío. Ingrese {campo} nuevamente: \n")
    return valor

def obtener_correo():
    correo = input("ingrese correo\n")
    while '@' not in correo:
        correo = input("ingrese correo, debe ingresar al menos un @\n")
    return correo

def obtener_edad():
    while True:
        edadS = input("ingrese edad\n")
        while not edadS:
            edadS = input("ingrese edad, no debe venir vacio\n")
        try:
            edad = int(edadS)
            while edad < 0 or edad > 110:
                edad = int(input("ingrese valor de edad, entre 0 y 110\n"))
            return edad
        except:
            print("para campo edad, solo se permiten campos tipo numericos")

def obtener_sexo():
    sexo = input("ingrese sexo\n").lower()
    while sexo not in ['f', 'm']: # if sexo != 'm' and sexo != 'f':
        sexo = input("ingrese sexo, opciones: m o f\n").lower()
    return sexo

def obtener_prevision():
    prevision = input("ingrese su prevision\n").lower()
    while prevision not in ['fonasa', 'isapre']:
        prevision = input("ingrese su prevision\n").lower()
    return prevision

def registrar_paciente():
    while True:
        limpiar_pantalla()
        print("Registrar Paciente")
        rut = obtener_rut()
        nombre = obtener_campo_no_vacio("nombre")
        direccion = obtener_campo_no_vacio("direccion")
        correo = obtener_correo()
        edad = obtener_edad()
        sexo = obtener_sexo()
        prevision = obtener_prevision()
        paciente = [rut, nombre, direccion, correo, edad, sexo, prevision]
        pacientes.append(paciente)
        agregar = int(input("Desea agregar otro paciente?   1.Si   2.No\n"))
        if agregar == 1:
            continue
        elif agregar == 2:
            break
    print(paciente)
    input("enter para continuar...")

def atencion_paciente():
    limpiar_pantalla()
    print("Atencion Paciente")
    rut_buscar = int(input("ingrese rut del paciente\n"))
    for paciente in pacientes:
        if paciente[0] == rut_buscar:
            print(f"Adelante {paciente[1].capitalize()}")
            registro = input("cual es el motivo de su consulta\n")
            while not registro:
                registro = input("cual es el motivo de su consulta, campo no puede venir vacio\n")
            paciente.append(registro)
            print(paciente)
            input("enter para continuar...")
        else:
            print("segun nuestros registros, no existe paciente")

def gestionar_paciente():
    while True:
        limpiar_pantalla()
        print("1) Consultar datos paciente")
        print("2) Modificar datos paciente")
        print("3) Eliminar paciente")
        print("4) Volver al menu principal")
        try:
            opcion2 = int(input("ingrese opcion\n"))
            if opcion2 == 1:
                consultar_datos()
            elif opcion2 == 2:
                print("")
            elif opcion2 == 3:
                eliminar_datos()
            elif opcion2 == 4:
                print("Saliendo al menu principal...")
                time.sleep(1)
                break
        except:
            print("opcion ingresada no es valida")

def consultar_datos():
    limpiar_pantalla()
    print("Consultar datos paciente")
    rut_buscar = int(input("ingrese rut del paciente a buscar\n"))
    for paciente in pacientes:
        if paciente[0] == rut_buscar:
            print(f"RUT: {paciente[0]}")
            print(f"NOMBRE: {paciente[1]}")
            print(f"DIRECCION: {paciente[2]}")
            print(f"CORREO: {paciente[3]}")
            print(f"EDAD: {paciente[4]}")
            print(f"SEXO: {paciente[5]}")
            print(f"PREVISION: {paciente[6]}")
            print(f"REGISTRO: {paciente[7]}")
            try:
                print(f"REGISTRO: {paciente[7]}")
            except:
                print(f"REGISTRO: no existe ficha para cliente {paciente[0]}")
    input("enter para continuar...")

def eliminar_datos():
    limpiar_pantalla()
    print("Eliminar Paciente")
    rut_eliminar = int(input("ingrese rut de paciente para eliminar\n"))
    for paciente in pacientes:
        if paciente[0] == rut_eliminar:
            #quien es el paciente
            pacientes.remove(paciente)
        else:
            print(f"segun nuestros registros, el rut {rut_eliminar} no existe")