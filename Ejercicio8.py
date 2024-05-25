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



class CuentaJoven(Cuenta):
    def __init__(self, titular, edad, cantidad=0.0, bonificacion=0.0):
        super().__init__(titular, cantidad)
        self._bonificacion = bonificacion
        self._edad = edad
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self._bonificacion = bonificacion
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        self._edad = edad
    
    def titular_valido(self):
        return 18 <= self.edad < 25
    
    def mostrar(self):
        print(f'Cuenta Joven\nTitular: {self.titular}, Cantidad: {self.cantidad}, Bonificación: {self.bonificacion}%')
    
    def retirar(self, cantidad):
        if self.titular_valido():
            super().retirar(cantidad)
        else:
            print("El Titular no es válido para retirar dinero de la Cuenta Joven porque es mayor de 25 años.")



cuenta_joven_menor_25_anios = CuentaJoven("Zoralia Guillen", 20, 1000.0, 10.0)
cuenta_joven_menor_25_anios.mostrar()
cuenta_joven_menor_25_anios.ingresar(100)
cuenta_joven_menor_25_anios.mostrar()
cuenta_joven_menor_25_anios.retirar(110)
cuenta_joven_menor_25_anios.mostrar()

cuenta_joven_mayor_25_anios = CuentaJoven("Zoralia Guillen", 30, 1000.0, 10.0)
cuenta_joven_mayor_25_anios.mostrar()
cuenta_joven_mayor_25_anios.retirar(110)
cuenta_joven_mayor_25_anios.mostrar()