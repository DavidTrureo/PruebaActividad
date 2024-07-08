import time, os, random, csv, math

# Lista de productos
productos = ["Televisor", "Lavadora", "Refrigerador", "Microondas", "Computadora", "Celular", "Impresora", "Cafetera", "Licuadora", "Ventilador"]

# Función para Limpiar Pantalla
def limpiar():
    os.system("clear")
    
# Función para asignar precios aleatorios
def asignar_precios_aleatorios():
    precios = {}
    for producto in productos:
        precios[producto] = random.randint(300000, 2500000)
    return precios

# Función para clasificar precios
def clasificar_precios(precios):
    clasificacion = {"menores_800000": [], "entre_800000_y_2000000": [], "superiores_2000000": []}
    for producto, precio in precios.items():
        if precio < 800000:
            clasificacion["menores_800000"].append((producto, precio))
        elif 800000 <= precio <= 2000000:
            clasificacion["entre_800000_y_2000000"].append((producto, precio))
        else:
            clasificacion["superiores_2000000"].append((producto, precio))
    return clasificacion

# Función para ver estadísticas
def ver_estadisticas(precios):
    precios_valores = list(precios.values())
    precio_min = min(precios_valores)
    precio_max = max(precios_valores)
    precio_prom = sum(precios_valores) / len(precios_valores)
    precio_media_geo = math.exp(sum(math.log(p) for p in precios_valores) / len(precios_valores))
    return precio_min, precio_max, precio_prom, precio_media_geo

# Función para generar reporte de precios y exportar a CSV
def reporte_precios(precios):
    reporte = "Producto,Precio Base,Descuento Promoción,Descuento Membresía,Precio Final\n"
    for producto, precio in precios.items():
        descuento_promocion = precio * 0.10
        descuento_membresia = precio * 0.05
        precio_final = precio - descuento_promocion - descuento_membresia
        reporte += f"{producto},{precio},{descuento_promocion},{descuento_membresia},{precio_final}\n"
    
    with open('reporte_precios.csv', 'w', newline='') as file:
        file.write(reporte)
    return reporte

# Menú principal
def menu():
    precios = {}
    while True:
        limpiar()
        print("****** Menú de la Tienda ******")
        print(" ")
        print("1. Asignar precios aleatorios")
        print("2. Clasificar precios")
        print("3. Ver estadísticas")
        print("4. Reporte de precios")
        print("5. Salir del programa")
        print(" ")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            limpiar()
            precios = asignar_precios_aleatorios()
            print("****** Asignar Precios Aleatorios ******")
            print(" ")
            for producto, precio in precios.items():
                print(f"{producto}: ${precio}")
            print(" ")
            x = input("Presione Enter para continuar...")

        elif opcion == "2":
            if precios:
                limpiar()
                print("****** Clasificación de Precios ******")
                print(" ")
                clasificacion = clasificar_precios(precios)
                print("*** Precios Menores a $800.000 ***")
                print(" ")
                if clasificacion["menores_800000"]:
                    for producto, precio in clasificacion["menores_800000"]:
                        print(f"{producto}: ${precio}")
                else:
                    print("No existen productos en este rango")
                print(" ")
                print("*** Precios Entre $800.000 y $2.000.000 ***")
                print(" ")
                if clasificacion["entre_800000_y_2000000"]:
                    for producto, precio in clasificacion["entre_800000_y_2000000"]:
                        print(f"{producto}: ${precio}")
                else:
                    print("No existen productos en este rango")
                print(" ")
                print("*** Precios Superiores a $2.000.000 ***")
                print(" ")
                if clasificacion["superiores_2000000"]:
                    for producto, precio in clasificacion["superiores_2000000"]:
                        print(f"{producto}: ${precio}")
                else:
                    print("No existen productos en este rango")
                print(" ")
                x = input("Presione Enter para continuar...")
            else:
                print(" ")
                print("Primero debe asignar precios a los productos.")
                time.sleep(2)

        elif opcion == "3":
            if precios:
                limpiar()
                print("****** Ver Estadisticas ******")
                print(" ")
                precio_min, precio_max, precio_prom, precio_media_geo = ver_estadisticas(precios)
                print(f"Precio Mínimo: ${precio_min}\nPrecio Máximo: ${precio_max}\nPrecio Promedio: ${precio_prom:.2f}\nMedia Geométrica: ${precio_media_geo:.2f}\n")
                print(" ")
                x = input("Presione Enter para continuar...")
            else:
                print(" ")
                print("Primero debe asignar precios a los productos.")
                time.sleep(2)

        elif opcion == "4":
            if precios:
                limpiar()
                print("****** Reporte de Precios ******")
                print(" ")
                reporte = reporte_precios(precios)
                print("Reporte generado y guardado como 'reporte_precios.csv'.")
                print(" ")
                #print(reporte)
                print(" ")
                x = input("Presione Enter para continuar...")
            else:
                print(" ")
                print("Primero debe asignar precios a los productos.")
                time.sleep(2)
        elif opcion == "5":
            limpiar()
            print("Saliendo del programa.")
            print(" ")
            print("Desarrollado por David Trureo Ahumada")
            print("Versión 1.0")
            time.sleep(1)
            limpiar()
            print("Saliendo del programa..")
            print(" ")
            print("Desarrollado por David Trureo Ahumada")
            print("Versión 1.0")
            time.sleep(1)
            limpiar()
            print("Saliendo del programa...")
            print(" ")
            print("Desarrollado por David Trureo Ahumada")
            print("Versión 1.0")
            time.sleep(3)
            break
        else:
            print("Opción no válida, intente de nuevo.")
