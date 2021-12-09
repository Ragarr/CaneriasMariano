import pyxel
import constants as c
from clases.objeto import objeto

class moneda(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_moneda_girada
        self.duracion_frames = pyxel.frame_count+c.fps/3 # durara en pantalla 0.2secs
        self.v_y=-1.5 # asi la moneda subira al aparecer
        self.ancho=9

    def actualizar(self,player):
        if self.duracion_frames > pyxel.frame_count and pyxel.frame_count % (c.fps/15) == 0:
            self.girar()
        elif self.duracion_frames > pyxel.frame_count:
            pass
        else:
            self.morir()
        self.actualizar_posicion()
 

    def girar(self):
        if self.sprite == c.sprite_moneda_girada:
            self.sprite = c.sprite_moneda
        else:
            self.sprite = c.sprite_moneda_girada

    def colisionar_jugador(self):
        pass
