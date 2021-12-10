from clases.objetos.objeto import objeto
import constants as c 


class mastil(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord,c.sprite_mastil,2, 152)


    def colisionar_jugador(self):
        pass

    def actualizar(slef,player):
        pass
