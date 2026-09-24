class Paciente:
    def __init__(self, nombre, documento, telefono):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono
        self.citas = []

    def agregar_cita(self, cita):
        self.citas.append(cita)

    def mostrar_informacion(self):
        return f"{self.nombre} | Documento: {self.documento} | Teléfono: {self.telefono}"

    def __str__(self):
        return self.mostrar_informacion()
