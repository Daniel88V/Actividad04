cola_pacientes = []
def agregar_paciente():
    nombre = input("Ingrese el nombre del paciente: ")
    cola_pacientes.append(nombre)
    print("agregado")

    def atender_paciente():
        if len(cola_pacientes) > 0: #len sirve para ver cuantos hay en la lista
            paciente = cola_pacientes.pop(0)
            print(f"Atendido {paciente}")
        else:
            print("No hay nadie")

    def mostar_info():
        if len(cola_pacientes) >0:
            print("pacientes en la cola:")
            for pacientes in cola_pacientes:
                print(pacientes)
                print()
            else:
                print("No hay nadie, ingresa a alguien")
class clientes:
    def __init__(self, nombre, telefono,identificacion,edad):




def menu():
    while True:
        print ("Bienvenido al menu de la Recepción")
        print("1.Agregar Pacientes")
        print("2.Atender Pacientes")
        print("3.Mostrar Cola")
        print("4.Salir")
        op = input("Elija una opción: ")



