
#Modulo para Viaje

#Crear la clase Viaje la cual tendra los datos de los viajes hechos (dia, origen, destino, ruta, tiempo, costo)
class Viaje:
    def __init__(self, dia, origen, destino, ruta, tiempo, costo):
        self.dia = dia
        self.origen = origen
        self.destino = destino
        self.ruta = ruta
        self.tiempo = tiempo
        self.costo = costo

#
    def mostrar(self):
        return (f"{self.dia.capitalize()} - {self.origen} → {self.destino} | "
                f"Ruta: {self.ruta} | Tiempo: {self.tiempo} min | Costo: ${self.costo:.2f}")