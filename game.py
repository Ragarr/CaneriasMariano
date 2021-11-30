import pyxel
from clases import bloque
from clases import player
from clases import npc
from clases import objeto
from clases import atrezzo
import constants as c
class App():
    def __init__(self) -> None:
        
        pyxel.init(c.ancho_pantalla, c.largo_pantalla, caption="test", fps=c.fps)
        pyxel.load("assets/test_resource.pyxres")
        self.contador = 0

        self.jugador = player.mario([20, 12]) 

        self.bloques = [bloque.interrogacion([20, 80]), bloque.ladrillo_no_rompible([28, 80]), 
                        bloque.ladrillo_con_monedas([36, 80]), bloque.ladrillo_rompible([44, 80]), 
                        bloque.tuberia([52, 80]), bloque.ladrillo_no_rompible([120, 92]), 
                        bloque.ladrillo_no_rompible([0, 92]), bloque.ladrillo_no_rompible([pyxel.width-8, 92])]
        # creacion del suelo
        self.bloques.append(bloque.suelo([0,pyxel.height*(2/3)]))


            
        self.objetos = [objeto.objeto([20, 72], 0), objeto.objeto([28, 72], 3), objeto.objeto([36, 72], 4), 
                        objeto.objeto([44, 72], 5), objeto.objeto([52, 72], 6)]
        
        self.npcs = [npc.goompa([20, 72]), npc.koopa_troopa([90, 92])]

        self.atrezzo=[atrezzo.arbusto([20,92]),atrezzo.montaña([28,92]),atrezzo.nube([36,92])]


        # esto tiene que ir al final del init

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jugador.actualizar_estado(self.bloques,self.npcs)
        for npc in self.npcs:
            npc.actualizar_estado(self.bloques , (other_npc for other_npc in self.npcs if other_npc != npc) ) # paso la lista de npcs exluyendo el npc a evaluar
        self.contador = 400-int(pyxel.frame_count/c.fps)
        

        

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

        
App()