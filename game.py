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
        self.jugador.mover(self.bloques,self.npcs)
        self.actualizar_npcs()
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
        if self.jugador.muerto:
            pyxel.text(30, 30, "MUERTO", 0)
        else:
            pyxel.text(30, 30, "VIVO", 0)


    






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