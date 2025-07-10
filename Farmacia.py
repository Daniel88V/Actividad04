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
        return f"Medicamento: {self._medicamento}| Tipo: {self._tipo}| Fecha de Vencimiento: {self._FechaVec}"
class Farmacia:
    def __init__(self, nombre_farmacia):
        self._nombre_farmacia = nombre_farmacia
        self.medicamento = []
    def buscar_medicamento(self, nombre):
        for medicina in self.medicamento:
            if medicina._nombre == nombre:
                return medicina
        return None
    def registrar_medicina(self):
        print("---Registro de nuevo medicamento---")
        nombre = input("Nombre del medicamento: ")
        tipo = input("Tipo del medicamento: ")
        fechavec = input("Fecha de vencimento: ")
        if self.buscar_medicamento(fechavec):
            print("Este medicamento ya existe")
            return
        nueva_medicina = Medicamento(nombre, tipo, fechavec)
        self.medicamento.append(nueva_medicina)
        print(f"Medicamento: {nombre} agregado exitosamente")
    def entregar_medicamento(self):
        print("---Asignar medicamento a cliente---")

    def mostrar_medicamentos(self):
        for medicamento in self.medicamento:
            print(medicamento)
def main():
    mi_clinica = Farmacia("Farmacia de la clinica")
    print(f"Bienvenido a la farmacia")
    while True:
        print(" ==== MENÚ FARMACIA ====")
        print("1. Agregar medicamento")
        print("2. Asignar medicamento")
        print("3. Mostrar pila")
        print("4. Salir")
        eleccion = input("Seleccione una opción: ")
        if eleccion == "1":
            mi_clinica.registrar_medicina()
        elif eleccion == "4":
            print("Saliendo del sistema...")
            break
if __name__ == "__main__":
    main()