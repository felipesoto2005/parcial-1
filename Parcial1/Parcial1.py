import time
#MainClass

#aqui importamos las clases que acarrean el sistema
from registro import RegistroViajes
from viaje import Viaje

#un dialogo de una parodia (no afecta el codigo principal solo es para ponerle brillo a la hora de la salida :3)
def undertale_dialogue():
    print("\nPapyrus:supongo que este es el momento... saborea mi dolor. *Le tira su brazo y ni siquiera llega a golpearlo*")
    time.sleep(1)
    print("Frisk: Buen golpe.")
    time.sleep(1)
    print("Papyrus: ¡MENUDO ESQUIVE! \(°O°) \n")


#clase principal
class SistemaTransporte:
    def __init__(self):
        self.registro = RegistroViajes() #crear registro para guardar los viajes

    #metodo para que el usuario ingrese datos
    def registrar_viaje(self):
        print("\n Registrar de nuevo viaje:")
        dia = input("Día del viaje: ")
        origen = input("Origen: ")
        destino = input("Destino: ")
        ruta = input("Ruta (urbana/rural): ")
        tiempo = float(input("Tiempo del viaje en minutos: "))
        costo = float(input("Costo del viaje en USD: "))
        viaje = Viaje(dia, origen, destino, ruta, tiempo, costo)
        self.registro.agregar_viaje(viaje)

#Un menu principal asi bien facha
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
                (undertale_dialogue())
                break
            else:
                print("Opción inválida. Intente de nuevo.")

#punto de partida del programa
if __name__ == "__main__":
    app = SistemaTransporte()
    app.ejecutar()
    
    
    
    
    
    
