from clases.objetos.objeto import objeto
import constants as c
import pyxel
class estrella(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_estrella
        self.v_y= 1
        self.v_x = 1
        self.ancho = 15
        self.alto = 15
    def sufrir_gravedad_estrella(self):
        #Parametro diferenciador del resto de objetos para que la animación de la estrella sea más natural
        if (self.coord[1] < pyxel.height):
            self.v_y += 0.21
        else:
            self.morir()

    def colisionar_bloques(self, bloques: list):
        for bloque in bloques:
            n_suelo = False  # Nos permite saber si está tocando una superficie para que no siga precipitándose a la nada

            if self.colisionando(bloque):  # comprueba si hay colision
                # comprueba si la colision es por encima
                if ((abs(bloque.coord[1]-(self.coord[1]+self.alto))) <= self.alto):
                    self.v_y = 0
                    #choque lateral con los bloques y cambio de sentido solo con los bloques no movibles y tuberias yas que otros tipos podrían dar pie a errores y estos son los únicos a la altura del suelo
                    self.coord[1] = bloque.coord[1] - self.alto

                    self.coord[1] = self.coord[1]
                    self.v_y = -self.v_y
                    n_suelo = True  # Es importante para que no se enbucle el suelo
                    # Salto de la estrella
                    self.v_y = - 3
                if (abs((bloque.coord[0]+bloque.ancho)-self.coord[0]) <= self.ancho
                        and not n_suelo):
                    self.v_x = -self.v_x
                if (abs((bloque.coord[0]+bloque.ancho)-self.coord[0]) >= self.ancho
                        and not n_suelo):
                    self.v_x = -self.v_x
            if ( bloque.pared_derecha and bloque.coord[0]+bloque.ancho < self.coord[0] 
                and bloque.coord[0]+bloque.ancho +2 > self.coord[0] and self.coord[1] > bloque.coord[1]):
                    self.v_x = -self.v_x
            if ( bloque.pared_izquierda and self.coord[0]+self.ancho < bloque.coord[0] 
                and self.coord[0]+self.ancho + 2> bloque.coord[0] and self.coord[1] > bloque.coord[1]):
                     self.v_x = -self.v_x


    def colisionar_jugador(self):
        self.morir()


    def actualizar(self, bloques ):
       
        self.sufrir_gravedad_estrella()
        self.colisionar_bloques(bloques)
        self.actualizar_posicion()
        
