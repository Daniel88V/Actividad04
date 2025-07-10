print("Bienvenido a la farmacia")
class Medicamento:
    def __init__(self, nombre, tipo, fechavec):
        self._nombre = nombre
        self._tipo = tipo
        self._FechaVec = fechavec
        self._medicamento = []
    def ingreso_medicamento(self, medicamento):
        self._medicamento.append(medicamento)
        print(f"Medicamento: {self._medicamento} agregado exitosamente")
    def __str__(self):
        return f"Medicamento: {self._medicamento} Fecha de Vencimiento: {self._FechaVec}"

def main():
    mi_clinica = Medicamento("Farmacia de la clinica")
    print(f"Bienvenido a la farmacia")
    while True:
        print(" ==== MENÚ FARMACIA ====")
        print("1. Agregar medicamento")
        print("2. Asignar medicamento")
        print("3. Mostrar pila")
        print("4. Salir")
        eleccion = input("Seleccione una opción: ")
        if eleccion == "1":
            mi_clinica.ingreso_medicamento()