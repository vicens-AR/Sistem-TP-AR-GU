import time
import random

class Nodo:
    def __init__(self, nombre):
       self.nombre = nombre
       self.conexiones = []
       self.buffer = []

    def Agregar_conexion(self,nodo):
        self.conexiones.append(nodo)
        
    def enviar_mensaje(self,mensaje):
        print(f"{self.nombre} has enviado un mensaje que dice: {mensaje}")
        for conexion in self.conexiones:
            conexion.recibir_mensaje(mensaje)

    def recibir_mensaje(self, mensaje):
        print(f"{self.nombre} recibio un mensaje: {mensaje}")

    
    #metodos de parte 2
    def Eliminar_conexion(self,nodo):
        if nodo in self.conexiones:
            self.conexiones.remove(nodo)
            print(f"Se ha eliminado la conexión con : {self.nombre}")
    
    #metodo parte 3
    def procesar_buffer(self):
        print(f"Procesando mensajes en el buffer de {self.nombre}")
        for mensaje in self.buffer:
            if random.random() < 0.5:  # Probabilidad de perdida de paquetes
                print(f"¡Mensaje perdido en {self.nombre}!")
            else:
                self.enviar_mensaje(mensaje)
        self.buffer = []

#crear nodos
servidor = Nodo("Servidor")

cliente1 = Nodo("Martina")
cliente2 = Nodo("Negro")
cliente3 = Nodo("Carla")


#establer conexiones
cliente1.Agregar_conexion(servidor)
cliente2.Agregar_conexion(servidor)
cliente3.Agregar_conexion(servidor)
servidor.Agregar_conexion(cliente3)
servidor.Agregar_conexion(cliente2)
servidor.Agregar_conexion(cliente1)

#desconexio y reconexion
servidor.Eliminar_conexion(cliente1)
print("Simulando desconexión y reconexión dinámica...")
time.sleep(10) 
servidor.Agregar_conexion(cliente1)
print("Hola de nuevo a todos!")



#mensajes enviados
mensaje = input("ingrese su mensaje: ")
servidor.enviar_mensaje(mensaje)
cliente1.recibir_mensaje(mensaje)
cliente2.recibir_mensaje(mensaje)
cliente3.recibir_mensaje(mensaje)


#buffer
cliente1.procesar_buffer()
cliente2.procesar_buffer()
cliente3.procesar_buffer()
