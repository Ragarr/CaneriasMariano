

if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import constants as c
import pyxel


class objeto():
    def __init__(self, coord: list) -> None:

        self.coord = coord
        self.velocidad_x = 0
        self.velocidad_y = 4
        self.activo = True

    def actualizar_posicion(self):
        self.coordenada[0] += self.velocidad_x
        self.coordenada[1] += self.velocidad_y

    def colisionar_bloque(self):
        self.velocidad_x = 0 - self.velocidad_x


class flor(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_flor

    def actualizar(self,player):
        pass


class estrella(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_estrella

    def actualizar(self,player):
        pass


class champi(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_champi

    def actualizar(self, player):
        pass


class moneda(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_moneda_girada
        self.duracion_frames = pyxel.frame_count+c.fps
        self.consumida = False

    def actualizar(self, player):
        if self.duracion_frames > pyxel.frame_count and pyxel.frame_count % (c.fps/3) == 0:
            self.girar()
        elif self.duracion_frames > pyxel.frame_count:
            pass
        else:
            self.sprite = c.sprite_transparente
        if not self.consumida:
            player.monedas += 1
            self.consumida = True

    def girar(self):
        if self.sprite == c.sprite_moneda_girada:
            self.sprite = c.sprite_moneda
        else:
            self.sprite = c.sprite_moneda_girada
