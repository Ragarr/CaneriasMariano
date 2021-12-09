import pyxel
from clases.suelo import suelo
from clases.escalera import escalera
from clases.ladrillo_con_monedas import ladrillo_con_monedas
from clases.ladrillo_rompible import ladrillo_rompible
from clases.tuberia import tuberia
from clases.interrogacion import interrogacion
from clases.moneda import moneda
from clases.champi import champi
from clases.estrella import estrella
from clases.flor import flor
from clases.bandera import bandera
from clases.mastil import mastil
from clases import player
from clases.goompa import goompa
from clases.koopa_troppa import koopa_troopa
from clases import atrezzo
import constants as c
class game():
    def __init__(self) -> None:
        pyxel.init(c.ancho_pantalla, c.alto_pantalla, caption="Cañerias Mariano", fps=c.fps)
        pyxel.load(c.assets_path)
        self.en_menu = True
        self.tiempo = c.tiempo # contador de la esquina superior derecha
        self.jugador = player.mario([1500, c.altura_suelo-15])
        self.__generar_bloques()
        self.__generar_suelo()
        self.__generar_npcs()
        self.__generar_objetos()
        self.__generar_atrezzo()
        pyxel.run(self.update,self.draw)

    def update(self):
        if self.en_menu: # comprueba si estamos en el menu de inicio para que no se ejecute el nivel
            if pyxel.btnp(pyxel.KEY_ENTER):
                self.en_menu=False
        elif self.jugador.muerto:  # comprueba si estamos en el menu de muerte para que no se ejecute el nivel
            if self.jugador.vidas <= 0:  # si no te quedan vidas reinicia el juego entero
                if pyxel.btnp(pyxel.KEY_ENTER):
                    self.reset_game()
            if pyxel.btnp(pyxel.KEY_ENTER):  # reinicia el nivel
                self.reset_level()
                self.jugador.muerto=False
        elif self.tiempo < 0:  # mueres si te quedas sin tiempo
            self.jugador.morir()

        else: # ejecucion normal del nivel tras comprobar que no estamos en un menu
            self.jugador.actualizar_estado(self.__bloques,self.npcs,self.objetos,self.jugador)
            self.__borrar_entidades(self.__bloques, self.npcs, self.objetos,self.atrezzo)
            self.__mantener_jugador_en_pantalla()
            for npc in self.npcs: # actualiza a los npcs uno por uno
                npc.actualizar_estado(self.__bloques , (other_npc for other_npc in self.npcs if other_npc != npc),self.objetos,self.jugador ) # hay que excluir al propio npc
            for bloque in self.__bloques: # actualiza los bloques uno por uno
                bloque.reposicionar()
            for objeto in self.objetos:  # actualiza los objetos uno por uno
                objeto.actualizar(self.__bloques)
            self.tiempo -= 1 if pyxel.frame_count%c.fps==0 else 0 # actualiza el contador de la derecha

            if self.jugador.juego_finalizado and pyxel.btnp(pyxel.KEY_ENTER): # reinicia al llegar al final del juego
                self.reset_game()
    
    def draw(self):
        
        if self.en_menu: #si estas en el menu de inicio dibuja solo el menu de inicio
            pyxel.cls(c.azul)
            pyxel.blt(0,0,*c.sprite_cartel)
        elif self.jugador.muerto:  # si estas en el menu de muerte dibuja solo el menu de muerte
            pyxel.cls(c.negro)
            if self.jugador.vidas <= 0: # si te has quedado sin vidas muestra la pantalla para reiniciar el juego
                pyxel.text(pyxel.width/2+c.ancho_mario+3, pyxel.height/2,"HAS MUERTO",c.blanco)
                pyxel.text(pyxel.width/2+c.ancho_mario+3, pyxel.height/2+10,"pulsa intro para reiniciar",c.blanco)
            else:  # si  no te has quedado sin vidas muestra la pantalla para reiniciar el nivel
                pyxel.blt(pyxel.width/2,pyxel.height/2, *self.jugador.sprite)
                pyxel.text(pyxel.width/2+c.ancho_mario+3, pyxel.height/2,"x  {}".format(self.jugador.vidas),c.blanco)
            
        else: # dibujado normal del nivel
            pyxel.cls(c.azul)
            #bloques, objetos, npcs y atrezzo
            for i in range(len(self.atrezzo)):
                pyxel.blt(*self.atrezzo[i].coord, *self.atrezzo[i].sprite)
            for i in range(len(self.objetos)):
                pyxel.blt(*self.objetos[i].coord, *self.objetos[i].sprite)
            for i in range(len(self.__bloques)):
                pyxel.blt(self.__redondear(self.__bloques[i].coord[0]),self.__redondear(self.__bloques[i].coord[1]),*self.__bloques[i].sprite)
            for i in range(len(self.npcs)):
                pyxel.blt(*self.npcs[i].coord, *self.npcs[i].sprite)
            
            #el jugador
            pyxel.blt(*self.jugador.coord,*self.jugador.sprite)
            if self.jugador.estrella:# hace la animacion del brillo del modo estrella   
                if pyxel.frame_count % (c.fps/6) == 0:
                    pyxel.blt(self.jugador.coord[0], self.jugador.coord[1],
                              *c.sprite_animacion_estrella_amarillo(self.jugador.alto))
                if pyxel.frame_count % (c.fps/10) == 0:
                    pyxel.blt(self.jugador.coord[0], self.jugador.coord[1],
                              *c.sprite_estrella)
            #timer
            pyxel.text(pyxel.width-40, 10, "TIME",c.blanco)
            pyxel.text(pyxel.width-20,10,str(self.tiempo),c.blanco)
            #monedas
            pyxel.blt(100,9,*c.sprite_moneda_chiquita)
            pyxel.text(103, 11, str(self.jugador.dinero), c.negro)
            #puntuacion mario
            pyxel.text(30, 10, "MARIO", c.blanco)
            pyxel.text(30, 20, "{:06d}".format(self.jugador.score), c.blanco)
        if self.jugador.juego_finalizado: # mensaje de final del juego
            pyxel.text(pyxel.width/4, pyxel.height/2,"GRACIAS POR JUGAR, PULSA INTRO PARA REINICIAR",c.blanco)
    
    def __generar_atrezzo(self):
        self.atrezzo = [atrezzo.arbusto([600, c.altura_suelo-12])]
       
    def __generar_objetos(self):
        self.objetos = [bandera([3000, 120]), mastil([3000, 110])]
    
    def __generar_suelo(self):
        """el suelo son bloques, pero es comodo y visual generarlos a parte"""
        x = 0
        while x < 1000:
            self.__bloques.append(suelo([x, c.altura_suelo]))
            x += c.ancho_suelo
        
        x+=45
        while x < 1335:
            self.__bloques.append(suelo([x, c.altura_suelo]))
            x += c.ancho_suelo
        x += 60
        while x < 2002:
            self.__bloques.append(suelo([x, c.altura_suelo]))
            x += c.ancho_suelo
        x=2035
        while x < 3000:
            self.__bloques.append(suelo([x, c.altura_suelo]))
            x += c.ancho_suelo
    
    def __generar_bloques(self):
        self.__bloques = [
            #primera tanda de bloques
            interrogacion([256,c.altura_suelo-55],True),ladrillo_rompible([301,c.altura_suelo-55]),
            interrogacion([316, c.altura_suelo-55], True),ladrillo_rompible([331,c.altura_suelo-55]),
            interrogacion([346, c.altura_suelo-55], False),ladrillo_rompible([361,c.altura_suelo-55]),
            interrogacion([331, c.altura_suelo-110],True),
            # escaleras de tuberias
            tuberia([415, c.altura_suelo-c.alto_smario-3], c.alto_smario+3),
            tuberia([565, c.altura_suelo-c.alto_smario-20], c.alto_smario+20),
            tuberia([715, c.altura_suelo-c.alto_smario-30], c.alto_smario+30),
            tuberia([865, c.altura_suelo-c.alto_smario-30], c.alto_smario+30),
            #segunda tanda de bloques despues de la caida
            ladrillo_rompible([1200, c.altura_suelo-55]),interrogacion([1215, c.altura_suelo-55], False),
            ladrillo_rompible([1230, c.altura_suelo-55]),
            #los bloques que van por encima de los anteriores
            ladrillo_rompible([1245, c.altura_suelo-110]),ladrillo_rompible([1260, c.altura_suelo-110]),
            ladrillo_rompible([1275, c.altura_suelo-110]),ladrillo_rompible([1290, c.altura_suelo-110]),
            ladrillo_rompible([1305, c.altura_suelo-110]),ladrillo_rompible([1320, c.altura_suelo-110]),
            ladrillo_rompible([1335, c.altura_suelo-110]),ladrillo_rompible([1350, c.altura_suelo-110]),
            ladrillo_rompible([1365, c.altura_suelo-110]),
            #tercera tanda 
            ladrillo_rompible([1415, c.altura_suelo-110]),ladrillo_rompible([1430, c.altura_suelo-110]),
            ladrillo_rompible([1445, c.altura_suelo-110]),interrogacion([1460, c.altura_suelo-110],True),
            ladrillo_rompible([1460, c.altura_suelo-55]),
            # cuarta 
            ladrillo_rompible([1550, c.altura_suelo-55]),ladrillo_rompible([1565, c.altura_suelo-55],True),
            #quinta

            #sexta
            ladrillo_rompible([1550, c.altura_suelo-55]),ladrillo_rompible([1580, c.altura_suelo-110]),
            ladrillo_rompible([1595, c.altura_suelo-110]),ladrillo_rompible([1610, c.altura_suelo-110]),
            #septima
            ladrillo_rompible([1660, c.altura_suelo-55]),ladrillo_rompible([1675, c.altura_suelo-55]),
            interrogacion([1660, c.altura_suelo-110],False),interrogacion([1675, c.altura_suelo-110], True),
            ladrillo_rompible([1645, c.altura_suelo-110]),ladrillo_rompible([1690, c.altura_suelo-110]),
            #octava escaleras
            #subida
            escalera([1720,c.altura_suelo-c.alto_escalera],c.alto_escalera,True),
            escalera([1735,c.altura_suelo-2*c.alto_escalera],2*c.alto_escalera,True),
            escalera([1750,c.altura_suelo-3*c.alto_escalera],3*c.alto_escalera,True),
            escalera([1765,c.altura_suelo-4*c.alto_escalera],4*c.alto_escalera,True),
            #bajada
            escalera([1810,c.altura_suelo-4*c.alto_escalera],4*c.alto_escalera,True),
            escalera([1825,c.altura_suelo-3*c.alto_escalera],3*c.alto_escalera,True),
            escalera([1840,c.altura_suelo-2*c.alto_escalera],2*c.alto_escalera,True),
            escalera([1855,c.altura_suelo-c.alto_escalera],c.alto_escalera,True),
            #novena escaleras
            #subida
            escalera([1932,c.altura_suelo-c.alto_escalera],c.alto_escalera,True),
            escalera([1947,c.altura_suelo-2*c.alto_escalera],2*c.alto_escalera,True),
            escalera([1962,c.altura_suelo-3*c.alto_escalera],3*c.alto_escalera,True),
            escalera([1977,c.altura_suelo-4*c.alto_escalera],4*c.alto_escalera,True),
            escalera([1992,c.altura_suelo-4*c.alto_escalera],4*c.alto_escalera,True),
            #bajada
            escalera([2035,c.altura_suelo-4*c.alto_escalera],4*c.alto_escalera,True),
            escalera([2050,c.altura_suelo-3*c.alto_escalera],3*c.alto_escalera,True),
            escalera([2065,c.altura_suelo-2*c.alto_escalera],2*c.alto_escalera,True),
            escalera([2080,c.altura_suelo-c.alto_escalera],c.alto_escalera,True),
            #decimo
            tuberia([2155,c.altura_suelo-c.alto_smario-3],c.alto_smario+3),
            ladrillo_con_monedas([2230,c.altura_suelo-55]),
            ladrillo_con_monedas([2245,c.altura_suelo-55]),
            interrogacion([2260,c.altura_suelo-55],True),ladrillo_rompible([2275,c.altura_suelo-55]),
            #undecimo
            tuberia([2390,c.altura_suelo-c.alto_smario-3],c.alto_smario+3),
            # parte diseñada por nosotros
            interrogacion([2465,c.altura_suelo-55],True),interrogacion([2495,c.altura_suelo-55],True),
            interrogacion([2525,c.altura_suelo-55],True),interrogacion([2495,c.altura_suelo-110],False),
            ]
    
    def __generar_npcs(self):
        self.npcs = [goompa([760,c.altura_suelo-c.alto_goompa]),goompa([800,c.altura_suelo-c.alto_goompa]),
            goompa([2280,c.altura_suelo-c.alto_goompa]),goompa([2300,c.altura_suelo-c.alto_goompa]),
            goompa([1330, c.altura_suelo-110-c.alto_goompa]),goompa([1350, c.altura_suelo-110-c.alto_goompa]),
            goompa([1470, c.altura_suelo-c.alto_goompa]),goompa([1490, c.altura_suelo-c.alto_goompa]),
            koopa_troopa([2495,c.altura_suelo-c.alto_koopa_troopa])
                    ]

    def __mantener_jugador_en_pantalla(self):
        """hace que el jugador no puda salir por la izquierda y si llega al centro mueve el nivel"""
        if self.jugador.coord[0]<0:
            self.jugador.coord[0] =0
        if self.jugador.coord[0] > pyxel.width/2:
            self.jugador.coord[0] = pyxel.width/2
            self.__desplazar_nivel()
     
    def __desplazar_nivel(self):
        """se asegura de que el jugador se mantiene en el centro de la pantalla trasmitiendo su movimiento a las demas entidades"""
        for bloque in self.__bloques:
            bloque.coord[0]-=self.jugador.v_x
        for objeto in self.objetos:
            objeto.coord[0] -= self.jugador.v_x
        for npc in self.npcs:
            npc.coord[0] -= self.jugador.v_x
        for decorado in self.atrezzo:
            decorado.coord[0] -= self.jugador.v_x

    def __redondear(self,n:float)->int:
        """esta funcion es necesaria para evitar que visualmente las entidades no vibren al desplazarse"""
        return round(n-0.000001) # el metodo round funciona un poco mal en este caso pero asi siempre redondea correctamente

    def reset_level(self):
        """reinicia el nivel manteniendo las vidas del jugador"""
        self.jugador.coord= [20,c.altura_suelo]
        self.jugador.dinero=0
        self.jugador.score=0
        self.tiempo = c.tiempo  # contador de la esquina superior derecha
        self.__generar_bloques()
        self.__generar_suelo()
        self.__generar_npcs()
        self.__generar_objetos()
        self.__generar_atrezzo()

    def reset_game(self):
        """reinicia el juego entero"""
        self.en_menu = True
        self.tiempo = c.tiempo  # contador de la esquina superior derecha
        self.jugador = player.mario([30, c.altura_suelo-15])
        self.__generar_bloques()
        self.__generar_suelo()
        self.__generar_npcs()
        self.__generar_objetos()
        self.__generar_atrezzo()

    def __borrar_entidades(self, bloques: list, npcs: list, objetos: list, decoracion: list):
        """un bucle que va recorriendo todas las entidades del juego viendo si deben ser eliminadas:
            las elimina si no existen(bloques y objetos),estan muertas(npcs) o salen por la izquierda de la pantalla,
            no elimina si sale spor la izquierda ya que influye negativamente en el rendimiento"""
        i = 0
        while i < len(bloques):  # revisa los bloques
                bloque = bloques[i]
                if not bloque.existe or bloque.coord[0] < -bloque.ancho:
                    del(bloques[i])
                else:
                    i += 1
        i = 0
        while i < len(npcs):  # revisa los npcs
            npc = npcs[i]
            if not npc.esta_vivo:
                del(npcs[i])
            else:
                i += 1
        i = 0
        while i < len(objetos):  # revisa los objetos
            objeto = objetos[i]
            if not objeto.existe:
                if isinstance(objeto, moneda):
                    self.jugador.score += c.punt_moneda
                del(objetos[i])
            else:
                i += 1

game()