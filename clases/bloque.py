import pyxel
import random

class bloque():
    def __init__(self,coord:list,sprite:list) -> None:
        """coord es una lista que contiene x e y en dicho orden. sprite es una lista de 5 elementos 
        que contiene en este orden los siguienes valores n este orden:
            -el numero de banco del sprite
            -la pos x donde se inicia el sprite
            -la pos y donde se inicia el sprite
            -la pos x final del sprite
            -la pos y final del sprite
        """
        self.coord=coord # lista de la forma: (x_i,y_i) donde se inicia la posicion del sprite en pantalla
        self.sprite=sprite # lista que contiene la info para localizar el sprite en memoria

        self.ancho = 0  # aqui hay que añadir el ancho (x) del ladrillo en pixeles para cuando tengamos el archivo con los sprites
        self.largo = 0  # mas de lo mismo que arriba pero con el largo (y) en pixeles

class ladrillo_no_rompible(bloque):
    """un bloque con textura de ladrillo que no interactua con el jugador"""
    def __init__(self, coord: list) -> None:
        super().__init__(coord, ["""aqui va el sprite"""]) # una vez que el profesor nos pase el archivo con los sprites


class ladrillo_rompible(bloque):
    """un bloque con textura de ladrillo que cuando es golpeado por el jugador suelta le da una moneda"""
    def __init__(self, coord: list) -> None:
        super().__init__(coord, ["""aqui va el sprite"""])  # una vez que el profesor nos pase el archivo con los sprites
        self.monedas=random.randint()