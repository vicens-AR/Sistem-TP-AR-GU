import time

class Nodo:
    def __init__(self, nombre):
       self.nombre = nombre
       self.conexiones = []
      

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
servidor.enviar_mensaje(input("ingresa tu mensaje:"))
cliente1.recibir_mensaje()
cliente2.recibir_mensaje()
cliente3.recibir_mensaje()