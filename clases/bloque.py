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
        self.coord = coord
        self.coord_iniciales = coord.copy()
        self.sprite = sprite
        self.tiene_hitbox = True  # colisiones del bloque
        # aqui hay que añadir el ancho (x) del ladrillo en pixeles para cuando tengamos el archivo con los sprites
        self.ancho = ancho
        # mas de lo mismo que arriba pero con el largo (y) en pixeles
        self.alto = alto
        self.v_y=0

    def reposicionar(self):
        # print(int(self.coord[1]), int(self.coord_iniciales[1]))
        self.coord[1] = min(self.coord[1]+self.v_y,self.coord_iniciales[1]+2)
        if self.coord[1] < self.coord_iniciales[1]:
            self.v_y+=0.2
        else:
            self.v_y=0



class ladrillo_no_rompible(bloque):
    def __init__(self, coord: list,) -> None:
        """un bloque con textura de ladrillo que no interactua con el jugador"""
        # una vez que el profesor nos pase el archivo con los sprites
        super().__init__(coord, c.sprite_ladrillo, c.ancho_ladrillo,c.alto_ladrillo)


    def golpear(self,bloques=None):
        self.v_y-=0.2


class ladrillo_rompible(bloque):
    def __init__(self, coord: list) -> None:
        """un bloque con textura de ladrillo que cuando es golpeado por el jugador suelta le da una moneda"""
        super().__init__(coord, c.sprite_ladrillo, c.ancho_ladrillo, c.alto_ladrillo)

    def golpear(self,bloques=None):
        """rompe el bloque"""
        # remplazar el sprite por uno vacio
        self.dibujo[2], self.dibujo[3], self.dibujo[4], self.dibujo[5], self.dibujo[6], self.dibujo[7] = c.sprite_transparente  
        # deshabilitar las colisiones con el objeto
        self.tiene_hitbox = False  


class ladrillo_con_monedas(bloque):
    def __init__(self, coord: list) -> None:
        """visualmente es igual que los demas ladrillos pero contiene una cantidad aleatorea de monedas"""
        super().__init__(coord, c.sprite_ladrillo, c.ancho_ladrillo, c.alto_ladrillo)
        # numero de monedas que contiene el bloque
        self.monedas = random.randint(1, 6)
        # controla si el objeto tiene colisiones

    def golpear(self, objetos:list):
        """dara monedas hasta que no haya, entonces se rompera"""
        if self.monedas <= 1:
            self.romper()
        self.monedas -= 1  # resta una moneda al contenido del bloque
        objetos.append(objeto.moneda([self.coord_iniciales[0],self.coord_iniciales[1]-15]))
    def romper(self):
        self.sprite = c.sprite_transparente  # remplazar el sprite por el cielo
        self.tiene_hitbox = False  # para deshabilitar las colisiones con el objeto


class interrogacion(bloque):
    def __init__(self, coord: list) -> None:
        """este bloque es tanto el de la interrogacion como el bloque liso dependiendo en si esta activo o no"""
        super().__init__(coord, c.sprite_interrogacion,c.ancho_interrogacion,c.alto_interrogacion)

        # 0-3moneda, 4champi, 5flor, 6estrella
        self.contenido = random.randint(0, 6)

    def golpear(self,bloques=None):
        """dara un objeto y se convertirta en un bloque plano"""
        self.sprite = c.sprite_interrogacion_golpeado  # reemplazar el sprite de interrogacion por el liso

class tuberia(bloque):
    def __init__(self, coord: list,alto:int) -> None:
        super().__init__(coord, c.tuberia(alto)) # una vez que el profesor nos pase el archivo con los sprites
        self.alto=alto
        self.ancho=c.ancho_tuberia

class suelo(bloque):
    def __init__(self, coord: list) -> None:
        # una vez que el profesor nos pase el archivo con los sprites
        super().__init__(coord, c.sprite_suelo, pyxel.width, pyxel.height/3)

