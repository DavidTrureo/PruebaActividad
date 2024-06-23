#actividad experiencia 2 (2.4)
import os

os.system("clear")
#preguntar por cantidad de pasajes
#hacer bucle for
#preguntar por el precio (cada iteracion de la cantidad)
#si viene un dato != int habia que romper la app (break)

total_ingresos = 0
bandera_cantidad = True
bandera_precio = True
while bandera_cantidad:
    try:
        cantidad = int(input("ingrese cantidad de pasajes\n"))
        
        for x in range(cantidad):
            while bandera_precio:
                try:        
                    precio = int(input(f"ingrese precio de pasaje {x+1}\n"))
                    total_ingresos = total_ingresos + precio
                    break
                except:
                    print("no existe ese precio")
            
    except:
        print("numero no valido")
    break
    
print(f"para {cantidad} pasajes, el valor a pagar es ${total_ingresos}")
