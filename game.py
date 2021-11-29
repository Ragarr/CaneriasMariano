import pyxel
from clases import bloque
from clases import player
from clases import npc
from clases import objeto
from clases import atrezzo
class App():
    def __init__(self) -> None:
        
        pyxel.init(256, 150, caption="test",fps=40)
        pyxel.load("assets/test_resource.pyxres")
        self.contador = 0

        self.jugador = player.mario([20, 12]) 
        self.bloques = [bloque.interrogacion([20, 80]), bloque.ladrillo_no_rompible(
            [28, 80]), bloque.ladrillo_con_monedas([36, 80]), bloque.ladrillo_rompible([44, 80]),bloque.tuberia([52,80])]
        self.objetos = [objeto.objeto([20, 72], 0), objeto.objeto(
            [28, 72], 3), objeto.objeto([36, 72], 4), objeto.objeto([44, 72], 5), objeto.objeto([52, 72], 6)]
        self.npcs=[npc.goompa([20,92]),npc.koopa_troopa([90,92])]
        self.atrezzo=[atrezzo.arbusto([20,92]),atrezzo.montaña([28,92]),atrezzo.nube([36,92])]


        # esto tiene que ir al final del init

        pyxel.run(self.update, self.draw)
    

    def update(self):

        self.actualizar_npcs()
        self.actualizar_jugador()
        self.contador = 400-int(pyxel.frame_count/60)
        

        

    def draw(self):
        pyxel.cls(12)
        for i in range(len(self.bloques)):
            pyxel.blt(*self.bloques[i].coord,*self.bloques[i].sprite)
        for i in range(len(self.objetos)):
            pyxel.blt(*self.objetos[i].coord, *self.objetos[i].sprite)
        for i in range(len(self.npcs)):
            pyxel.blt(*self.npcs[i].coord, *self.npcs[i].sprite)
        for i in range(len(self.atrezzo)):
            pyxel.blt(*self.atrezzo[i].coord, *self.atrezzo[i].sprite)
        pyxel.blt(*self.jugador.coord,*self.jugador.sprite)
        pyxel.text(pyxel.width-20,10,str(self.contador),0)
        pyxel.text(70, 10, "COINS: {}".format(self.jugador.monedas), 0)
        pyxel.text(30,10,"MARIO",0)
        pyxel.text(30, 20, "{:06d}".format(self.jugador.score), 0)
        if self.jugador.vivo:
            pyxel.text(30, 30, "VIVO", 0)
        else:
            pyxel.text(30, 30, "MUERTO", 0)


    

    def actualizar_jugador(self):

        # actualizar hitbox (para cuando es golpeado)
        if abs(self.jugador.frame_golpe -pyxel.frame_count) == 90:
            self.jugador.tiene_hitbox=True
            print("si hitbox")

        # movimiento jugador eje x
        """para que el jugador frene igual que en mario original es necesario que cambie su velocidad lentamente, como si tuviera inercia
        por ello necesitamos crear dos variables booleanas que marcan si se esta frenando para que los condicionales de reducir la velocidad
        en x para alcanzar 0 y el de aumentar la velocidad x para alcanzar 0 no se superpongan """

        frenando_palante = True if self.jugador.velocidad_x > 0 else False  # determina si vas hacia alante para saber en que direccion frenar
        frenando_patras = True if self.jugador.velocidad_x < 0 else False   # determina si vas hacia atras para saber en que direccion frenar

        if pyxel.btn(pyxel.KEY_D):  # acelera si pulsas la D
            self.jugador.velocidad_x = min(self.jugador.velocidad_x+0.2, 2)
        elif not pyxel.btn(pyxel.KEY_A) and frenando_palante: # Deceleras si avancas hacia adelante y no pulsas la D ni la A
            self.jugador.velocidad_x = max(self.jugador.velocidad_x-0.1, 0)

        if pyxel.btn(pyxel.KEY_A):  # decelera si pulsas la D
            self.jugador.velocidad_x = max(self.jugador.velocidad_x-0.2, -2)
        elif not pyxel.btn(pyxel.KEY_D) and frenando_patras: # Deceleras si avancas hacia detras y no pulsas la A ni la D
            self.jugador.velocidad_x = min(self.jugador.velocidad_x+0.1, 0)

        # evitar que el jugador salga de la pantalla
        if self.jugador.coord[0] < 0:
            self.jugador.velocidad_x = 0.5
        elif self.jugador.coord[0] > pyxel.width-self.jugador.ancho:
            self.jugador.velocidad_x = -0.5
        


        #mov jugador eje y
        #contacto con el suelo y gravedad
        if (self.jugador.coord[1] < 92):
            self.jugador.velocidad_y += 0.25
        elif pyxel.btn(pyxel.KEY_SPACE):
            self.jugador.velocidad_y = -4
        else: 
            self.jugador.velocidad_y = 0

        # contacto con bloques
        for bloque in self.bloques:
            if (abs(bloque.coord[0]-self.jugador.coord[0]) < self.jugador.ancho
                    and abs(bloque.coord[1]-self.jugador.coord[1]) < self.jugador.alto): # comprueba si hay colision
                print()







        # --------------------------------contacto con npcs en progreso------------------
        for npc in self.npcs:
            if (abs(npc.coord[0]-self.jugador.coord[0]) < self.jugador.ancho
                    and abs(npc.coord[1]-self.jugador.coord[1]) < self.jugador.alto):  # comprueba si hay colision
                if ((npc.coord[0]-self.jugador.coord[0]+self.jugador.ancho)<2
                    and self.jugador.tiene_hitbox
                    and npc.esta_vivo):
                    print("colision en x ")
                    print("no hitbox ")
                    self.jugador.recibir_daño()



                elif ((npc.coord[1]-(self.jugador.coord[1]+self.jugador.alto)) < 2 
                    and not abs(npc.coord[0]-self.jugador.coord[0]) < 2
                    and self.jugador.tiene_hitbox
                    and npc.esta_vivo):
                    print("colision en y ")
                    npc.morir() 
                    print("npc muerto")
                    self.jugador.velocidad_y = -2
                    self.jugador.score+=1000
    
        self.jugador.actualizar_posicion()


    def actualizar_npcs(self):
        #movimiento de los npcs
        for i in range(len(self.npcs)):
            if self.npcs[i].coord[0] <= 0:
                self.npcs[i].colisionar_bloque()
                self.npcs[i].actualizar_posicion()
            elif self.npcs[i].coord[0] >= pyxel.width-self.npcs[i].ancho:
                self.npcs[i].colisionar_bloque()
                self.npcs[i].actualizar_posicion()
            elif (self.npcs[0].coord[0] + 8 >= self.npcs[1].coord[0] 
                  and self.npcs[0].coord[0] <= self.npcs[1].coord[0] + 8):
                self.npcs[0].colisionar_bloque()
                self.npcs[1].colisionar_bloque()
                self.npcs[0].actualizar_posicion()
                self.npcs[1].actualizar_posicion()
                #  si el spawn está justo a la distancia se embuclan entre si

            self.npcs[i].actualizar_posicion()

        
App()