if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()

import random
import pyxel
from clases import objeto
import constants as c

class bloque():
    def __init__(self, coord: list, sprite: list, ancho, alto ) -> None:
        """coord es una lista de 2 elementos 
        que contiene en este orden los siguienes valores x e y  del origen
        """
        self.__coord = coord
        self.__coord_iniciales = self.__coord.copy()
        self.__sprite = sprite
        self.__tiene_hitbox = True  # colisiones del bloque
        # aqui hay que añadir el ancho (x) del ladrillo en pixeles para cuando tengamos el archivo con los sprites
        self.__ancho = ancho
        # mas de lo mismo que arriba pero con el largo (y) en pixeles
        self.__alto = alto
        self.__v_y=0
        self.__v_x=0
        self.__existe=True
    @property
    def existe(self):
        return self.__existe
    @existe.setter
    def existe(self,new_existe):
        if not isinstance(new_existe,bool):
            raise ValueError("el valor debe ser booleano")
        self.__existe=new_existe

    @property # getter
    def coord(self):
        return self.__coord

    @coord.setter # el setter
    def coord(self,coord:list):
        # modificando las coordenadas
        if not isinstance(coord,list):
            raise ValueError("las coordenadas deben ser una lista")
        if len(coord) !=2:
            raise ValueError("la lista de coordenadas debe tener exactamente dos elementos")
        if not isinstance(coord[0], (int,float)) or not isinstance(coord[0], (int,float)):
            raise ValueError("las coordenadas deben ser enteros o floats")
        self.__coord=coord
    @property
    def v_y(self):
        return self.__v_y
    @v_y.setter
    def v_y(self,v_y:float):
        if not isinstance(v_y, (float,int)):
            raise ValueError("la velocidad debe ser un int o float")
        self.__v_y=v_y

    @property
    def v_x(self):
        return self.__v_x

    @v_x.setter
    def v_x(self, v_x: float):
        if not isinstance(v_x, (float, int)):
            raise ValueError("la velocidad debe ser un int o float")
        self.__v_x = v_x

    @property # permite consultar la hitbox
    def tiene_hitbox(self):
        return self.__tiene_hitbox

    @property
    def ancho(self):
        return self.__ancho
    @property
    def alto(self):
        return self.__alto
    @property
    def sprite(self):
        return self.__sprite
    @sprite.setter
    def sprite(self,new_sprite:list):
        if not isinstance(new_sprite, list):
            raise ValueError("el sprite deben ser una lista")
        if len(new_sprite) !=6:
            raise ValueError("la lista sprite debe tener exactamente 6 elementos")
        self.__sprite=new_sprite
    @property
    def tiene_hitbox(self):
        return self.__tiene_hitbox
    @tiene_hitbox.setter
    def tiene_hitbox(self, hitbox:bool):
        self.__tiene_hitbox=hitbox

    @property
    def coord_iniciales(self):
        return self.__coord_iniciales

    @coord_iniciales.setter
    def coord_iniciales(self):
        self.__coord=self.__coord.copy()
    
    def reposicionar(self):
        # print(int(self.coord[1]), int(self.coord_iniciales[1]))
        self.coord[1] = min(self.coord[1]+self.v_y,self.coord_iniciales[1]+2)
        if self.coord[1] < self.coord_iniciales[1]:
            self.v_y+=0.1
        else:
            self.v_y=0
        self.coord[0]+=self.__v_x





class ladrillo_no_rompible(bloque):
    def __init__(self, coord: list,) -> None:
        """un bloque con textura de ladrillo que no interactua con el jugador"""
        # una vez que el profesor nos pase el archivo con los sprites
        super().__init__(coord, c.sprite_ladrillo, c.ancho_ladrillo,c.alto_ladrillo)


    def golpear(self,bloques=None,player=None):
        self.v_y=-0.5


class ladrillo_rompible(bloque):
    def __init__(self, coord: list) -> None:
        """un bloque con textura de ladrillo que cuando es golpeado por el jugador suelta le da una moneda"""
        super().__init__(coord, c.sprite_ladrillo, c.ancho_ladrillo, c.alto_ladrillo)

    def golpear(self,bloques=None,player=None):
        """rompe el bloque"""
        self.romper()

    def romper(self):
        self.existe=False


class ladrillo_con_monedas(bloque):
    def __init__(self, coord: list) -> None:
        """visualmente es igual que los demas ladrillos pero contiene una cantidad aleatorea de monedas"""
        super().__init__(coord, c.sprite_ladrillo, c.ancho_ladrillo, c.alto_ladrillo)
        # numero de monedas que contiene el bloque
        self.monedas = random.randint(1,6)
        # controla si el objeto tiene colisiones

    def golpear(self, objetos:list,player=None):
        """dara monedas hasta que no haya, entonces se rompera"""
        if self.monedas < 1:
            self.romper()
        if pyxel.frame_count % 5 == 0:
            self.v_y-=0.5
            self.monedas =(self.monedas- 1) # resta una moneda al contenido del bloque
            objetos.append(objeto.moneda([self.coord_iniciales[0],self.coord_iniciales[1]-15]))
            player.dinero += 1

        
        
    def romper(self):
        self.existe=False
 # para deshabilitar las colisiones con el objeto


class interrogacion(bloque):
    def __init__(self, coord: list) -> None:
        """este bloque es tanto el de la interrogacion como el bloque liso dependiendo en si esta activo o no"""
        super().__init__(coord, c.sprite_interrogacion,c.ancho_interrogacion,c.alto_interrogacion)

        # 0-3moneda, 4champi, 5flor, 6estrella
        self.contenido = random.randint(0, 6)

    def golpear(self,bloques=None,player=None):
        """dara un objeto y se convertirta en un bloque plano"""
        self.v_y=-0.2
        self.__sprite = c.sprite_interrogacion_golpeado  # reemplazar el sprite de interrogacion por el liso

class tuberia(bloque):
    def __init__(self, coord: list,alto:int) -> None:
        super().__init__(coord, c.tuberia(alto)) # una vez que el profesor nos pase el archivo con los sprites
        self.__alto=alto
        self.__ancho=c.ancho_tuberia

class suelo(bloque):
    def __init__(self, coord: list) -> None:
        # una vez que el profesor nos pase el archivo con los sprites
        super().__init__(coord, c.sprite_suelo, pyxel.width, pyxel.height/3)

class bloque_no_movible(bloque):
    def __init__(self, coord: list) -> None:
        super().__init__(coord,c.sprite_bloque_inamovible, c.ancho_bloque_inamovible, c.alto_bloque_inamovible)

    def golpear(lf, bloques=None, player=None):
        pass