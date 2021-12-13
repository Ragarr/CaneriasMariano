from clases.bloques.bloque import bloque 
import constants as c
class castillo(bloque):
    
    def __init__(self,coord ) -> None:
     #Las tuberías tienen colisiones laterales en los dos extremos por ello no varían    
        
        super().__init__(coord, c.sprite_castillo,c.ancho_castillo,c.alto_castillo)