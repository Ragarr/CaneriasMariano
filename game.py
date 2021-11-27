import pyxel
from clases import bloque
from clases import player
from clases import npc
from clases import objeto
from clases import atrezzo
class App():
    def __init__(self) -> None:
        
        pyxel.init(200, 100, caption="test",fps=60)
        pyxel.load("assets/test_resource.pyxres")
        

        self.jugador = player.mario([20, 12]) ##
        self.bloques = [bloque.interrogacion([20, 20]), bloque.ladrillo_no_rompible(
            [28, 20]), bloque.ladrillo_con_monedas([36, 20]), bloque.ladrillo_rompible([44, 20]),bloque.tuberia([52,20])]
        self.objetos = [objeto.objeto([20, 28], 0), objeto.objeto(
            [28, 28], 3), objeto.objeto([36, 28], 4), objeto.objeto([44, 28], 5), objeto.objeto([52, 28], 6)]
        self.npcs=[npc.goompa([20,36]),npc.koopa_troopa([29,36])]
        self.atrezzo=[atrezzo.arbusto([20,44]),atrezzo.montaña([28,44]),atrezzo.nube([36,44])]
        self.npcs[1].colisionar_bloque()


        # esto tiene que ir al final del init

        pyxel.run(self.update, self.draw)
    
    def update(self):
        
        for i in range(len(self.npcs)):
            if self.npcs[i].coord[0]<=0:
                self.npcs[i].colisionar_bloque()
                self.npcs[i].actualizar_posicion()
            elif self.npcs[i].coord[0] >= pyxel.width-self.npcs[i].ancho:
                self.npcs[i].colisionar_bloque()
                self.npcs[i].actualizar_posicion()
            elif self.npcs[0].coord[0] + 8 >= self.npcs[1].coord[0] and self.npcs[0].coord[0] <= self.npcs[1].coord[0] + 8:
                self.npcs[0].colisionar_bloque()
                self.npcs[1].colisionar_bloque()
                self.npcs[0].actualizar_posicion()
                self.npcs[1].actualizar_posicion()
                #He probado las colisiones entre el goompa y el koopa troopa(cambio de sentido linea 21)
                # He movido las cooordenadas del koopa en 1 ya que si están justo a la distancia se embuclan entre si 
                # he descubierto que cuando colisionan entre si por detras cambian de direccion y no deberian
                # aunque no se si es una situacion que se dara en el juego ya que creo que todos se mueven a la misma velocidad

                
            else:
                self.npcs[i].actualizar_posicion()
            
        

        
        
    

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
        pyxel.text(10,10,str(pyxel.frame_count),2)


        
App()