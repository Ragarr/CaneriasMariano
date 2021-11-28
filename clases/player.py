
if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
import pyxel

class mario():
    def __init__(self, coord: list) -> None:
        self.score = 0
        self.monedas = 0
        self.tamaño = 0  # 0peque, 1supermario, 2con flor
        self.coord = coord  # ubicacion de el sprite
        self.velocidad_x=0
        self.velocidad_y=0
        self.sprite = [0, 48, 0, 8, 8, 0]
        self.ancho=8
        self.alto=8
        self.tiene_hitbox=True
        self.frame_golpe = 0
        self.es_grande=False
        self.es_flor=False
        self.vivo=True
    def actualizar_posicion(self): # cambia la posicion del personaje
        self.coord[0]+=self.velocidad_x
        self.coord[1]+=self.velocidad_y
    def recibir_daño(self):
        self.tiene_hitbox=False
        if self.es_flor:
            self.es_flor=False
            self.es_grande=True
        elif self.es_grande:
            self.es_grande=False
        else:
            self.vivo=False
        self.frame_golpe=pyxel.frame_count

    