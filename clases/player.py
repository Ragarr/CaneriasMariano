
if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import pyxel
import constants as c
class mario():
    def __init__(self, coord: list) -> None:
        self.__sprite = c.sprite_mario_quieto
        self.__ancho = c.ancho_mario
        self.__alto = c.alto_mario
        self.__iniciar_temporizadores()
        self.__iniciar_booleanos()
        self.__iniciar_fuerzas()
        self.__score = 0
        self.__dinero = 0
        self.__coord = coord  # ubicacion de el sprite
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
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, new_ancho):
        self.__ancho = new_ancho
    
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, new_alto):
        self.__ancho = new_alto

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, new_score):
        if not isinstance (new_score, int):
            raise ValueError('La puntación debe ser un número entero')
        if not new_score >= 0:
            raise ValueError('La puntación debe ser mayor que 0')
        self.__score = new_score
    @property
    def dinero(self):
        return self.__dinero
    
    @dinero.setter
    def dinero(self, new_dinero):
        if not isinstance (new_dinero, int):
            raise ValueError('Las dinero deben ser un número entero')
        if not new_dinero >= 0:
            raise ValueError('Las dinero deben ser mayor que 0')
        self.__dinero = new_dinero
    @property
    def coord(self):
        return self.__coord
    @coord.setter
    def coord(self, coord):
        if len(coord) != 2:
            raise ValueError('La lista coord tiene que tener exactamente 2 elementos')
        self.__coord = coord


    def __iniciar_temporizadores(self):

        """timers en frames para las animaciones """
        self.timer_andar = 0
        self.timer_invencible_animation = 0
        self.timer_inicio_invencibilidad = 0
        self.timer_transicion_fuego = 0
        self.timer_muerte = 0
        self.timer_transicion = 0 # animacion de transicion y frames de invulnerabilidad
        self.timer_fireball = 0 # animacion de la fireball
        self.timer_bandera = 0 # animacion de la mandera
    
    def __iniciar_booleanos(self):
        """boleanos para el comportamiento de mario"""
        self.mirando_derecha = True
        self.permitir_salto = True 
        self.muerto = False
        self.invencible = False  # modo estrella
        self.grande = False  # su estado de ser mario, super mario o con fuego
        self.fuego = False # su estado de ser mario, super mario o con fuego
        self.permitir_fireball = True
        self.en_transicion = False # para cuando cambia de estado
        self.perdiendo_invencibilidad = False # para la estrella
    
    def __iniciar_fuerzas(self):
        self.v_x = 0
        self.v_y = 0
    def actualizar_posicion(self):  # cambia la posicion del personaje
        self.coord[0] += self.v_x
        self.coord[1] += self.v_y
    
    def actualizar_estado(self,bloques:list,npcs:list,objetos:list,jugador):        
        """actualiza las velocidades, el tamaño y en general todos los atributos del jugador"""
        if pyxel.btn(pyxel.KEY_D):  # acelera si pulsas la D
            self.v_x = min(self.v_x+c.v_avance, c.v_player_max_x)
            self.mirando_derecha=True
        elif not pyxel.btn(pyxel.KEY_A) and self.mirando_derecha: # Deceleras si avancas hacia adelante y no pulsas la D ni la A
            self.v_x = max(self.v_x-c.v_rozamiento, 0)

        if pyxel.btn(pyxel.KEY_A):  # decelera si pulsas la D
            self.v_x = max(self.v_x-c.v_avance, -c.v_player_max_x)
            self.mirando_derecha=False
        elif not pyxel.btn(pyxel.KEY_D) and not self.mirando_derecha: # Deceleras si avancas hacia detras y no pulsas la A ni la D
            self.v_x = min(self.v_x+c.v_rozamiento, 0)

        # evitar que el jugador salga de la pantalla
        if self.coord[0] < 0:
            self.v_x = 0.5
        elif self.coord[0] > pyxel.width-self.ancho:
            self.v_x = -0.5
        
        #mov jugador eje y
        #gravedad
        if (self.coord[1] < pyxel.width):
            self.v_y += c.v_gravedad
        elif pyxel.btn(pyxel.KEY_SPACE):
            self.v_y = -c.v_salto
        else: 
            self.muerto=True

        # contacto con bloques

        for bloque in bloques:
            colision_superior=False
            colision_inferior=False
            if (bloque.tiene_hitbox and abs(bloque.coord[0]-self.coord[0]) < self.ancho
                and abs(bloque.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
                if ((bloque.coord[1]+bloque.alto)-self.coord[1]) <= self.alto and not colision_superior:
                    #print("colision inferior con {}".format(type(bloque)))
                    bloque.golpear(objetos,jugador)
                    self.v_y = 2*c.v_gravedad
                    colision_inferior = True
                if ((abs(bloque.coord[1]-(self.coord[1]+self.alto)))  <= self.alto and not colision_inferior):  # comprueba si la colision es por encima
                    #print("colision superior con {}".format(type(bloque)))
                    colision_superior=True
                    self.coord[1]=bloque.coord[1]-self.alto
                    # permite que se pueda saltar encima de los bloques, si se pone la velocidad
                    if (pyxel.btn(pyxel.KEY_SPACE)):
                        self.v_y =-c.v_salto
                    else:  # te pega al bloque
                        self.v_y = 0
                if ((bloque.coord[0]+bloque.ancho)-self.coord[0]<=self.ancho
                    and not colision_superior):
                    self.v_x= - self.v_x
                    #print("colision izquierda con {}".format(type(bloque)))


        for npc in npcs:
            if (abs(npc.coord[0]-self.coord[0]) < self.ancho
                and abs(npc.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
                if ((npc.coord[0]-self.coord[0]+self.ancho) < c.tolerancia_colisiones
                        and not self.en_transicion
                            and npc.esta_vivo):
                        self.recibir_daño()

                elif ((npc.coord[1]-(self.coord[1]+self.alto)) < self.alto
                    and not abs(npc.coord[0]-self.coord[0]) < 2
                    and not self.en_transicion
                    and npc.esta_vivo):
                    npc.colisionar_jugador()
                    self.v_y = -c.v_rebote
                    self.score += 1000

        self.actualizar_posicion()
    
    def convertir_en_supermario(self):
        self.sprite=c.sprite_smario_quieto
        self.alto=c.alto_smario
        self.ancho=c.ancho_mario
    def recibir_daño(self):
        if self.fuego:
            self.fuego=False
            self.grande=True
        elif self.grande:
            self.grande=False
        else:
            self.morir()
    def morir(self):
        pass

