"""Script para exportar los datos a Excel"""

import pandas as pd
from channel_rectangular import CanalRectangular
from data import caudal, base, pendiente, rugosidad

class ExportExcel:
    def __init__(self) -> None:
        self.canal_rectagular =  CanalRectangular(caudal, base, 
                                                  pendiente, rugosidad)
        
    def data_canal_rectangular(self):
        try:
            self.export = self.canal_rectagular.rectangular_excel()
            self.export = pd.DataFrame(self.export)
            self.export.to_excel("Canal_rectangular.xlsx", index = False)
            print(" - Exportado correctanmente - ")
        except ModuleNotFoundError:
            print("No se encontro el modulo 'openpyxl'")
        
    def data_canal_trapezoidal(self):
        pass

    def data_canal_triangular(self):
        pass

if __name__ == "__main__":
    prueba = ExportExcel()
    prueba.data_canal_rectangular()