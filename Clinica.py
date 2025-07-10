def menu:
    while True:

print ("Bienvenido al menu de la Recepción")
print("1.Agregar Pacientes")
print("2.Atender Pacientes")
print("3.Mostrar Cola")
print("4.Salir")
print("Elija una opción")
op = int(input())
if op == 1:
    print("Nombre del paciente")
    nombre = input()
    print("ID")
    id = int(input())
    print("No. Telefono")
    telefono = input()
elif op == 2:
    print(f"el nombre del paciente {nombre}")
    print(f"el telefono del paciente {telefono}")
    print(f"Paciente {id} esta siendo atendido")
elif op == 3:
    print("Listado de los pacientes")
if op == 4:
    print("Estamos Saliendo")
    
