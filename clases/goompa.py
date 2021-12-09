import constants as c
from clases.npc import npc
import pyxel

class goompa(npc):
    def __init__ (self, coord: list) -> None:
        # Esto hay que modificarlo cuando tengamos los sprites
        super().__init__(coord=coord, sprite=c.sprite_goompa)
        self.ancho = c.ancho_goompa
        self.alto = c.alto_goompa
        self.es_caparazon=False
    
    def colisionar_jugador(self,jugador):
        self.morir(jugador)
    
    def morir(self,jugador):
        self.sprite = c.sprite_goompa_aplastado
        jugador.score += c.punt_goompa
        self.esta_vivo=False



    def actualizar_estado(self, bloques: list, npcs: list,objetos:list,jugador):
        if pyxel.width<self.coord[0]:
            pass
        else:
            self.sufrir_gravedad(jugador)
            self.colisionar_bloques(bloques)
            self.colisionar_npcs(npcs,jugador)
            self.actualizar_posicion()
            self.colisionar_con_objeto(objetos,jugador)
