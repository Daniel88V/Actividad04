class Recepción:
    def __init__(self, nombre, telefono,identificacion,edad):
        self.nombre = nombre
        self.telefono = telefono
        self.identificacion = identificacion
        self.edad = edad



def menu():
    while True:
        print ("Bienvenido al menu de la Recepción")
        print("1.Agregar Pacientes")
        print("2.Atender Pacientes")
        print("3.Mostrar Cola")
        print("4.Salir")
        op = input("Elija una opción: ")


