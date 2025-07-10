print("Bienvenido a la farmacia")
class Medicamento:
    def __init__(self, nombre, tipo, FechaVec):
        self._nombre = nombre
        self._tipo = tipo
        self._FechaVec = FechaVec
        self._medicamento = []
    def ingreso_medicamento(self, medicamento):
        self._medicamento.append(medicamento)
        print(f"Medicamento: {self._medicamento} agregado exitosamente")

