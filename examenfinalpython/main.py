import functions
import time  # 1. Importamos el módulo time

def main():
    """Función principal que ejecuta el menú del programa."""
    while True:
        functions.limpiar_pantalla()
        functions.menu()

        try:
            opcion = int(input("Ingrese una opción: \n"))

            if opcion == 1:
                functions.registrar_estudiante()
            elif opcion == 2:
                functions.mostrar_estudiante()
            elif opcion == 3:
                functions.imprimir_certificados()
            elif opcion == 4:
                functions.descargar_archivo()

            # --- AQUÍ ESTÁ EL CAMBIO ---
            elif opcion == 5:
                functions.limpiar_pantalla()

                # Mensaje base que se repetirá
                mensaje_salida = "SALIENDO"

                # Bucle que se ejecuta 3 veces para añadir los puntos
                for i in range(1, 4):
                    # Limpia la pantalla en cada iteración para que el mensaje parezca actualizarse en el mismo lugar
                    functions.limpiar_pantalla()

                    # Crea la cadena de puntos (".", "..", "...")
                    puntos = "." * i

                    # Imprime el mensaje
                    print(mensaje_salida + puntos)

                    # Pausa de 0.6 segundos
                    time.sleep(0.6)

                # Mensaje final de despedida (opcional)
                print("\n¡Hasta luego!")
                time.sleep(1) # Una última pausa para que se pueda leer
                functions.limpiar_pantalla()

                break # Sale del bucle y termina el programa

            else:
                print("Opción no válida. Por favor, intente de nuevo.")
                input("Presione Enter para continuar...")

        except ValueError:
            print("Entrada incorrecta. Por favor, ingrese un número válido.")
            input("Presione Enter para continuar...")


# Esta construcción asegura que el código solo se ejecute
# cuando se corre este archivo directamente.
if __name__ == "__main__":
    main()