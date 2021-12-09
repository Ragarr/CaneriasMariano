from clases.bloque import bloque 
import constants as c
class tuberia(bloque):
    
    def __init__(self, coord: list, alto:int, colision = True) -> None:
        super().__init__(coord, c.tuberia(alto), c.ancho_tuberia, alto, colision, colision )
        
    def golpear(self,bloques=None, player=None):
        pass
