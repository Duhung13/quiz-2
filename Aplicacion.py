from Ingeniero import Ingeniero
from Arquitecto import Arquitecto
from Obrero import Obrero

class Aplicacion:
    def __init__(self):
        self.personas = []

    
    def registrarPersona(self):

        nombre = input("Ingrese el nombre de la persona: ")
        apellido = input("Ingrese el apellido de la persona: ")
        cedula = input("Ingrese la cedula de la persona: ")
        tipe = input("Ingrese el tipo de trabajador (O/A/I): ")
        mes = input("Ingrese el mes de trabajo: ")
        if tipe == "O":
            
            horastrabajadas = input("Ingrese las horas trabajadas: ")
            especialidad = input("Ingrese la especialidad: ")
            honorario = "5"
            self.personas.append(Obrero(nombre, apellido, cedula, tipe, mes, horastrabajadas, especialidad, honorario))
        elif tipe == "A":
            horastrabajadas = input("Ingrese las horas trabajadas: ")
            especialidad = input("Ingrese la especialidad: ")
            honorario = "10"
            self.personas.append(Arquitecto(nombre, apellido, cedula, tipe, mes,  horastrabajadas, especialidad, honorario))

        elif tipe == "I":
            horastrabajadas = input("Ingrese las horas trabajadas: ")
            especialidad = input("Ingrese la especialidad: ")
            honorario = "25"
            self.personas.append(Ingeniero(nombre, apellido, cedula, tipe, mes, horastrabajadas, especialidad, honorario))
    

        print("Persona registrada con exito")

    def TotalPagado9(self):
        total = 0
        for persona in self.personas:
            total += persona.horastrabajadas
        print(f"El total pagado es: {total}")
    
    def CantidadEmpleadosporTipo(self):
        contadorO = 0
        contadorA = 0
        contadorI = 0
        for persona in self.personas:
            if persona.type == "O":
                contadorO += 1
            elif persona.type == "A":
                contadorA += 1
            elif persona.type == "I":
                contadorI += 1
        print(f"La cantidad de obreros es: {contadorO}")
        print(f"La cantidad de arquitectos es: {contadorA}")
        print(f"La cantidad de ingenieros es: {contadorI}")
    
    def PromedioPagotipoEmpleado(self):

        contadorO = 0
        contadorA = 0
        contadorI = 0
        totalO = 0
        totalA = 0
        totalI = 0
        for persona in self.personas:
            if persona.type == "O":
                contadorO += 1
                totalO += persona.horastrabajadas
            elif persona.type == "A":
                contadorA += 1
                totalA += persona.horastrabajadas
            elif persona.type == "I":
                contadorI += 1
                totalI += persona.horastrabajadas
        print(f"El promedio de pago para los obreros es: {totalO/contadorO}")
        print(f"El promedio de pago para los arquitectos es: {totalA/contadorA}")
        print(f"El promedio de pago para los ingenieros es: {totalI/contadorI}")

    def EmpleadoMayorPagoporTipo(self):
        mayorO = None
        mayorA = None
        mayorI = None
        for persona in self.personas:
            if persona.type == "O":
                if mayorO is None or int(persona.horastrabajadas) > int(mayorO.horastrabajadas):
                    mayorO = persona
            elif persona.type == "A":
                if mayorA is None or int(persona.horastrabajadas) > int(mayorA.horastrabajadas):
                    mayorA = persona
            elif persona.type == "I":
                if mayorI is None or int(persona.horastrabajadas) > int(mayorI.horastrabajadas):
                    mayorI = persona

        if mayorO:
            print(f"El obrero con mayor pago es: {mayorO.nombre} {mayorO.apellido} con {mayorO.horastrabajadas} horas trabajadas")
        else:
            print("No hay obreros registrados")

        if mayorA:
            print(f"El arquitecto con mayor pago es: {mayorA.nombre} {mayorA.apellido} con {mayorA.horastrabajadas} horas trabajadas")
        else:
            print("No hay arquitectos registrados")

        if mayorI:
            print(f"El ingeniero con mayor pago es: {mayorI.nombre} {mayorI.apellido} con {mayorI.horastrabajadas} horas trabajadas")
        else:
            print("No hay ingenieros registrados")

    
    def MontoFacturadoPrimo(self, datito, recarga):

        valuee = True
        contador = 2
        while contador <= int(datito):
            contador += 1
            if int(datito) % contador == 0:
                valuee = False

        contador3 = 0

            
        if valuee:
            contador2 = 1
            while contador2 <= int(datito):
                if int(datito) % contador2 == 0:
                    contador3 += 1
                contador2 += 1
            if contador3 < int(datito):
                print(f"El monto facturado es: { - int(recarga) * 0.05 + int(recarga) - int(recarga) *0.1}")
            else:
                print(f"El monto facturado es: { - int(recarga) * 0.05 + int(recarga)}")
                
        
        else:
            contador2 = 1
            while contador2 <= int(datito):
                if int(datito) % contador2 == 0:
                    contador3 += 1
                contador2 += 1
            
            if contador3 < int(datito):
                print(f"El monto facturado es: {int(recarga) - int(recarga) *0.1}")
            else:
                print(f"El monto facturado es: {int(recarga)}")
        
    def menu(self):

        while True:
            print("1. Registrar persona")
            print("2. Estadisticas")
            print("3. Salir")
            opcion = input("Ingrese la opcion: ")
            if opcion == "1":
                self.registrarPersona()
            elif opcion == "2":
                print("1. Total pagado")
                print("2. Cantidad de empleados por tipo")
                print("3. Promedio de pago por tipo de empleado")
                print("4. Empleado con mayor pago por tipo")
                print("5. Monto facturado")
                opcion2 = input("Ingrese la opcion: ")
                if opcion2 == "1":
                    self.TotalPagado9()
                elif opcion2 == "2":
                    self.CantidadEmpleadosporTipo()
                elif opcion2 == "3":
                    self.PromedioPagotipoEmpleado()
                elif opcion2 == "4":
                    self.EmpleadoMayorPagoporTipo()
                elif opcion2 == "5":
                    datito = input("Ingrese un numero: ")
                    recarga = input("Ingrese el monto: ")
                    self.MontoFacturadoPrimo(datito, recarga)
            elif opcion == "3":
                break
        
aplicacion = Aplicacion()
aplicacion.menu()

        

        