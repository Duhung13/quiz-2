from Persona import Persona

class Ingeniero(Persona):
    def __init__(self, nombre, apellido, cedula, tipe, mes, horastrabajadas, especialidad, Honorario):
        super().__init__(nombre, apellido, cedula, tipe, mes, horastrabajadas)
        self.especialidad = especialidad
        self.Honorario = Honorario

    
    def ingeniero_show(self):
        return f"""
        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Cedula: {self.cedula}
        Type: {self.type}
        Horas Trabajadas: {self.horastrabajadas}
        Especialidad: {self.especialidad}
        """
    