
if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import pyxel
import constants as c
class mario():
    def __init__(self, coord: list) -> None:
    
        self.sprite = [0, 48, 0, 8, 8, 0]
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
        elif not pyxel.btn(pyxel.KEY_A) and self.mirando_derecha: # Deceleras si avancas hacia adelante y no pulsas la D ni la A
            self.v_x = max(self.v_x-c.v_rozamiento, 0)

        if pyxel.btn(pyxel.KEY_A):  # decelera si pulsas la D
            self.v_x = max(self.v_x-c.v_avance, -c.v_player_max_x)
        elif not pyxel.btn(pyxel.KEY_D) and not self.mirando_derecha: # Deceleras si avancas hacia detras y no pulsas la A ni la D
            self.v_x = min(self.v_x+c.v_rozamiento, 0)

        # evitar que el jugador salga de la pantalla
        if self.coord[0] < 0:
            self.v_x = 0.5
        elif self.coord[0] > pyxel.width-self.ancho:
            self.v_x = -0.5
        
        #mov jugador eje y
        #contacto con el suelo y gravedad
        if (self.coord[1] < 92):
            self.v_y += 0.25
        elif pyxel.btn(pyxel.KEY_SPACE):
            self.v_y = -4
        else: 
            self.v_y = 0

        # contacto con bloques
        for bloque in bloques:
            if (abs(bloque.coord[0]-self.coord[0]) < self.ancho
                    and abs(bloque.coord[1]-self.coord[1]) < self.alto): # comprueba si hay colision
                print("colision")
                if ((bloque.coord[1]+bloque.alto)-self.coord[1]) <2:    #comprueba si la colision es por debajo
                    self.coord[1] = bloque.coord[1] + bloque.alto - 2       # hay 2 pixeles de marjen
                    self.v_y = 0
                    self.coord[1] = self.coord[1]+2
                if bloque.coord[1]-(self.coord[1]-self.alto) > 2: #comprueba si la colision es por encima
                    if pyxel.btn(pyxel.KEY_SPACE): # permite que se pueda saltar encima de los bloques, si se pone la velocidad
                        self.coord[1] = bloque.coord[1] - self.alto # en 0 directamente no podrias saltar
                        self.v_y -= c.v_salto 
                        self.v_x =  0.1*self.v_x # da la sensacion de que rebotas un pelin al golpear el bloque
                    else: # te pega al bloque 
                        self.v_y = 0
                        self.coord[1] = bloque.coord[1] - self.alto -1 # hace que te pongas en el pixel correcto y no atravieses el bloque
            else:
                self.v_y += c.v_gravedad


        for npc in npcs:
            if (abs(npc.coord[0]-self.coord[0]) < self.ancho
                    and abs(npc.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
                if ((npc.coord[0]-self.coord[0]+self.ancho) < 2
                    and not self.en_transicion
                    and npc.esta_vivo):
                    print("colision en x ")
                    print("no hitbox ")
                elif ((npc.coord[1]-(self.coord[1]+self.alto)) < 2
                    and not abs(npc.coord[0]-self.coord[0]) < 2
                    and not self.en_transicion
                    and npc.esta_vivo):
                    print("colision en y ")
                    npc.morir()
                    print("npc muerto")
                    self.v_y = -2
                    self.score += 1000

        self.actualizar_posicion()

    