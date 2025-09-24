import vehiculo
from time import sleep


class VehiculoElectrico(vehiculo.Vehiculo):
    bateria_baja = 'Error no se pudo {}. Bateria baja.'

    def __init__(self, tipo, marca, modelo, color, total_precio, llantas):
        super().__init__(tipo, marca, modelo, color, total_precio)
        self.llantas = llantas
        self.__bateria = 100

    def __str__(self):
        return super().__str__() + f'\nLlantas: {self.llantas}\nBateria: {self.bateria}%'

    def __repr__(self):
        return super().__repr__().replace(")", ', ')+f'Llantas: {self.llantas} Bateria: {self.bateria}%'

    def __len__(self):
        return 9

    def verificar_descarga(self, descarga):
        if isinstance(descarga, int) and self.bateria >= descarga and descarga >= 0:
            self.bateria -= descarga
            print('Ha bajado un 10% de su bateria')
        else:
            print('Bateria sin carga')

    def arrancar(self):
        if self.verificar_descarga(5):
            super().arrancar()
        else:
            print(VehiculoElectrico.bateria_baja.format('arrancar'))

    def acelerar(self):
        if self.verificar_descarga(10):
            super().acelerar()
        else:
            print(VehiculoElectrico.bateria_baja.format('acelerar'))

    def cargar(self):
        while self.bateria < 100:
            sleep(1)
            self.bateria += 1
            print(f'Cargando bateria {self.bateria}%')
        print('Bateria cargada al 100%')

    def descuento(self):
        precio = int(self.total_precio.strip('$'))
        descuento = precio * 10 / 100
        self.total_precio = int(precio - descuento)
        print('Descuento aplicado...')

    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, descarga):
        if isinstance(descarga, int) and self.bateria >= descarga:
            self.__bateria = descarga


if __name__ == '__main__':
    auto = VehiculoElectrico('Automovil', 'Tesla', 'Porsche', 'Rojo', '100000', 4)
    print(auto.descuento())
    print(auto())

    print('Representacion:', repr(auto))
    print('Cantidad de atributos:', len(auto))

    auto.bateria = 100
    print(auto.bateria)
