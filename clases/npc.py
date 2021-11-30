if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import pyxel
import constants as c
class npc():
    def __init__(self, coord: list, sprite: list  ) -> None:
        self.sprite = sprite
        self.coord = coord
        self.esta_vivo = True # El npc está vivo 
        self.v_x = c.v_npc  # La velocidad habrá que modificarla según probemos
        self.v_y = 0
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

    def colisionar_bloque(self):
        '''Se llama  cuando el npc colisiona y queremos que cambia su moviento al sentido contrario'''
        self.v_x = -self.v_x
    
    def actualizar_estado(self,bloques:list,npcs:list):

        for bloque in bloques:
            if (abs(bloque.coord[0]-self.coord[0]) < self.ancho
                    and abs(bloque.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
                self.v_x = -self.v_x
                print("npc colisionando")

        for npc in npcs:
            if (abs(npc.coord[0]-self.coord[0]) < self.ancho and abs(npc.coord[1]-self.coord[1]) < self.alto):
                self.v_x =-self.v_x
                print("npc colisionando")

            
        self.actualizar_posicion()

    def actualizar_posicion(self):
       self.coord[0]+=self.v_x
       self.coord[1] += self.v_y

    def morir(self):
        self.esta_vivo = False
        self.sprite = [0, 120, 120, 0, 0, 0]

class goompa(npc):
    def __init__ (self, coord: list) -> None:
        super().__init__ (coord, [0 , 48, 72, 8, 8, 0])#Esto hay que modificarlo cuando tengamos los sprites
        self.ancho = c.ancho_goompa
        self.alto = c.alto_goompa

class koopa_troopa(npc):
    def __init__ (self, coord: list) -> None:
        super().__init__ (coord, [0,48, 80, 8, 8, 0 ])#Esto hay que modificarlo cuando tengamos los sprites
        self.ancho = c.ancho_koopa_troopa
        self.alto = c.alto_koopa_troopa
        self.es_caparazon = False

    def colisionar_jugador(self):
        if self.es_caparazon and self.v_x == 0:
            '''Si el caparazón está parado y el jugador choca con él lo pondrá en movimiento'''
            self.v_x = -5
        elif self.es_caparazon and self.velocidad != 0:
            '''Emplearemos este método exclusivamente cuando el jugador salte encima del caparazón en movimiento'''
            self.v_x = 0
        else:
            '''Este último parámetro se refiere a cuando choca con el jugador de manera frontal, ya que este sigue su moviento'''
            self.es_caparazon = True
            self.v_x = 0
            self.sprite = [0,56, 80, 8, 8, 0 ]
    def resurgir(self):
        '''El koopa troopa volverá a su estado original pasado un tiempo '''
        self.es_caparazon = False
        self.v_x = 2
        self.sprite = [0,48, 80, 8, 8, 0 ]