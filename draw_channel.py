"""Script para dibujar la sección en Autocad"""

from pyautocad import Autocad , aDouble as AD
from channel_rectangular import CanalRectangular
from data import caudal, base, pendiente, rugosidad, espesor, borde_libre

class DrawChannel():
    def __init__(self) -> None:
        self.canal_rectangular =  CanalRectangular(caudal, base, 
                                                  pendiente, rugosidad)

    def connect_autocad(self):
        self.acad = Autocad()
        return self.acad

    def draw_rectangular(self):
        x, y, z = self.acad.doc.Utility.GetPoint()
        tirante = self.canal_rectangular.tirante()
        self.polilinea = self.acad.model.AddPolyline(
            AD(
            x, y, z,
            x, y - tirante  - borde_libre - espesor, z,
            x + base + 2 * espesor, y - tirante - borde_libre - espesor, z,
            x + base + 2 * espesor, y , z,
            x + base + espesor , y , z,
            x + base + espesor, y - tirante - borde_libre, z,
            x + espesor, y - tirante  - borde_libre, z,
            x + espesor, y, z,
            )
        )
        self.polilinea.Closed = True
        
if __name__ == "__main__":
    prueba = DrawChannel()
    prueba.connect_autocad()


