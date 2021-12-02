

if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import constants as c
import pyxel


class objeto():
    def __init__(self, coord: list) -> None:

        self.__coord = coord
        self.__v_x = 0
        self.__v_y = 0
        self.__esta_activo = True

    @property
    def coord(self):
        return self.__coord
    @coord.setter
    def coord(self, new_coord):
        if len(new_coord) != 2:
            raise ValueError('La lista coord tiene que tener exactamente 2 elementos')
        self.__coord = new_coord
    @property
    def v_x(self):
        return self.__v_x
    @v_x.setter
    def v_x(self,new_v_x):
        if not isinstance(new_v_x,(float,int)):
            raise ValueError('La velocidad debe ser un entero o float')
        self.__v_x=new_v_x
    @property
    def v_y(self):
        return self.__v_y
    @v_y.setter
    def v_y(self,new_v_y):
        if not isinstance(new_v_y, (float, int)):
            raise ValueError('La velocidad debe ser un entero o float')
        self.__v_y = new_v_y
    @property
    def esta_activo(self):
        return self.__esta_activo
    @esta_activo.setter
    def esta_activo(self,esta_activo:bool):
        if not isinstance(esta_activo, bool):
            raise ValueError('el estado de activo debe ser un valor booleano')
        self.__esta_activo=esta_activo


    def actualizar_posicion(self):
        self.coord[0] += self.v_x
        self.coord[1] += self.v_y

    def colisionar_bloque(self):
        self.v_x = 0 - self.v_x


class flor(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_flor

    def actualizar(self,player):
        self.actualizar_posicion()


class estrella(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_estrella

    def actualizar(self,player):
        self.actualizar_posicion()


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
        self.duracion_frames = pyxel.frame_count+c.fps/3 # durara en pantalla 0.2secs
        self.consumida = False
        self.v_y=-1.5 # asi la moneda subira al aparecer

    def actualizar(self,player):
        if self.duracion_frames > pyxel.frame_count and pyxel.frame_count % (c.fps/15) == 0:
            self.girar()
        elif self.duracion_frames > pyxel.frame_count:
            pass
        else:
            self.sprite = c.sprite_transparente
        self.actualizar_posicion()
 

    def girar(self):
        if self.sprite == c.sprite_moneda_girada:
            self.sprite = c.sprite_moneda
        else:
            self.sprite = c.sprite_moneda_girada
