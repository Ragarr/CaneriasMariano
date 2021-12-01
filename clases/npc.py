"""if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()"""
import pyxel
import constants as c
class npc():
    def __init__(self, coord: list, sprite: list  ) -> None:
        self.__sprite = sprite
        self.__coord = coord
        self.__esta_vivo = True # El npc está vivo 
        self.__v_x = c.v_npc  # La v_x habrá que modificarla según probemos
        self.__v_y = 0
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
    @property
    def sprite(self):
        return self.__sprite

    @sprite.setter
    def sprite(self, new_sprite: list):
        if not isinstance(new_sprite, list):
            raise ValueError("el sprite deben ser una lista")
        if len(new_sprite) != 6:
            raise ValueError("la lista sprite debe tener exactamente 6 elementos")
        self.__sprite = new_sprite
    @property
    def coord(self):
        return self.__coord
    @coord.setter
    def coord(self, coord):
        self.__coord = coord
    @property
    def esta_vivo(self):
        return self.__esta_vivo
    @esta_vivo.setter
    def esta_vivo(self, esta_vivo:bool):
        self.__esta_vivo=esta_vivo
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
    
    def colisionar_bloque(self):
        '''Se llama  cuando el npc colisiona y queremos que cambia su moviento al sentido contrario'''
        self.v_x = -self.v_x
    


    def actualizar_posicion(self):
       self.coord[0]+=self.v_x
       self.coord[1] += self.v_y

    def morir(self):
        self.esta_vivo = False
        self.sprite = [0, 0, 0, 0, 0, c.azul]

class goompa(npc):
    def __init__ (self, coord: list) -> None:
        # Esto hay que modificarlo cuando tengamos los sprites
        super().__init__(coord=coord, sprite=c.sprite_goompa)
        self.ancho = c.ancho_goompa
        self.alto = c.alto_goompa
    def colisionar_jugador(self):
        self.sprite=c.sprite_goompa_aplastado
        self.morir()
    def colisionar_npc(self,npc):
        if npc.es_caparazon:
            self.morir()
        else:
            self.colisionar_bloque()

    def actualizar_estado(self, bloques: list, npcs: list):

        for bloque in bloques:
            if (abs(bloque.coord[0]-self.coord[0]) < self.ancho
                    and abs(bloque.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
                self.colisionar_bloque()


        for npc in npcs:
            if (abs(npc.coord[0]-self.coord[0]) < self.ancho and abs(npc.coord[1]-self.coord[1]) < self.alto
                    and npc.esta_vivo):

                self.colisionar_npc(npc)


        self.actualizar_posicion()


class koopa_troopa(npc):
    def __init__ (self, coord: list) -> None:
        super().__init__ (coord=coord, sprite=c.sprite_koopa_troopa)#Esto hay que modificarlo cuando tengamos los sprites
        self.ancho = c.ancho_koopa_troopa
        self.alto = c.alto_koopa_troopa
        self.es_caparazon = False
        self.frame_concha= 400*c.fps

    def colisionar_jugador(self):
        if self.es_caparazon and self.v_x == 0:
            '''Si el caparazón está parado y el jugador choca con él lo pondrá en movimiento'''
            self.v_x = c.v_caparazon
        elif self.es_caparazon and self.v_x != 0:
            '''Emplearemos este método exclusivamente cuando el jugador salte encima del caparazón en movimiento'''
            self.v_x = 0
        else:
            '''Este último parámetro se refiere a cuando choca con el jugador de manera frontal, ya que este sigue su moviento'''
            self.es_caparazon = True
            self.frame_concha=pyxel.frame_count
            self.v_x = 0
            self.sprite = c.sprite_concha
            self.coord[1]+=5

    def actualizar_estado(self, bloques: list, npcs: list):
        if pyxel.frame_count-self.frame_concha >= c.frames_duracion_concha:
            self.frame_concha = 400*c.fps
            self.resurgir()

        for bloque in bloques:
            if (abs(bloque.coord[0]-self.coord[0]) < self.ancho
                    and abs(bloque.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
                self.colisionar_bloque()

        for npc in npcs:
            if (abs(npc.coord[0]-self.coord[0]) < self.ancho and abs(npc.coord[1]-self.coord[1]) < self.alto
                    and npc.esta_vivo):
                self.colisionar_bloque()

        self.actualizar_posicion()

    def resurgir(self):
        '''El koopa troopa volverá a su estado original pasado un tiempo '''
        if self.v_x<0:
            self.v_x = -c.v_koopa_troopa
        else:
            self.v_x = c.v_koopa_troopa
        self.es_caparazon = False
        self.coord[1]-=5
        self.sprite = c.sprite_koopa_troopa

a=koopa_troopa([1,1])
print(a.coord)
print(a.sprite)
