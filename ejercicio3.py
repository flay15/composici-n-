class Motor:
    def __init__(self, tipo):
        self.tipo = tipo

class Coche:
    def __init__(self, marca, tipo_motor):
        self.marca = marca
        self.motor = Motor(tipo_motor)

    def encender_motor(self):
        print(f"El coche {self.marca} con motor {self.motor.tipo} está encendido.")

coche = Coche("Toyota", "V8")
coche.encender_motor()
