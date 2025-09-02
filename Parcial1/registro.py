
from viaje import Viaje

#Crear la clase para guardar y controlar los viajes que se van registrando
class RegistroViajes:
    def __init__(self):
        self.viajes = []

    def agregar_viaje(self, viaje):
        self.viajes.append(viaje) #simplemente lo metemo a la lista

    def mostrar_viajes(self):
        print("\n Lista de viajes realizados:")
        for i, viaje in enumerate(self.viajes, 1): #aqui haecos que la lista salga con un numerito para llevarlo de forma ordenaas
            print(f"{i}. {viaje.mostrar()}") # se usa el metodo mostrar del viaje


#aqui se suma el tiempo y el costo de los viajes para el resumen semanal
    def resumen_semanal(self):
        total_tiempo = sum(v.tiempo for v in self.viajes)
        total_costo = sum(v.costo for v in self.viajes)
        print("\n Resumen semanal:")
        print(f" Tiempo total invertido: {total_tiempo:.2f} minutos")
        print(f" Gasto total en transporte: ${total_costo:.2f}")