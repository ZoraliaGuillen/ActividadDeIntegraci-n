class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, titular):
        self._titular = titular
    
    @property
    def cantidad(self):
        return self._cantidad
    
    def mostrar(self):
        print(f'Titular: {self.titular}, Cantidad: {self.cantidad}')
    
    def ingresar(self, cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
    
    def retirar(self, cantidad):
        self._cantidad -= cantidad



cuenta = Cuenta("Zoralia Guillen")
cuenta.mostrar()
cuenta.ingresar(100)
cuenta.mostrar()
cuenta.retirar(110)
cuenta.mostrar()