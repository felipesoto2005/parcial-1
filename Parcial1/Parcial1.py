
#MainClass

#Llamar 
from registro import RegistroViajes
from viaje import Viaje



class SistemaTransporte:
    def __init__(self):
        self.registro = RegistroViajes()

    def registrar_viaje(self):
        print("\n📝 Registro de nuevo viaje:")
        dia = input("Día del viaje (ej. lunes): ")
        origen = input("Origen: ")
        destino = input("Destino: ")
        ruta = input("Ruta (urbana/rural): ")
        tiempo = float(input("Tiempo del viaje en minutos: "))
        costo = float(input("Costo del viaje en USD: "))
        viaje = Viaje(dia, origen, destino, ruta, tiempo, costo)
        self.registro.agregar_viaje(viaje)

    def ejecutar(self):
        while True:
            print("\n--- Sistema de Registro de Transporte Público ---")
            print("1. Registrar nuevo viaje")
            print("2. Mostrar viajes realizados")
            print("3. Mostrar resumen semanal")
            print("4. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_viaje()
            elif opcion == "2":
                self.registro.mostrar_viajes()
            elif opcion == "3":
                self.registro.resumen_semanal()
            elif opcion == "4":
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    app = SistemaTransporte()
    app.ejecutar()