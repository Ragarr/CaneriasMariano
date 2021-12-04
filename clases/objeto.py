

if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()

import constants as c
import pyxel
import clases.bloque

 


class suelo():
    def __init__(self, coord: list) -> None:
        # una vez que el profesor nos pase el archivo con los sprites
        super().__init__(coord, c.sprite_suelo, pyxel.width, pyxel.height/3)


class objeto():
    def __init__(self, coord: list) -> None:

        self.__coord = coord
        self.__coord_iniciales = coord.copy()
        self.__v_x = 0
        self.__v_y = 0
        self.__esta_activo = True
        self.__existe=True
        
    @property
    def coord_iniciales(self):
        return self.__coord_iniciales
    @property
    def existe(self):
        return self.__existe
    """@existe.setter
    def existe(self,new_existe):
        self.__existe=new_existe"""
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

    def morir(self):
        self.esta_vivo = False
        self.sprite = c.sprite_transparente
    def actualizar_posicion(self):
        self.coord[0] += self.v_x
        self.coord[1] += self.v_y
    def desaparecer(self):
        self.__existe=False
    def colisionando(self,bloque):
        if (bloque.tiene_hitbox and abs(bloque.coord[0]-self.coord[0]) < self.ancho
                and abs(bloque.coord[1]-self.coord[1]) < self.alto):  # comprueba si hay colision
            return True
        else:
            return False
    def sufrir_gravedad(self):
        if (self.coord[1] < pyxel.height):
            self.__v_y += c.v_gravedad
        else:
            self.morir()
    def colisionar_bloques(self, bloques: list):
        for bloque in bloques:
            n_suelo = False
            
            if self.colisionando(bloque) and  self.coord_iniciales[1]-c.alto_champi/2 +1 < self.coord[1] and  isinstance(bloque, clases.bloque.interrogacion) and not isinstance(self, estrella):
                self.v_y = -0.1
                self.v_x = 0
                
            
            elif self.colisionando(bloque):  # comprueba si hay colision
                if self.colisionando(bloque) and  self.coord_iniciales[1]-c.alto_champi/2  < self.coord[1] and  isinstance(bloque, clases.bloque.interrogacion) and  isinstance(self, champi ):
                    self.v_x = 1 
                    self.coord[1] -= 10
                    self.v_y = -3
                    
                    
                    
                # comprueba si la colision es por encima
                elif ((abs(bloque.coord[1]-(self.coord[1]+self.alto))) <= self.alto):
                    self.__v_y = 0
                    if not isinstance(bloque,clases.bloque.bloque_no_movible) and not isinstance(bloque, clases.bloque.tuberia):
                        self.coord[1] = bloque.coord[1] - self.alto
                    else:
                         self.coord[1]= self.coord[1]
                         self.v_y = -self.v_y
                    n_suelo= True 
                    self.v_y = -3 if isinstance(self, estrella) else c.v_gravedad
                if (abs((bloque.coord[0]+bloque.ancho)-self.coord[0]) <= self.ancho
                        and not n_suelo):
                    self.__v_x = -self.__v_x
                if (abs((bloque.coord[0]+bloque.ancho)-self.coord[0]) >= self.ancho
                      and not n_suelo):
                    self.__v_x = -self.__v_x 
        
    

                

class moneda(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_moneda_girada
        self.duracion_frames = pyxel.frame_count+c.fps/3 # durara en pantalla 0.2secs
        self.v_y=-1.5 


    

    
class flor(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_flor
        self.v_y = -1   

    def actualizar(self, player):
        if self.coord[1] <= self.coord_iniciales[1]:
            self.v_y += 0.1
        else:
            self.v_y = 0
        self.actualizar_posicion()


class estrella(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_estrella
        self.v_y= 1
        self.v_x = 1
        self.ancho = 15
        self.alto = 15
    def sufrir_gravedad_estrella(self):
        if (self.coord[1] < pyxel.height):
            self.v_y += 0.21
        else:
            self.morir()
    
    
    def actualizar(self, player):
        if self.coord[1]<=self.coord_iniciales[1]:
            self.v_y+=0.1
        else:
            self.v_y = 0
        self.actualizar_posicion()
    
    
    def actualizar(self, bloques ):
       
        self.sufrir_gravedad_estrella()
        self.colisionar_bloques(bloques)
        self.actualizar_posicion()
        

        
       
        
        
   

class champi(objeto):

    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_champi
        self.v_y= 0
        self.v_x = 1
        self.ancho = 15
        self.alto = 15

    def actualizar(self, bloques):
        self.sufrir_gravedad()
        self.colisionar_bloques(bloques)
        self.actualizar_posicion()
   
           
    


class moneda(objeto):
    def __init__(self, coord: list) -> None:
        super().__init__(coord)
        self.sprite = c.sprite_moneda_girada
        self.duracion_frames = pyxel.frame_count+c.fps/3 # durara en pantalla 0.2secs
        self.v_y=-1.5 # asi la moneda subira al aparecer

    def actualizar(self,player):
        if self.duracion_frames > pyxel.frame_count and pyxel.frame_count % (c.fps/15) == 0:
            self.girar()
        elif self.duracion_frames > pyxel.frame_count:
            pass
        else:
            self.desaparecer()
        self.actualizar_posicion()
 

    def girar(self):
        if self.sprite == c.sprite_moneda_girada:
            self.sprite = c.sprite_moneda
        else:
            self.sprite = c.sprite_moneda_girada
