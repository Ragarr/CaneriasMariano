from clases.bloques.bloque import bloque
import constants as c

class escalera(bloque):
    """este bloque SOLO puede usarse para hacer escaleras o a nivel de suelo, si es true hay colision a la 
    derecha de la escalera"""
    def __init__(self, coord: list, alto:int, colisiones: bool = False) -> None:
        
        super().__init__(coord,c.escalera(alto), c.ancho_escalera, alto*c.alto_escalera , colisiones, not colisiones)

    def golpear(self, bloques=None, player=None):
        pass