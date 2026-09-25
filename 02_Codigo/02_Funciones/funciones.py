from cita import Cita
from medicamento import Medicamento


def registrar_cita(paciente, fecha, hora, motivo):
    """Registra una cita y la relaciona con un paciente."""
    cita = Cita(fecha, hora, motivo, paciente)
    return cita


def registrar_medicamento(cita, nombre, dosis, frecuencia):
    """Agrega un medicamento a una cita."""
    medicamento = Medicamento(nombre, dosis, frecuencia)
    cita.agregar_medicamento(medicamento)
    return medicamento


def mostrar_informacion(paciente):
    """Muestra la información básica de un paciente."""
    return paciente.mostrar_informacion()

