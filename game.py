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
        self.jugador = player.mario([125, 147])
        self.__generar_bloques()
        self.__generar_suelo()
        self.__generar_npcs()
        self.__generar_objetos()

        

        self.atrezzo=[]


        # esto tiene que ir al final del init

        pyxel.run(self.update, self.draw)

    def update(self):
        self.jugador.actualizar_estado(self.__bloques,self.npcs,self.objetos,self.jugador)
        self.__borrar_entidades(self.__bloques, self.npcs, self.objetos)
        self.__mantener_jugador_en_pantalla()
        for npc in self.npcs:
            npc.actualizar_estado(self.__bloques , (other_npc for other_npc in self.npcs if other_npc != npc),self.objetos ) # paso la lista de npcs exluyendo el npc a evaluar
        for bloque in self.__bloques:
            bloque.reposicionar()
        for objeto in self.objetos:
            objeto.actualizar(self.__bloques)
        self.contador = 400-int(pyxel.frame_count/c.fps)

    def draw(self):
        pyxel.cls(c.azul)
        for i in range(len(self.objetos)):
            pyxel.blt(*self.objetos[i].coord, *self.objetos[i].sprite)
        for i in range(len(self.__bloques)):
            pyxel.blt(self.__redondear(self.__bloques[i].coord[0]),self.__redondear(self.__bloques[i].coord[1]),*self.__bloques[i].sprite)
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
            if not bloque.existe or bloque.coord[0]< -bloque.ancho:
                print("bloque eliminado")
                del(bloques[i])
            else:   
                i+=1
        i = 0
        while i < len(npcs):
            npc = npcs[i]
            if not npc.esta_vivo or npc.coord[0] < -npc.ancho:
                print("npc eliminado")
                del(npcs[i])
            else:
                i += 1
        i = 0
        while i < len(objetos):
            objeto = objetos[i]
            if not objeto.existe or objeto.coord[0]< - objeto.ancho:
                print("objeto eliminado")
                del(objetos[i])
            else:
                i += 1
    
    def __generar_objetos(self):
        self.objetos = []
    
    def __generar_suelo(self):
        # creacion del suelo
        x = 0
        while x < 10*pyxel.width:
            self.__bloques.append(bloque.suelo([x, c.altura_suelo]))
            x += c.ancho_suelo
    
    def __generar_bloques(self):
        self.__bloques = [bloque.escalera([200, c.altura_suelo-15*3], 3, True), 
        bloque.escalera([200-17, c.altura_suelo-15*2], 2, False), bloque.escalera([200-17-17, c.altura_suelo-15], 1, False),
        bloque.escalera([300, c.altura_suelo-15*3], 3, True), 
        bloque.escalera([300+17, c.altura_suelo-15*2], 2, True), bloque.escalera([300+34, c.altura_suelo-15], 1, True), 
        bloque.ladrillo_rompible([400, c.altura_suelo-50], False), bloque.tuberia([600, c.altura_suelo-60], 60)
        ]
    
    def __generar_npcs(self):
        self.npcs = [npc.goompa([200,50])]

    def __mantener_jugador_en_pantalla(self):
        if self.jugador.coord[0]<0:
            self.jugador.coord[0] =0
        if self.jugador.coord[0] > pyxel.width/2 and self.jugador.mirando_derecha:
            self.jugador.coord[0] = pyxel.width/2
            self.__desplazar_nivel()
     
    def __desplazar_nivel(self):
        for bloque in self.__bloques:
            bloque.coord[0]-=self.jugador.v_x
        for objeto in self.objetos:
            objeto.coord[0] -= self.jugador.v_x
        for npc in self.npcs:
            npc.coord[0] -= self.jugador.v_x

    def __redondear(self,n:float)->int:
        return round(n-0.000001)
App()