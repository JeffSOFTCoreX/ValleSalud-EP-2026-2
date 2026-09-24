import unittest

from funciones import registrar_cita, registrar_medicamento
from paciente import Paciente


class PruebasPI(unittest.TestCase):
    def test_registro_de_cita(self):
        paciente = Paciente("Ana García", "12345678", "3001234567")
        cita = registrar_cita(
            paciente,
            "25/09/2026",
            "09:00",
            "Control general",
        )

        self.assertEqual(len(paciente.citas), 1)
        self.assertIs(paciente.citas[0], cita)
        self.assertIs(cita.paciente, paciente)

    def test_registro_de_medicamento(self):
        paciente = Paciente("Ana García", "12345678", "3001234567")
        cita = registrar_cita(
            paciente,
            "25/09/2026",
            "09:00",
            "Control general",
        )
        medicamento = registrar_medicamento(
            cita,
            "Paracetamol",
            "500 mg",
            "8 horas",
        )

        self.assertEqual(len(cita.medicamentos), 1)
        self.assertIs(cita.medicamentos[0], medicamento)
        self.assertEqual(medicamento.nombre, "Paracetamol")


if __name__ == "__main__":
    unittest.main(verbosity=2)
