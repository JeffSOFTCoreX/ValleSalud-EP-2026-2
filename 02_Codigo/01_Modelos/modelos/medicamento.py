class Medicamento:
    def __init__(self, nombre, dosis, frecuencia):
        self.nombre = nombre
        self.dosis = dosis
        self.frecuencia = frecuencia

    def describir(self):
        return f"{self.nombre} - {self.dosis}, cada {self.frecuencia}"

    def __str__(self):
        return self.describir()
