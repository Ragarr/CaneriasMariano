if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import pyxel
from clases.bloque import suelo
import constants as c
from clases.objeto import fireball
class npc():
    def __init__(self, coord: list, sprite: list  ) -> None:
        self.__sprite = sprite
        self.__coord = coord
        self.__esta_vivo = True # El npc está vivo 
        self.__v_x = -c.v_npc  # La v_x habrá que modificarla según probemos
        self.__v_y = 0
        self.tiene_hitbox=True
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
    def coord(self, new_coord):
        if len(new_coord)!= 2:
            raise ValueError('La lista coord tiene que tener exactamente 2 elementos')
        self.__coord = new_coord
    @property
    def esta_vivo(self):
       return self.__esta_vivo
    @esta_vivo.setter
    def esta_vivo(self, new_esta_vivo:bool):
        if not isinstance(new_esta_vivo, bool):
            raise ValueError('El valor de estar vivo debe ser un booleano')
        self.__esta_vivo= new_esta_vivo
    @property
    def v_x(self):
        return self.__v_x
    @v_x.setter
    def v_x(self,new_v_x):
        if  not isinstance(new_v_x, (int, float)):
            raise ValueError('El valor de la velocidad es int o float')
        self.__v_x= new_v_x
    @property
    def v_y(self):
        return self.__v_y
    @v_y.setter
    def v_y(self,new_v_y):
        if  not isinstance(new_v_y, (int, float)):
            raise ValueError('El valor de la velocidad es int o float')
        self.__v_y=new_v_y

    def sufrir_gravedad(self):
        if (self.coord[1] < pyxel.height):
            self.__v_y += c.v_gravedad
        else:
            self.morir()
    
    def colisionar_bloques(self, bloques: list):
        for bloque in bloques:
            en_suelo = False

            if self.colisionando(bloque):  # comprueba si hay colision
                # comprueba si la colision es por encima
                if ((abs(bloque.coord[1]-(self.coord[1]+self.alto))) <= self.alto):
                    self.__v_y = 0
                
                    en_suelo= True if isinstance(bloque,suelo) else False
                else:
                    self.__v_y = c.v_gravedad

                if ((bloque.coord[0]+bloque.ancho)-self.coord[0] <= self.ancho
                        and not en_suelo):
                    self.__v_x = c.v_npc if not self.es_caparazon else c.v_caparazon
                if ((bloque.coord[0]+bloque.ancho)-self.coord[0] >= self.ancho
                      and not en_suelo):
                    self.__v_x = -c.v_npc if not self.es_caparazon else -c.v_caparazon
    
    def colisionar_npcs(self, npcs):
        for npc in npcs:
            if self.colisionando(npc):
                if npc.es_caparazon:
                    self.morir()
                else:
                    self.__v_x = -self.__v_x

    def actualizar_posicion(self):
       self.coord[0] += self.v_x
       self.coord[1] += self.v_y

    def morir(self):
        self.esta_vivo = False
        self.sprite = c.sprite_transparente

    def colisionando(self, entity):
        if (entity.tiene_hitbox and abs(entity.coord[0]-self.coord[0]) < self.ancho
                and abs(entity.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
            return True
        else:
            return False
    
    def colisionar_con_objeto(self,objetos:list,jugador):
        for objeto in objetos:
            if self.colisionando(objeto) and isinstance(objeto,fireball):
                jugador.score+=c.punt_goompa # ambas son iguales
                self.morir()


class goompa(npc):
    def __init__ (self, coord: list) -> None:
        # Esto hay que modificarlo cuando tengamos los sprites
        super().__init__(coord=coord, sprite=c.sprite_goompa)
        self.ancho = c.ancho_goompa
        self.alto = c.alto_goompa
        self.es_caparazon=False
    
    def colisionar_jugador(self,jugador):
        self.sprite=c.sprite_goompa_aplastado
        jugador.score+=c.punt_goompa
        self.morir()


    def actualizar_estado(self, bloques: list, npcs: list,objetos:list,jugador):
        if jugador.coord[0] + pyxel.width <self.coord[0]:
            pass
        else:
            self.sufrir_gravedad()
            self.colisionar_bloques(bloques)
            self.colisionar_npcs(npcs)
            self.actualizar_posicion()
            self.colisionar_con_objeto(objetos,jugador)


class koopa_troopa(npc):
    def __init__ (self, coord: list) -> None:
        super().__init__ (coord=coord, sprite=c.sprite_koopa_troopa)#Esto hay que modificarlo cuando tengamos los sprites
        self.ancho = c.ancho_koopa_troopa
        self.alto = c.alto_koopa_troopa
        self.es_caparazon = False
        self.frame_concha= 400*c.fps

    def colisionar_jugador(self,jugador):
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
            self.alto = c.alto_concha
            self.coord[1]-=15

    def actualizar_estado(self, bloques: list, npcs: list, objetos:list,jugador):
        if jugador.coord[0]+pyxel.width<self.coord[0]:
            pass
        else:
            self.sufrir_gravedad()
            self.colisionar_bloques(bloques)
            self.colisionar_npcs(npcs)
            self.colisionar_con_objeto(objetos,jugador)
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


