

if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import constants as c
import pyxel


class objeto():
    def __init__(self, coord: list) -> None:

        self.__coord = coord
        self.__v_x = 0
        self.__v_y = 4
        self.__esta_activo = True

    @property
    def coord(self):
        return self.__coord
    @coord.setter
    def coord(self,coord):
        self.__coord=coord
    @property
    def v_x(self):
        return self.__v_x
    @v_x.setter
    def v_x(self,v_x):
        self.__v_x=v_x
    @property
    def v_y(self):
        return self.__v_y
    @v_y.setter
    def v_y(self,v_y):
        self.__v_y=v_y
    @property
    def esta_activo(self):
        return self.__esta_activo
    @esta_activo.setter
    def esta_activo(self,esta_activo:bool):
        self.__esta_activo=esta_activo


    def actualizar_posicion(self):
        self.coordenada[0] += self.v_x
        self.coordenada[1] += self.v_y

    def colisionar_bloque(self):
        self.v_x = 0 - self.v_x


class flor(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_flor

    def actualizar(self,player):
        return 0


class estrella(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_estrella

    def actualizar(self,player):
        return 0


class champi(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_champi

    def actualizar(self, player):
        return 0


class moneda(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_moneda_girada
        self.duracion_frames = pyxel.frame_count+c.fps
        self.consumida = False

    def actualizar(self,player):
        if self.duracion_frames > pyxel.frame_count and pyxel.frame_count % (c.fps/3) == 0:
            self.girar()
        elif self.duracion_frames > pyxel.frame_count:
            pass
        else:
            self.sprite = c.sprite_transparente
 

    def girar(self):
        if self.sprite == c.sprite_moneda_girada:
            self.sprite = c.sprite_moneda
        else:
            self.sprite = c.sprite_moneda_girada
