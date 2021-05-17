from datetime import datetime

class Reloj():
		
    def __init__(self, marca):
        self.marca = marca
        self._hora = datetime.now()

    @property
    def hora(self):
        self._hora = datetime.now()
        self.sonar()
        return self._hora.strftime("%H:%M:%S")

    def sonar(self):
        if (self._hora.minute == 0 and self._hora.second == 0):
            print("ding dong")

class Cronometro():

    def __init__(self, es_digital):
        self.es_digital = es_digital

class Reloj_pared(Reloj):

    def __init__(self, marca, tipo_soporte):
        super().__init__(marca)
        self.tipo_soporte = tipo_soporte

    def sonar(self):
        if (self._hora.minute == 0 and self._hora.second == 0):
            print("Cuckoo cuckoo")

class Reloj_muneca(Reloj):
		
    def __init__(self, marca, material_correa):
        super().__init__(marca)
        self.material_correa = material_correa

    def sonar(self):
        if (self._hora.minute == 0 and self._hora.second == 0):
            print("beep beep")

class Reloj_digital(Reloj, Cronometro):

    def __init__(self, marca, es_digital):
        Reloj.__init__(self, marca)
        Cronometro.__init__(self, es_digital)

reloj = Reloj("Hublot")
cuckoo = Reloj_pared("Anton", "Tornillos")
reloj_muneca = Reloj_muneca("Rolex", "oro")
digital = Reloj_digital("Casio", True)

print(reloj.hora)
print(cuckoo.hora)
print(reloj_muneca.hora)
print(digital.es_digital)
