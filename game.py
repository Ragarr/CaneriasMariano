import pyxel
from clases import bloque
from clases import player
from clases import npc
from clases import objeto
from clases import atrezzo
class App():
    def __init__(self) -> None:
        
        pyxel.init(100, 100, caption="test")
        pyxel.load("assets/test_resource.pyxres")
        

        self.jugador = player.mario([20, 12]) ##
        self.bloques = [bloque.interrogacion([20, 20]), bloque.ladrillo_no_rompible(
            [28, 20]), bloque.ladrillo_con_monedas([36, 20]), bloque.ladrillo_rompible([44, 20]),bloque.tuberia([52,20])]
        self.objetos = [objeto.objeto([20, 28], 0), objeto.objeto(
            [28, 28], 3), objeto.objeto([36, 28], 4), objeto.objeto([44, 28], 5), objeto.objeto([52, 28], 6)]
        self.npcs=[npc.goompa([20,36]),npc.koopa_tropa([28,36])]
        self.atrezzo=[atrezzo.arbusto([20,44]),atrezzo.montaña([28,44]),atrezzo.nube([36,44])]



        # esto tiene que ir al final del init

        pyxel.run(self.update(), self.draw())

    def update(self):
        if pyxel.btnp(pyxel.KEY_E):
            self.bloques[0].
        pass
    

    def draw(self):
        pyxel.cls(0)
        for i in range(len(self.bloques)):
            pyxel.blt(*self.bloques[i].coord,*self.bloques[i].sprite)
        for i in range(len(self.objetos)):
            pyxel.blt(*self.objetos[i].coord, *self.objetos[i].sprite)
        for i in range(len(self.npcs)):
            pyxel.blt(*self.npcs[i].coord, *self.npcs[i].sprite)
        for i in range(len(self.atrezzo)):
            pyxel.blt(*self.atrezzo[i].coord, *self.atrezzo[i].sprite)
        pyxel.blt(*self.jugador.coord,*self.jugador.sprite)

        
App()