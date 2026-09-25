from paciente import Paciente
from cita import Cita
from medicamento import Medicamento


def ejecutar_pruebas():
    print("=== PRUEBAS DEL SISTEMA MÉDICO ===")

    paciente = Paciente("Ana García", "12345678", "3001234567")
    medicamento = Medicamento("Paracetamol", "500 mg", "8 horas")
    cita = Cita("25/09/2026", "09:00", "Control general", paciente)
    cita.agregar_medicamento(medicamento)

    print("[OK] Paciente creado:", paciente)
    print("[OK] Medicamento creado:", medicamento)
    print("[OK] Cita creada:", cita)
    print("[OK] Relación paciente-cita:", len(paciente.citas) == 1)
    print("[OK] Relación cita-medicamento:", len(cita.medicamentos) == 1)

    assert paciente.nombre == "Ana García"
    assert paciente.citas[0] is cita
    assert cita.medicamentos[0] is medicamento
    assert medicamento.dosis == "500 mg"

    print("[OK] Todas las pruebas finalizaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
