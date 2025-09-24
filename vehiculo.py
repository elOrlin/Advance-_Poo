class Vehiculo:
    __slots__ = ('id', 'tipo', 'marca', 'modelo', 'color', '__precio', '__arrancar')
    vehiculos_generados = 0

    def __init__(self, tipo, marca, modelo, color, precio):
        self.id = Vehiculo.incrementar()
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.__precio = str(precio)+"$"
        self.__arrancar = False

    def __call__(self):
        self.arrancar()
        self.acelerar()
        self.desplazar()
        self.frenar()

    def __str__(self):
        return f'Id: {self.id}\nTipo: {self.tipo}\nMarca: {self.marca}\nModelo: {self.modelo}\nColor: {self.color}\nPrecio: {self.__precio}\n'

    def __len__(self):
        return 6

    def vehiculo(self):
        return f'{self.marca} {self.modelo}'

    def arrancar(self):
        self.set_arrancar(True)
        print('Arrancando...')

    def acelerar(self):
        if self.get_arrancar():
            print('Acelerando...')
        else:
            print('Primero tienes que arrancar el vehiculo')

    def desplazar(self):
        print('Desplazandose...')

    def frenar(self):
        self.set_arrancar(False)
        print('Frenando...')

    @property
    @staticmethod
    def autor(self):
        print('Autor: Orlin')

    @classmethod
    def incrementar(cls):
        cls.vehiculos_generados += 1
        return cls

    def get_arrancar(self):
        return self.__arrancar

    def set_arrancar(self, value):
        if isinstance(value, bool):
            self.__arrancar = value

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def total_precio(self, value):
        resultado = str(value).replace("$", "").strip()
        if resultado.isdigit():
            self.__precio = resultado + "$"
        else:
            raise ValueError("El precio debe ser un número válido")


if __name__ == "__main__":
    auto = Vehiculo('Automovil', 'Tesla', 'Model S', 'Rojo', '90000')
    moto = Vehiculo('Moto', 'BMW', 'ce04', 'Negro', '13000')
    camion = Vehiculo('Camion', 'Volvo', 'FH16', 'Gris', '40000')

    for vehiculo in (auto, moto, camion):
        print(str(vehiculo))
        print(len(vehiculo))
        vehiculo.autor
        print('Vehiculos Generados', vehiculo.vehiculos_generados)
        vehiculo()
        print('aqui hay un camion', camion)
    print(vehiculo.get_arrancar())
    auto.total_precio = 50000
    print('Precio:', auto.total_precio)
