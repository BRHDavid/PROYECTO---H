class Incetidumbre():
    def __init__(self) -> None:
        pass
    
    def incertidumbre(self):
    
        entidades = ["caudal",
                     "pendiente",
                     "rugosidad"]
        dato = input(f"Incertidumbre de que parametro quiere conocer:{entidades[0],entidades[1], entidades[2]}")
        
        if dato.lower() == entidades[0]:
            self.q_max = float(input("Ingresa el Q máx: "))
            self.q_error = float(input("Ingresa el Q error: "))
            self.coeficiente_de_variacion = (self.q_max - self.q_error)/(self.q_max)
        
        elif dato.lower() == entidades[1]:
            self.s_max = float(input("Ingresa el s máx: "))
            self.s_error = float(input("Ingresa el s error: "))
            self.coeficiente_de_variacion = (self.s_max - self.s_error)/(self.s_max)
        
        elif dato.lower() == entidades[2]:
            self.n_max = float(input("Ingresa el n máx: "))
            self.n_error = float(input("Ingresa el n error: "))
            self.coeficiente_de_variacion = (self.n_max - self.n_error)/(self.n_max)
        
        self.varianza_tirante = (self.coeficiente_de_variacion)/ \
                                ((5 * self.b + self.tirante * 6)/(
                             3 * self.tirante * (self.b + 2 * self.tirante )))
        return self.varianza_tirante