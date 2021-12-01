import pyxel
from clases import bloque
from clases import player
from clases import npc
from clases import objeto
from clases import atrezzo
import constants as c
class App():
    def __init__(self) -> None:
        
        pyxel.init(c.ancho_pantalla, c.alto_pantalla, caption="test", fps=c.fps)
        pyxel.load(c.assets_path)
        self.contador = 0
        self.jugador = player.mario([20, 12])

        self.bloques = [bloque.ladrillo_con_monedas([100,110]),bloque.ladrillo_no_rompible([115,125]),
<<<<<<< HEAD
                        bloque.ladrillo_no_rompible([0, c.altura_suelo-c.alto_ladrillo+1]),
                        bloque.ladrillo_no_rompible([c.ancho_pantalla-c.ancho_ladrillo, c.altura_suelo-c.alto_ladrillo+1]),
                        bloque.ladrillo_con_monedas([85, 110]), bloque.ladrillo_con_monedas([70, 110])]
=======
                        bloque.ladrillo_no_rompible([0, c.altura_suelo-c.alto_ladrillo]),
                        bloque.ladrillo_no_rompible([c.ancho_pantalla-c.ancho_ladrillo, c.altura_suelo-c.alto_ladrillo+1])]
>>>>>>> main
        # creacion del suelo
        x=0
        while x < pyxel.width:
            self.bloques.append(bloque.suelo([x, c.altura_suelo]))
            x+=c.ancho_suelo

        self.objetos = [objeto.champi([130, c.altura_suelo-15]), objeto.estrella([145, c.altura_suelo-15]),
                        objeto.flor([160,c.altura_suelo-15])]

        self.npcs = []

        self.atrezzo=[]


        # esto tiene que ir al final del init

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jugador.actualizar_estado(self.bloques,self.npcs,self.objetos,self.jugador)
        for npc in self.npcs:
            npc.actualizar_estado(self.bloques , (other_npc for other_npc in self.npcs if other_npc != npc) ) # paso la lista de npcs exluyendo el npc a evaluar
        for bloque in self.bloques:
            bloque.reposicionar()
        for objeto in self.objetos:
            objeto.actualizar(player.mario)
        self.contador = 400-int(pyxel.frame_count/c.fps)
        self.borrar_entidades(self.bloques, self.npcs, self.objetos)


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
        pyxel.text(70, 10, "COINS: {}".format(self.jugador.dinero), 0)
        pyxel.text(30,10,"MARIO",0)
        pyxel.text(30, 20, "{:06d}".format(self.jugador.score), 0)
        if self.jugador.muerto:
            pyxel.text(30, 30, "MUERTO", 0)
        else:
            pyxel.text(30, 30, "VIVO", 0)
    def borrar_entidades(self,bloques:list,npcs:list,objetos:list):
        i=0
        while i < len(bloques):
            bloque=bloques[i]
            if not bloque.existe:
                del(bloques[i])
            i+=1



        
App()