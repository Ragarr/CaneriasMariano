from clases.atrezzo.atrezzo import atrezzo
import constants as c

class arbusto(atrezzo):
    def __init__(self, coord:list) -> None:
        super().__init__(coord, c.sprite_arbusto)