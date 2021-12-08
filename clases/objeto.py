

if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()

import constants as c
import pyxel
import clases.bloque

 


class objeto():
    def __init__(self, coord: list) -> None:

        self.__coord = coord
        self.__coord_iniciales = coord.copy()
        self.__v_x = 0
        self.__v_y = 0
        self.__esta_activo = True
        self.__existe = True
        self.tiene_hitbox = True
        
    @property
    def v_x(self):
        return self.__v_x
    @v_x.setter
    def v_x(self, new_v_x):
        self.__v_x=new_v_x




    @property
    def coord_iniciales(self):
        return self.__coord_iniciales
    @property
    def existe(self):
        return self.__existe

    @property
    def coord(self):
        return self.__coord
    @coord.setter
    def coord(self, new_coord):
        if len(new_coord) != 2:
            raise ValueError('La lista coord tiene que tener exactamente 2 elementos')
        self.__coord = new_coord
    @property
    def v_x(self):
        return self.__v_x
    @v_x.setter
    def v_x(self,new_v_x):
        if not isinstance(new_v_x,(float,int)):
            raise ValueError('La velocidad debe ser un entero o float')
        self.__v_x=new_v_x
    @property
    def v_y(self):
        return self.__v_y
    @v_y.setter
    def v_y(self,new_v_y):
        if not isinstance(new_v_y, (float, int)):
            raise ValueError('La velocidad debe ser un entero o float')
        self.__v_y = new_v_y
    @property
    def esta_activo(self):
        return self.__esta_activo
    @esta_activo.setter
    def esta_activo(self,esta_activo:bool):
        if not isinstance(esta_activo, bool):
            raise ValueError('el estado de activo debe ser un valor booleano')
        self.__esta_activo=esta_activo
    @property
    def existe(self):
        return self.__existe
    @existe.setter
    def existe (self,new_existe:bool):
        if not isinstance(new_existe, bool):
            raise ValueError('el estado de activo debe ser un valor booleano')
        self.__existe= new_existe
    def morir(self):
        self.__existe = False
    
    def actualizar_posicion(self):
        self.coord[0] += self.v_x
        self.coord[1] += self.v_y
    def colisionando(self,bloque):
        if (bloque.tiene_hitbox and abs(bloque.coord[0]-self.coord[0]) < self.ancho
                and abs(bloque.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
            return True
        else:
            return False
    def sufrir_gravedad(self):
        # Influye en los objetos a forma de gravedad para atraerlos al suelo
        if (self.coord[1] < pyxel.height):
            self.__v_y += c.v_gravedad
        else:
            self.morir()
    

class mastil(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite=c.sprite_mastil
        self.coord=coord
        self.ancho = 2
        self.alto = 152

    def colisionar_jugador(self,):
        pass

class bandera(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_bandera
        self.coord = coord
        self.ancho = 15
        self.alto = 152

    def colisionar_jugador(self,):
        self.v_y=1

    def actualizar(self, player):
        self.actualizar_posicion()

 
class flor(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_flor
        self.ancho = 15
        self.alto = 15
        self.v_y = -1   

    def actualizar(self, player):
        if self.coord[1] <= self.coord_iniciales[1]+8:
            self.v_y += 0.1
        else:
            self.v_y = 0
        self.actualizar_posicion()
    
    def colisionar_bloques(self, bloques: list):
        for bloque in bloques:
            n_suelo = False  # Nos permite saber si está tocando una superficie para que no siga precipitándose a la nada
            # animación de la seta subiendo, estática en el sitio hasta que llegue a la parte de arriba quedándose quieto en las x
            if self.colisionando(bloque) and self.coord_iniciales[1]-c.alto_champi/2 + 1 < self.coord[1] and isinstance(bloque, clases.bloque.interrogacion) and not isinstance(self, estrella):
                self.v_y = -0.1
                self.v_x = 0

    def colisionar_jugador(self):
        self.morir()

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
                    if not isinstance(bloque, clases.bloque.escalera) and not isinstance(bloque, clases.bloque.tuberia):
                        self.coord[1] = bloque.coord[1] - self.alto
                    else:
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
            if self.colisionando(bloque) and self.coord_iniciales[1]-c.alto_champi/2 + 1 < self.coord[1] and isinstance(bloque, clases.bloque.interrogacion):
                self.v_y = -0.1
                self.v_x = 0

            elif self.colisionando(bloque):  # comprueba si hay colision
                #salto de la seta justo cuando sale de un objeto de interrogación
                if self.colisionando(bloque) and self.coord_iniciales[1]-c.alto_champi/2 < self.coord[1] and isinstance(bloque, clases.bloque.interrogacion):
                    self.v_x = 1.2
                    self.coord[1] -= 10
                    self.v_y = -3

                # comprueba si la colision es por encima
                elif ((abs(bloque.coord[1]-(self.coord[1]+self.alto))) <= self.alto):
                    self.v_y = 0
                    #choque lateral con los bloques y cambio de sentido solo con los bloques no movibles y tuberias yas que otros tipos podrían dar pie a errores y estos son los únicos a la altura del suelo
                    if not isinstance(bloque, clases.bloque.escalera) and not isinstance(bloque, clases.bloque.tuberia):
                        self.coord[1] = bloque.coord[1] - self.alto
                    else:
                        self.coord[1] = self.coord[1]
                        self.v_y = -self.v_y
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
        
class moneda(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_moneda_girada
        self.duracion_frames = pyxel.frame_count+c.fps/3 # durara en pantalla 0.2secs
        self.v_y=-1.5 # asi la moneda subira al aparecer
        self.ancho=9

    def actualizar(self,player):
        if self.duracion_frames > pyxel.frame_count and pyxel.frame_count % (c.fps/15) == 0:
            self.girar()
        elif self.duracion_frames > pyxel.frame_count:
            pass
        else:
            self.morir()
        self.actualizar_posicion()
 

    def girar(self):
        if self.sprite == c.sprite_moneda_girada:
            self.sprite = c.sprite_moneda
        else:
            self.sprite = c.sprite_moneda_girada

    def colisionar_jugador(self):
        pass
class fireball(objeto):
    def __init__(self, coord: list, derecha: bool) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_fireball
        self.v_y = 1.5
        self.v_x = 3 if derecha else -3
        self.derecha = derecha
        self.ancho = 7
        self.alto = 7

    def sufrir_gravedad_estrella(self):
        #Parametro diferenciador del resto de objetos para que la animación de la estrella sea más natural
        if (self.coord[1] < pyxel.height):
            self.v_y += 0.21
        else:
            self.morir()

    def actualizar(self, bloques):

        self.sufrir_gravedad_estrella()
        self.colisionar_bloques(bloques)
        self.actualizar_posicion()

    def colisionar_bloques(self, bloques: list):
        for bloque in bloques:
            n_suelo = False  # Nos permite saber si está tocando una superficie para que no siga precipitándose a la nada

            if self.colisionando(bloque):  # comprueba si hay colision
                # comprueba si la colision es por encima
                if ((abs(bloque.coord[1]-(self.coord[1]+self.alto))) <= self.alto):
                    self.v_y = 0
                    #choque lateral con los bloques y cambio de sentido solo con los bloques no movibles y tuberias yas que otros tipos podrían dar pie a errores y estos son los únicos a la altura del suelo
                    self.coord[1] = self.coord[1]
                    self.v_y = -self.v_y
                    n_suelo = True  # Es importante para que no se enbucle el suelo
                    # Salto de la estrella
                    if self.derecha:
                        self.v_x -= 0.1
                    else:
                        self.v_x += 0.1
                    if abs(self.v_x) < 2.7:
                        self.morir()
                    self.v_y = - 3

                if (abs((bloque.coord[0]+bloque.ancho)-self.coord[0]) <= self.ancho
                        and not n_suelo):
                    self.v_x = -self.v_x
                if (abs((bloque.coord[0]+bloque.ancho)-self.coord[0]) >= self.ancho
                        and not n_suelo):
                    self.v_x = -self.v_x
            if ( bloque.pared_derecha and bloque.coord[0]+bloque.ancho < self.coord[0] 
                and bloque.coord[0]+bloque.ancho +4 > self.coord[0] and self.coord[1] > bloque.coord[1]):
                     self.morir()
            if ( bloque.pared_izquierda and self.coord[0]+self.ancho < bloque.coord[0] 
                and self.coord[0]+self.ancho + 4> bloque.coord[0] and self.coord[1] > bloque.coord[1]):
                     self.morir()

    def colisionar_jugador(self):
        pass
