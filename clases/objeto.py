


if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import constants as c

class objeto():
    def __init__(self,coord:list) -> None:

        self.coord = coord
        self.velocidad_x=0
        self.velocidad_y=4
        self.activo=True
    def actualizar_posicion(self):
        self.coordenada[0] += self.velocidad_x
        self.coordenada[1] += self.velocidad_y

    def colisionar_bloque(self):
        self.velocidad_x = 0 - self.velocidad_x

class flor(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite=c.sprite_flor

class estrella(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite=c.sprite_estrella

class champi(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite=c.sprite_champi