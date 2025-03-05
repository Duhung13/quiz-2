
class Persona:

    def __init__(self, nombre, apellido, cedula, tipe,mes, horastrabajadas):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.type = tipe
        self.mes = mes
        self.horastrabajadas = horastrabajadas

    def persona_show(self):
        return f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Cedula: {self.cedula}
        Type: {self.type}
        Horas Trabajadas: {self.horastrabajadas}
        """