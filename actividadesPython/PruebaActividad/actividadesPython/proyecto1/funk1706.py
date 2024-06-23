import os
import time

alumnos = []

def limpiar_pantalla():
    os.system("clear")

#la ocuparemos n veces que necesitemos solicitar alguna variable y que no venga vacia
def obtener_campo_no_vacio(campo):
    valor = input(f"Ingrese {campo}: \n")
    while not valor:
        valor = input(f"{campo} no puede guardarse vacío. Ingrese {campo} nuevamente: \n")
    return valor

def obtener_id():
    info = input("Ingrese grado Académico Basica o Media\n").lower()
    if info == 'AB'
        info_id = 'AB'


def registrar_alumno():
    while True:
        limpiar_pantalla()
        print("Registrar Alumno")
        id = obtener_id()
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
