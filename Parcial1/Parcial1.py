viajes = []

def registrar_viaje():
    dia = input("Día del viaje (ej. lunes): ")
    origen = input("Origen: ")
    destino = input("Destino: ")
    ruta = input("Ruta (urbana/rural): ")
    tiempo = float(input("Tiempo del viaje en minutos: "))
    costo = float(input("Costo del viaje en USD: "))
    
    viaje = {
        "día": dia,
        "origen": origen,
        "destino": destino,
        "ruta": ruta,
        "tiempo": tiempo,
        "costo": costo
    }
    viajes.append(viaje)

def mostrar_viajes():
    print("\n📋 Lista de viajes realizados:")
    for i, v in enumerate(viajes, 1):
        print(f"{i}. {v['día'].capitalize()} - {v['origen']} → {v['destino']} | Ruta: {v['ruta']} | Tiempo: {v['tiempo']} min | Costo: ${v['costo']:.2f}")

def resumen_semanal():
    total_tiempo = sum(v["tiempo"] for v in viajes)
    total_costo = sum(v["costo"] for v in viajes)
    print("\n📊 Resumen semanal:")
    print(f"🕒 Tiempo total invertido: {total_tiempo:.2f} minutos")
    print(f"💵 Gasto total en transporte: ${total_costo:.2f}")

# Menú principal
while True:
    print("\n--- Sistema de Registro de Transporte Público ---")
    print("1. Registrar nuevo viaje")
    print("2. Mostrar viajes realizados")
    print("3. Mostrar resumen semanal")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        registrar_viaje()
    elif opcion == "2":
        mostrar_viajes()
    elif opcion == "3":
        resumen_semanal()
    elif opcion == "4":
        print("¡Gracias por usar el sistema!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")