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
        self.jugador = player.mario([230, 50])
        self.__generar_bloques()
        self.__generar_suelo()
        self.__generar_npcs()
        self.objetos = [objeto.champi([130, c.altura_suelo-15]), objeto.estrella([145, c.altura_suelo-15]),
                        objeto.flor([160,c.altura_suelo-15])]

        

        self.atrezzo=[]


        # esto tiene que ir al final del init

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jugador.actualizar_estado(self.__bloques,self.npcs,self.objetos,self.jugador)
        self.__borrar_entidades(self.__bloques, self.npcs, self.objetos)
        self.mantener_jugador_en_pantalla()
        for npc in self.npcs:
            npc.actualizar_estado(self.__bloques , (other_npc for other_npc in self.npcs if other_npc != npc) ) # paso la lista de npcs exluyendo el npc a evaluar
        for bloque in self.__bloques:
            bloque.reposicionar()
        for objeto in self.objetos:
            objeto.actualizar(player.mario)
        self.contador = 400-int(pyxel.frame_count/c.fps)



    def draw(self):
        pyxel.cls(12)
        for i in range(len(self.__bloques)):
            pyxel.blt(self.redondear(self.__bloques[i].coord[0]),self.redondear(self.__bloques[i].coord[1]),*self.__bloques[i].sprite)
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
      
    def __borrar_entidades(self,bloques:list,npcs:list,objetos:list):
        i=0
        while i < len(bloques):
            bloque=bloques[i]
            if not bloque.existe:
                del(bloques[i])
            else:   
                i+=1
        i = 0
        while i < len(npcs):
            npc = npcs[i]
            if not npc.esta_vivo:
                del(npcs[i])
            else:
                i += 1
    def __generar_suelo(self):
        # creacion del suelo
        x = 0
        while x < 10*pyxel.width:
            self.__bloques.append(bloque.suelo([x, c.altura_suelo]))
            x += c.ancho_suelo
    def __generar_bloques(self):
        self.__bloques = [bloque.ladrillo_con_monedas([100,110]),bloque.bloque_no_movible([115,125]),
                        bloque.bloque_no_movible([0, c.altura_suelo-c.alto_ladrillo]),
                        bloque.bloque_no_movible([0, c.altura_suelo-2*c.alto_ladrillo]),
                        bloque.bloque_no_movible([0, c.altura_suelo-3*c.alto_ladrillo]),
                        bloque.ladrillo_con_monedas([85, 110]), bloque.ladrillo_con_monedas([70, 110])]
    def __generar_npcs(self):
        self.npcs = [npc.koopa_troopa([170, c.altura_suelo-c.alto_goompa]),npc.goompa([200, 110-c.alto_goompa])]

    def mantener_jugador_en_pantalla(self):
        if self.jugador.coord[0]<0:
            self.jugador.coord[0] =0
        if self.jugador.coord[0] > pyxel.width/2 and self.jugador.mirando_derecha:
            self.jugador.coord[0] = pyxel.width/2
            self.desplazar_nivel()

        
    def desplazar_nivel(self):
        for bloque in self.__bloques:
            bloque.coord[0]-=self.jugador.v_x
        for objeto in self.objetos:
            objeto.coord[0] -= self.jugador.v_x
        for npc in self.npcs:
            npc.coord[0] -= self.jugador.v_x

    def redondear(self,n:float)->int:
        return round(n-0.000001)
App()