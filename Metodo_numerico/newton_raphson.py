class NewtonRaphson:
    """Usamos el método de Newton-Rapshon para calcular el tirante"""
    def __init__(self) -> None:
        pass

    def rectangular(self, factor_seccion, b ,x):
        
        self.funcion = (factor_seccion - ((b * x)**(5/3)/
                                        (b + 2 * x)**(2/3)))
        self.derivada = (-b * (b * x)**(2/3)*(5 * b + 6 * x))/ \
                        (3 * (b + 2 * x)**(5/3))
        return self.funcion, self.derivada
    
    def trapezoidal(self):
        pass
    
    def triangular(self):
        pass