from clases.objetos.objeto import objeto
import constants as c

class bandera(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_bandera
        self.coord = coord
        self.ancho = 3 # para que se agarre al mastil y no a la bandera como tal
        self.alto = 152

    def colisionar_jugador(self):
        self.v_y=1

    def actualizar(self, player):
        self.actualizar_posicion()
