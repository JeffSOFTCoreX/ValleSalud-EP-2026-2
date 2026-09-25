from modelos.paciente import Paciente
from modelos.cita import Cita
from modelos.medicamento import Medicamento


def ejecutar_pruebas():

    print("=== DEMOSTRACIÓN DEL SISTEMA VALLESALUD ===\n")

    # Crear paciente
    paciente = Paciente(
        "Ana García",
        "12345678",
        "300123456"
    )

    # Crear medicamento
    medicamento = Medicamento(
        "Paracetamol",
        "500 mg",
        "8 horas"
    )

    # Crear cita relacionada al paciente
    cita = Cita(
        "25/09/2026",
        "09:00",
        "Control general",
        paciente
    )

    # Agregar medicamento a la cita
    cita.agregar_medicamento(medicamento)


    print("PACIENTE REGISTRADO:")
    print(paciente)

    print("\nMEDICAMENTO REGISTRADO:")
    print(medicamento)

    print("\nCITA REGISTRADA:")
    print(cita)


    print("\nVALIDACIÓN DE RELACIONES")
    print(
        "[OK] Paciente tiene citas:",
        len(paciente.citas) == 1
    )

    print(
        "[OK] Cita tiene medicamentos:",
        len(cita.medicamentos) == 1
    )

    print("\n[OK] Prototipo ejecutado correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
