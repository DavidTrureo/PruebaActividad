import os
os.system("clear")

print("hola mundo")


def elegir_entre_dos_valores(valor1, valor2):
    while True:
        entrada = input(f"Elija entre '{valor1}' y '{valor2}': ")
        if entrada == valor1:
            return valor1
        elif entrada == valor2:
            return valor2
        else:
            print("Error. Por favor, elija uno de los valores proporcionados.")

# Ejemplo de uso
opcion = elegir_entre_dos_valores("Fonasa", "Isapre")
print("Ha elegido:", opcion)