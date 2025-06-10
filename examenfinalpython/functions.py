import os
import random
import csv

# Lista global para almacenar los datos de los estudiantes
estudiantes = []


def limpiar_pantalla():
    """Limpia la pantalla de la consola, compatible con Windows, Mac y Linux."""
    if os.name == 'nt':
        os.system('cls')  # Para Windows
    else:
        os.system('clear')  # Para Mac y Linux


def obtener_id():
    """Obtiene, valida y asegura que un ID de estudiante sea único."""
    while True:
        grado = input("Ingrese grado académico ('basica' o 'media'):\n").lower()
        if grado in ['basica', 'media']:
            break
        print("Grado no válido. Intente de nuevo.")

    grado_corto = 'AB' if grado == 'basica' else 'AM'

    while True:
        try:
            id_numero_str = input("Ingrese el número de ID del alumno:\n")
            id_numero = int(id_numero_str)
            if id_numero <= 0:
                print("El ID debe ser un número positivo.")
                continue
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")
            continue

        id_final = id_numero_str + "-" + grado_corto

        id_ya_existe = False
        for estudiante in estudiantes:
            if estudiante[0] == id_final:
                id_ya_existe = True
                break

        if not id_ya_existe:
            return id_final
        else:
            print(f"ERROR: El ID '{id_final}' ya está registrado.")
            print("Por favor, ingrese un número de ID diferente.")


def obtener_nombre():
    """Obtiene y valida el nombre completo del estudiante."""
    while True:
        nombre = input("Ingrese nombre completo del alumno:\n")
        if len(nombre) >= 5 and ' ' in nombre.strip():
            return nombre.title()
        print("Nombre inválido. Debe tener al menos 5 caracteres y un espacio.")


def obtener_edad():
    """Obtiene y valida la edad del estudiante (entre 12 y 18)."""
    while True:
        try:
            edad = int(input("Ingrese edad del alumno (entre 12 y 18):\n"))
            if 12 <= edad <= 18:
                return edad
            else:
                print("La edad debe estar entre 12 y 18 años.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")


def registrar_estudiante():
    """Registra uno o más estudiantes en la lista global."""
    limpiar_pantalla()
    while True:
        print("\n--- Registro de Nuevo Estudiante ---")
        id_estudiante = obtener_id()
        nombre_estudiante = obtener_nombre()
        edad_estudiante = obtener_edad()

        estudiante = [id_estudiante, nombre_estudiante, edad_estudiante]
        estudiantes.append(estudiante)
        print(f"\n¡Estudiante '{nombre_estudiante}' registrado con éxito!")

        otro = input("¿Desea agregar otro estudiante? ('si' o 'no'):\n").lower()
        if otro != 'si':
            break
        limpiar_pantalla()


def mostrar_estudiante():
    """Busca un estudiante por ID y muestra sus datos básicos."""
    limpiar_pantalla()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        input("\nPresione Enter para continuar...")
        return

    id_buscar = input("Ingrese ID a buscar:\n")
    encontrado = False

    for estudiante in estudiantes:
        if id_buscar == estudiante[0]:
            print("\n--- Datos del Estudiante ---")
            print(f"ID:     {estudiante[0]}")
            print(f"NOMBRE: {estudiante[1]}")
            print(f"EDAD:   {estudiante[2]}")
            encontrado = True
            break

    if not encontrado:
        print("Según nuestros registros, el estudiante no existe.")

    input("\nPresione Enter para continuar...")


def imprimir_certificados():
    """Genera y muestra un certificado para un estudiante buscado por ID."""
    limpiar_pantalla()
    if not estudiantes:
        print("No hay estudiantes registrados.")
        input("\nPresione Enter para continuar...")
        return

    id_buscar = input("Ingrese ID a buscar para generar certificado:\n")
    encontrado = False

    for estudiante in estudiantes:
        if id_buscar == estudiante[0]:
            if len(estudiante) == 3:
                asistencia = random.randint(70, 100)
                notas = round(random.uniform(4.0, 7.0), 1)
                conducta = 'Ejemplar' if notas >= 5.0 and asistencia >= 85 else 'Bueno'
                estudiante.extend([asistencia, notas, conducta])

            print("\n--- Certificado de Estudiante ---")
            print(f"NOMBRE:     {estudiante[1]}")
            print(f"ASISTENCIA: {estudiante[3]}%")
            print(f"PROMEDIO:   {estudiante[4]}")
            print(f"CONDUCTA:   {estudiante[5]}")
            encontrado = True
            break

    if not encontrado:
        print("Alumno no existe.")

    input("\nPresione Enter para continuar...")


def menu():
    """Muestra el menú principal de opciones."""
    print("\n===== SISTEMA DE GESTIÓN DE ESTUDIANTES =====")
    print("1) Registrar Estudiante")
    print("2) Buscar Estudiante")
    print("3) Imprimir Certificados")
    print("4) Descargar Reporte en CSV")
    print("5) Salir")
    print("=============================================")


def descargar_archivo():
    """Guarda los datos de todos los estudiantes en un archivo CSV."""
    limpiar_pantalla()
    if not estudiantes:
        print("No hay estudiantes para exportar.")
        input("\nPresione Enter para continuar...")
        return
        
    nombre_archivo = 'reporte_estudiantes.csv'
    cabecera = ["ID", "NOMBRE", "EDAD", "ASISTENCIA (%)", "NOTA PROMEDIO", "CONDUCTA"]

    try:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(cabecera)

            for estudiante in estudiantes:
                if len(estudiante) < len(cabecera):
                    fila_completa = list(estudiante)
                    fila_completa.extend(['N/A'] * (len(cabecera) - len(estudiante)))
                    writer.writerow(fila_completa)
                else:
                    writer.writerow(estudiante)

        print(f"Archivo '{nombre_archivo}' creado exitosamente.")
    except IOError:
        print(f"Error: No se pudo escribir en el archivo '{nombre_archivo}'.")

    input("\nPresione Enter para continuar...")