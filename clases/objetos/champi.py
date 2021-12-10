from clases.objetos.objeto import objeto
import constants as c
from clases.bloques.escalera import escalera
from clases.bloques.tuberia import tuberia



class champi(objeto):

    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_champi
        self.v_y= 0
        self.v_x = 1.2
        self.ancho = 15
        self.alto = 15

    def actualizar(self, bloques):
        self.sufrir_gravedad()
        self.colisionar_bloques(bloques)
        self.actualizar_posicion()

    def colisionar_bloques(self, bloques: list):
        for bloque in bloques:
            n_suelo = False  # Nos permite saber si está tocando una superficie para que no siga precipitándose a la nada
            # animación de la seta subiendo, estática en el sitio hasta que llegue a la parte de arriba quedándose quieto en las x
            if self.colisionando(bloque) and self.coord_iniciales[1]-c.alto_champi/2 + 1 < self.coord[1] and not self.coord[1] > self.coord_iniciales[1] and self.coord[0] == self.coord_iniciales[0]  :
                self.v_y = -0.1
                self.v_x = 0

            elif self.colisionando(bloque):  # comprueba si hay colision
                #salto de la seta justo cuando sale de un objeto de interrogación
                if self.colisionando(bloque) and self.coord_iniciales[1]-c.alto_champi/2 < self.coord[1] and not self.coord[1] > self.coord_iniciales[1] :
                    self.v_x = 1.2
                    self.coord[1] -= 30
                    self.v_y = -3

                # comprueba si la colision es por encima
                elif ((abs(bloque.coord[1]-(self.coord[1]+self.alto))) <= self.alto):
                    self.v_y = 0
                    #choque lateral con los bloques y cambio de sentido solo con los bloques no movibles y tuberias yas que otros tipos podrían dar pie a errores y estos son los únicos a la altura del suelo
                    if not isinstance(bloque, escalera) and not isinstance(bloque, tuberia) and self.coord[1] > self.coord_iniciales[1] :
                        self.coord[1] = bloque.coord[1] - self.alto
                    
                    n_suelo = True  # Es importante para que no se enbucle el suelo
                    # Salto de la estrella
                    self.v_y = c.v_gravedad
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