from vehiculo_electrico import VehiculoElectrico


class Automobil(VehiculoElectrico):
    def __init__(self, marca, modelo, color, precio):
        super().__init__('Automobil', marca, modelo, color, precio, 4)

    @property
    def desplazar(self):
        print(f'{self.tipo} Desplazandose sobre {self.llantas} ruedas')


class Motocicleta(VehiculoElectrico):
    def __init__(self, marca, modelo, color, precio):
        super().__init__('Motocicleta', marca, modelo, color, precio, 2)

    @property
    def desplazar(self):
        print(f'{self.tipo} Desplazandose sobre {self.llantas} ruedas')


class Camion(VehiculoElectrico):
    def __init__(self, marca, modelo, color, precio):
        super().__init__('Camion', marca, modelo, color, precio, 8)

    @property
    def desplazar(self):
        print(f'{self.tipo} Desplazandose sobre {self.llantas} ruedas')


auto = Automobil('Tesla', 'Model X', 'Rojo', 100000)
moto = Motocicleta('BNW', 'CE04', 'Negro', 13000)
camion = Camion('Volvo', 'Nissan', 'Azul', 90000)

for vehiculo in (auto, moto, camion):
    vehiculo.desplazar
