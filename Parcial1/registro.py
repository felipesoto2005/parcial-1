from viaje import Viaje

class RegistroViajes:
    def __init__(self):
        self.viajes = []

    def agregar_viaje(self, viaje):
        self.viajes.append(viaje)

    def mostrar_viajes(self):
        print("\n📋 Lista de viajes realizados:")
        for i, viaje in enumerate(self.viajes, 1):
            print(f"{i}. {viaje.mostrar()}")

    def resumen_semanal(self):
        total_tiempo = sum(v.tiempo for v in self.viajes)
        total_costo = sum(v.costo for v in self.viajes)
        print("\n📊 Resumen semanal:")
        print(f"🕒 Tiempo total invertido: {total_tiempo:.2f} minutos")
        print(f"💵 Gasto total en transporte: ${total_costo:.2f}")