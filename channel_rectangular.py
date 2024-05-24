"""Script para exportar, calcular las propiedaes geométricas 
del canal rectangular"""

from newton_raphson import NewtonRaphson
from constantes import G, FLUJOS, TOLERANCIA
from math import sqrt

class CanalRectangular(NewtonRaphson):
    """Unidades de longitud en metros (m),
    tiempo en segundos (s) y volumen en metros
    cúbicos (m3)"""
    
    def __init__(self, q, b, s, n):
        super().__init__()
        if q <= 0 or b <= 0 or s <= 0 or n <= 0:
            raise ValueError("Todos los parámetros deben ser positivos.")
        
        self.q = q #m3/s
        self.b = b #m
        self.s = s # %%
        self.n = n #adimensional

        self.peso_especifico = 1000 #kg/m3
        self.factor_seccion = (self.q * self.n)/(sqrt(self.s))
        self.tirante_calculado = 0
        
    def tirante(self):
        """x0 es la condición inicial, por temas de eficiencia de código
        se usará como aproximación la hipótesis de canal ancho"""
        self.condicion_inicial = (self.factor_seccion / self.b) ** (3 / 5)
        iteraciones = 0
        max_iteraciones = 1000  # Limitar el número de iteraciones

        while iteraciones < max_iteraciones:
            self.fx, self.dx = self.rectangular(self.factor_seccion, self.b, 
                                                self.condicion_inicial)
            self.tirante_calculado = self.condicion_inicial - self.fx / self.dx
            if abs(self.tirante_calculado - self.condicion_inicial) < TOLERANCIA:
                break
            self.condicion_inicial = self.tirante_calculado
            iteraciones += 1

        return self.tirante_calculado
    
    def area(self):
        return self.b * self.tirante_calculado
    
    def espejo(self):
        return self.b
    
    def radio(self):
        return (self.b * self.tirante_calculado)/(self.b + 2 * self.tirante_calculado)
    
    def velocidad(self):
        return self.q / self.area()
    
    def froude(self):
        return self.velocidad() / sqrt(G * self.tirante_calculado)

    def perimetro(self):
        self.perimetro_rectangular = self.b + (self.tirante_calculado * 2)
        return self.perimetro_rectangular
    
    def energia_especifica(self):
        return self.tirante_calculado + self.velocidad() **2 / (G * 2)
    
    def fuerza_tractiva(self):
        return self.peso_especifico * self.radio() * self.s
    
    def flujo(self):
        froude = self.froude()
        
        if froude > 1:
            return FLUJOS[0]
        elif froude == 1:
            return FLUJOS[1]
        else:
            return FLUJOS[2]
        
    def rectangular_excel(self):
        self.data = {
            'VARIABLES' : ['Q','B ','S','n',
                            'y','A','T','Rh',
                            'V','F','P','E','t',
                            'Flujo'],
            'VALORES' : [self.q,self.b,self.s,self.n,
                        self.tirante(),self.area(),
                        self.espejo(),self.radio(),
                        self.velocidad(),self.froude(),
                        self.perimetro(),self.energia_especifica(),
                        self.fuerza_tractiva(),self.flujo()],
            'UNIDADES' : ['m3/s', 'm','m/m','',
                          'm','m2','m','m','m/s',
                          '','m','m','kg/m2','']
                }
        return self.data

if __name__ == '__main__':
    rectangular  = CanalRectangular(2, 1, 0.001, 0.014)
    print(rectangular.rectangular_excel())
        
    
        
    
        
    
        
    