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
        super().__init__ (coord, [0 , 48, 72, 8, 8, 0])#Esto hay que modificarlo cuando tengamos los sprites
        self.coord = coord
        self.velocidad_x = -1 # La velocidad habrá que modificarla según probemos
        self.velocidad_y = 0 
        self.ancho = 8
        self.altura = 8
    def actualizar_posicion(self):
        '''Mueve al koppa troopa de posición'''
        self.coord[0] += self.velocidad_x
        self.coord[1] += self.velocidad_y 
    def colisionar_bloque(self):
        '''Se define para cuando el goompa colisiona y queremos que cambia su moviento al sentido contrario'''
        self.velocidad_x = ( - self.velocidad_x) 
    def morir(self, aplastado = False):
        self.vivo = False
        if aplastado:
            self.sprite = [0 , 56, 72, 8, 8, 0]#cambiar del goompa normal al aplastado, exlcusivamente cuando el Mario salte encima del goompa
        


        


class koopa_troopa(npc):
    def __init__ (self, coord: list) -> None:
        self.vivo = True
        super().__init__ (coord, [0,48, 80, 8, 8, 0 ])#Esto hay que modificarlo cuando tengamos los sprites
        self.coord = coord
        self.velocidad_x = 1 # La velocidad habrá que modificarla según probemos
        self.velocidad_y = 0 
        self.ancho = 8
        self.altura = 8
        self.es_caparazon = False
    def actualizar_posicion(self):
        '''Mueve al koppa troopa de posición'''
        self.coord[0] += self.velocidad_x
        self.coord[1] += self.velocidad_y 
    def colisionar_bloque(self):
        '''Se define para cuando el koopa toopa colisiona y queremos que cambia su moviento al sentido contrario'''
        self.velocidad_x = 0 - self.velocidad_x 
    def morir(self):
        self.vivo = False
    def colisionar_jugador(self, sentido =  None ):
        if self.es_caparazon and self.velocidad_x == 0:
            '''Si el caparazón está parado y el jugador choca con él lo pondrá en movimiento y seguirá un sentido dependiendo desde donde lo golpee el jugador'''
            if sentido == 'izquierda':
                self.velocidad_x = 5
            elif sentido == 'derecha':
                self.velocidad_x = -5
        elif self.es_caparazon and self.velocidad != 0:
            '''Emplearemos este método exclusivamente cuando el jugador salte encima del caparazón en movimiento'''
            self.velocidad_x = 0
        else:
            '''Este último parámetro se refiere a cuando choca con el jugador de manera frontal, ya que este sigue su moviento'''
            self.es_caparazon = True
            self.velocidad_x = 0
            self.sprite = [0,56, 80, 8, 8, 0 ]
    def resurgir(self):
        '''El koopa troopa volverá a su estado original pasado un tiempo para ello ejecutaremos este método'''
        self.es_caparazon = False
        self.velocidad_x = 2
        self.sprite = [0,48, 80, 8, 8, 0 ]