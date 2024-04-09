class Nodo:
    def __init__(self,serv,C1,C2,C3):
        self.servidor = serv
        self.cliente1 = C1
        self.cliente2 = C2
        self.cliente3 = C3

    def Agregar_conexion(self):
        print(f"{self.servidor} se conecto con{self.cliente1}")