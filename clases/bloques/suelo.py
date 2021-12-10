from clases.bloques.bloque import bloque
import pyxel
import constants as c
class suelo(bloque):
    def __init__(self, coord: list) -> None:
        # una vez que el profesor nos pase el archivo con los sprites
        super().__init__(coord, c.sprite_suelo, pyxel.width, pyxel.height/3)
