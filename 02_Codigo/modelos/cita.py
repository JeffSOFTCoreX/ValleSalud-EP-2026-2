class Cita:
    def __init__(self, fecha, hora, motivo, paciente):
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.paciente = paciente
        self.medicamentos = []
        paciente.agregar_cita(self)

    def agregar_medicamento(self, medicamento):
        self.medicamentos.append(medicamento)

    def resumen(self):
        tratamiento = ", ".join(str(m) for m in self.medicamentos) or "Sin medicamentos"
        return (f"{self.fecha} {self.hora} | Paciente: {self.paciente.nombre} | "
                f"Motivo: {self.motivo} | Tratamiento: {tratamiento}")

    def __str__(self):
        return self.resumen()
