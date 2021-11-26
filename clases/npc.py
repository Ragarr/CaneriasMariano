if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
import pyxel
import random

class npc():
    def __init__(self, coord: list, sprite: list  ) -> None:
        self.sprite = sprite
        self.coord = coord
        self.vivo = True # El npc está vivo 
        """
        Cooord es una lista de 2 elementos que contiene la posicón de donde se pinta el sprite
        Sprite es una lista de 6 elementos 
        que contiene en este orden los siguienes valores n este orden:
        -el numero de banco del sprite
        -la pos x donde se inicia el sprite
        -la pos y donde se inicia el sprite
        -la pos x final del sprite
        -la pos y final del sprite
        -color de chroma
        """
        
        


class goompa(npc):
    def __init__ (self, coord: list) -> None:
        self.vivo = True
        super().__init__ (coord +[0 , 48, 72, 8, 8, 0])#Esto hay que modificarlo cuando tengamos los sprites
        self.coodenada = coord
        self.velocidad_x = -2 # La velocidad habrá que modificarla según probemos
        self.velocidad_y = 0 
        self.ancho = 8
        self.altura = 8
    def actualizar_posición(self):
        self.coordenada[0] += self.velocidad_x
        self.coordenada[1] += self.velocidad_y 
    def colisionar_bloque(self):
        self.velocidad_x = 0 - self.velocidad_x 
    def morir(self):
        self.vivo = False
        self.sprite = [0 , 56, 72, 8, 8, 0]


        


class koopa_tropa(npc):
    def __init__ (self, coord: list) -> None:
        self.vivo = True
        super().__init__ (coord +[0,48, 80, 8, 8, 0 ])#Esto hay que modificarlo cuando tengamos los sprites
        self.coodenada = coord
        self.velocidad_x = -2 # La velocidad habrá que modificarla según probemos
        self.velocidad_y = 0 
        self.ancho = 8
        self.altura = 8
        self.es_caparazon = False
    def actualizar_posicición(self):
        if self.es_caparazon:
            self.velocidad_x = 0
        self.coordenada[0] += self.velocidad_x
        self.coordenada[1] += self.velocidad_y 
