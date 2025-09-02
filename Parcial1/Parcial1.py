class Viaje:
    def __init__(self, dia, origen, destino, ruta, tiempo, costo):
        self.dia = dia
        self.origen = origen
        self.destino = destino
        self.ruta = ruta
        self.tiempo = tiempo
        self.costo = costo

   

class RegistroViajes:
    def __init__(self):
        self.viajes = []

    def agregar_viaje(self, viaje):
        self.viajes.append(viaje)

    def mostrar_viajes(self):
        print("\n Lista de viajes realizados:")
        for i, viaje in enumerate(self.viajes, 1):
            print(f"{i}. {viaje.mostrar()}")

    def resumen_semanal(self):
        total_tiempo = sum(v.tiempo for v in self.viajes)
        total_costo = sum(v.costo for v in self.viajes)
        print("\n Resumen semanal:")
        print(f" Tiempo total invertido: {total_tiempo:.2f} minutos")
        print(f" Gasto total en transporte: ${total_costo:.2f}")


registro = RegistroViajes()

def registrar_viaje():
    dia = input("Día del viaje: ")
    origen = input("Origen: ")
    destino = input("Destino: ")
    ruta = input("Ruta (urbana/rural): ")
    tiempo = float(input("ingrese el tiempo del viaje en minutos: "))
    costo = float(input("Costo del viaje en USD: "))
    viaje = Viaje(dia, origen, destino, ruta, tiempo, costo)
    registro.agregar_viaje(viaje)

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
        registro.mostrar_viajes()
    elif opcion == "3":
        registro.resumen_semanal()
    elif opcion == "4":
        print("¡Gracias por usar el sistema!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")