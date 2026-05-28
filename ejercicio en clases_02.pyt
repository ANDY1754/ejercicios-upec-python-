# ejercicio_02

# Variables
peso_total = 0
mayores_50 = 0
envio_prioritario = False

# Repetición para los 5 paquetes
for i in range(1, 6):

    # Entrada de datos
    peso = float(input("Ingrese el peso del paquete: "))

    # Acumulador
    peso_total = peso_total + peso

    # Contador
    if peso > 50:
        mayores_50 = mayores_50 + 1

    # Bandera booleana
    prioridad = input("¿El envío es prioritario? (si/no): ")

    if prioridad == "si":
        envio_prioritario = True

# Resumen final
print("\n----- RESUMEN FINAL -----")
print("Peso total acumulado:", peso_total)
print("Cantidad de paquetes mayores a 50 kg:", mayores_50)

if envio_prioritario:
    print("Sí existió al menos un envío prioritario")
else:
    print("No existió ningún envío prioritario")
