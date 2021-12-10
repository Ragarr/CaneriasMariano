from clases.objetos.objeto import objeto
import constants as c 


class mastil(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite=c.sprite_mastil
        self.coord=coord
        self.ancho = 2
        self.alto = 152

    def colisionar_jugador(self):
        pass

    def actualizar(slef,player):
        pass
