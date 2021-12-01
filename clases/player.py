
if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import pyxel
import constants as c
class mario():
    def __init__(self, coord: list) -> None:
    
        self.sprite = c.sprite_mario_quieto
        self.ancho = c.ancho_mario
        self.alto = c.alto_mario
        self.iniciar_temporizadores()
        self.iniciar_booleanos()
        self.iniciar_fuerzas()
        self.score = 0
        self.monedas = 0
        self.coord = coord  # ubicacion de el sprite

    def iniciar_temporizadores(self):

        """timers en frames para las animaciones """
        self.timer_andar = 0
        self.timer_invencible_animation = 0
        self.timer_inicio_invencibilidad = 0
        self.timer_transicion_fuego = 0
        self.timer_muerte = 0
        self.timer_transicion = 0 # animacion de transicion y frames de invulnerabilidad
        self.timer_fireball = 0 # animacion de la fireball
        self.timer_bandera = 0 # animacion de la mandera
    
    def iniciar_booleanos(self):
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
    
    def iniciar_fuerzas(self):
        self.v_x = 0
        self.v_y = 0

    def actualizar_posicion(self):  # cambia la posicion del personaje
        self.coord[0] += self.v_x
        self.coord[1] += self.v_y
    
    def actualizar_estado(self,bloques,npcs):
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
        #contacto con el suelo y gravedad
        if (self.coord[1] < pyxel.width):
            self.v_y += c.v_gravedad
        elif pyxel.btn(pyxel.KEY_SPACE):
            self.v_y = -c.v_salto
        else: 
            self.muerto=True

        # contacto con bloques
        for bloque in bloques:
                if (abs(bloque.coord[0]-self.coord[0]) < self.ancho
                    and abs(bloque.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
                    # comprueba si la colision es por debajo
                    if ((bloque.coord[1]+bloque.alto)-self.coord[1]) < bloque.alto:
                            # hay 2 pixeles de marjen
                            self.coord[1] = bloque.coord[1] + bloque.alto + 1
                            self.v_y += c.v_gravedad  # rebota con una velociadad de 0.7
                    if bloque.coord[1]-(self.coord[1]-self.alto) >= -0.1: # comprueba si la colision es por encima
                        # permite que se pueda saltar encima de los bloques, si se pone la velocidad
                        if pyxel.btn(pyxel.KEY_SPACE):
                            # en 0 directamente no podrias saltar
                            self.coord[1] = bloque.coord[1] - self.alto
                            self.v_y =-c.v_salto
                            # da la sensacion de que rebotas un pelin al golpear el bloque
                            self.v_x = 0.1*self.v_x
                        else:  # te pega al bloque
                            self.v_y = 0
                            # hace que te pongas en el pixel correcto y no atravieses el bloque
                            self.coord[1] = bloque.coord[1] - self.alto



        for npc in npcs:
                if (abs(npc.coord[0]-self.coord[0]) < self.ancho
                    and abs(npc.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
                    if ((npc.coord[0]-self.coord[0]+self.ancho) < 2
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

