
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
        self.__alto = new_alto

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
    @property
    def v_x(self):
        return self.__v_x
    @property
    def mirando_derecha(self):
        return self.__mirando_derecha

    def __iniciar_temporizadores(self):

        """timers en frames para las animaciones """
        self.__timer_andar = 0
        self.__timer_invencible_animation = 0
        self.__timer_inicio_invencibilidad = 0
        self.__timer_transicion_fuego = 0
        self.__timer_muerte = 0
        self.__timer_transicion = 0 # animacion de transicion y frames de invulnerabilidad
        self.__timer_fireball = 0 # animacion de la fireball
        self.__timer_bandera = 0 # animacion de la mandera
    
    def __iniciar_booleanos(self):
        """boleanos para el comportamiento de mario"""
        self.__andando=False
        self.__girando=False
        self.__mirando_derecha = True
        self.__permitir_salto = True 
        self.__muerto = False
        self.__invencible = False  # modo estrella
        self.__grande = True  # su estado de ser mario, super mario o con fuego
        self.__fuego = False # su estado de ser mario, super mario o con fuego
        self.__permitir_fireball = True
        self.__en_transicion = False # para cuando cambia de estado
        self.__perdiendo_invencibilidad = False # para la estrella
       
    def __iniciar_fuerzas(self):
        self.__v_x = 0
        self.__v_y = 0

    def __actualizar_posicion(self):  # cambia la posicion del personaje
        self.coord[0] += self.__v_x
        self.coord[1] += self.__v_y
    
    def actualizar_estado(self,bloques:list,npcs:list,objetos:list,jugador):        
        """actualiza las velocidades, el tamaño y en general todos los atributos del jugador"""
        if self.__grande:
            self.__convertir_en_supermario()
        self.__sufrir_gravedad()
        self.__colisonar_bloques(bloques,objetos,jugador)
        self.__colisionar_npcs(npcs)
        self.__detectar_botones()
        self.__actualizar_animaciones()
        self.__actualizar_posicion()
    
    def __convertir_en_supermario(self):
        self.sprite=c.sprite_smario_quieto
        self.alto=c.alto_smario
        self.ancho=c.ancho_mario
    def recibir_daño(self):
        if self.__fuego:
            self.__fuego=False
            self.__grande=True
        elif self.__grande:
            self.__grande=False
        else:
            self.__morir()
    def __morir(self):
        pass

    def __colisionando(self, entity):
        if (entity.tiene_hitbox and abs(entity.coord[0]-self.coord[0]) < self.ancho
                and abs(entity.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
            return True
        else:
            return False

    def __colisonar_bloques(self,bloques:list,objetos:list,jugador):
        self.__bloque_a_derecha=False
        self.__bloque_a_izquierda=False
        for bloque in bloques:
            colision_superior = False
            colision_inferior = False
            if self.__colisionando(bloque):  # comprueba si hay colision
                if abs(bloque.coord[1]+bloque.alto-self.coord[1]) <= c.tolerancia_colisiones and not colision_superior:
                    bloque.golpear(objetos, jugador)
                    self.__v_y = 2*c.v_gravedad
                    colision_inferior = True
                # comprueba si la colision es por encima
                elif ((abs(bloque.coord[1]-(self.coord[1]+self.alto))) <= self.alto and not colision_inferior):
                    #print("colision superior con {}".format(type(bloque)))
                    colision_superior = True
                    self.coord[1] = bloque.coord[1]-self.alto 
                    # permite que se pueda saltar encima de los bloques, si se pone la velocidad
                    if (pyxel.btn(pyxel.KEY_SPACE)):
                        self.__v_y = -c.v_salto
                    else:  # te pega al bloque
                        self.__v_y = 0
                """if (abs((bloque.coord[0]+bloque.ancho)-self.coord[0]) <= self.ancho
                        and not colision_superior): # jugador a la derecha del bloque
                    self.coord[0]+=2

                    
                elif (abs((bloque.coord[0])-self.coord[0]+self.ancho) >= self.ancho
                      and not colision_superior):  # jugador a la izquierda del bloque
                    self.coord[0] -= 2"""

                    #print("colision izquierda con {}".format(type(bloque)))

    def __colisionar_npcs(self,npcs:list):
        for npc in npcs:
            if self.__colisionando(npc):  # comprueba si hay colision
                if ((npc.coord[0]-self.coord[0]+self.ancho) < c.tolerancia_colisiones
                        and not self.__en_transicion
                        and npc.esta_vivo):
                    self.recibir_daño()

                elif ((npc.coord[1]-(self.coord[1]+self.alto)) < self.alto
                      and not abs(npc.coord[0]-self.coord[0]) < 2
                      and not self.__en_transicion
                      and npc.esta_vivo):
                    npc.colisionar_jugador()
                    self.__v_y = -c.v_rebote
                    self.score += 1000
    
    def __actualizar_animaciones(self):
        if self.__andando and not self.__grande:
            if self.sprite==c.sprite_mario_quieto and pyxel.frame_count%(c.fps/6)==0:
                self.sprite=c.sprite_mario_andando
            elif pyxel.frame_count % (c.fps/2) == 0:
                self.sprite=c.sprite_mario_quieto
        elif not self.__grande:
            self.sprite=c.sprite_mario_quieto
    
        if self.__andando and self.__grande:
            if self.sprite == c.sprite_smario_quieto and pyxel.frame_count % (c.fps/6) == 0:
                self.sprite = c.sprite_smario_andando1
            elif pyxel.frame_count % (c.fps/2) == 0:
                self.sprite = c.sprite_smario_quieto
        elif  self.__grande:
            self.sprite = c.sprite_smario_quieto

    def __sufrir_gravedad(self):
        #mov jugador eje y
        #gravedad
        if (self.coord[1] < pyxel.height):
            self.__v_y += c.v_gravedad
        else: 
            self.muerto=True
    def __detectar_botones(self):
        if pyxel.btn(pyxel.KEY_D) and not self.__bloque_a_derecha:  # acelera si pulsas la D
            self.__v_x = min(self.__v_x+c.v_avance, c.v_player_max_x)
            self.__mirando_derecha=True
            self.__andando=True
        elif not pyxel.btn(pyxel.KEY_A) and self.__mirando_derecha: # Deceleras si avancas hacia adelante y no pulsas la D ni la A
            self.__v_x = max(self.__v_x-c.v_rozamiento, 0)
            self.__andando=False

        if pyxel.btn(pyxel.KEY_A) and not self.__bloque_a_izquierda:  # decelera si pulsas la A
            self.__v_x = max(self.__v_x-c.v_avance, -c.v_player_max_x)
            self.__mirando_derecha=False
            self.__andando=True
        elif not pyxel.btn(pyxel.KEY_D) and not self.__mirando_derecha: # Deceleras si avancas hacia detras y no pulsas la A ni la D
            self.__v_x = min(self.__v_x+c.v_rozamiento, 0)
            self.__andando=False

