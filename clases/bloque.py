import pyxel
import random

class bloque():
    def __init__(self,coord:list,sprite:list) -> None:
        """coord es una lista que contiene x e y en dicho orden. sprite es una lista de 5 elementos 
        que contiene en este orden los siguienes valores n este orden:
            -el numero de banco del sprite
            -la pos x donde se inicia el sprite
            -la pos y donde se inicia el sprite
            -la pos x final del sprite
            -la pos y final del sprite
        """
        self.coord=coord # lista de la forma: (x_i,y_i) donde se inicia la posicion del sprite en pantalla
        self.sprite=sprite # lista que contiene la info para localizar el sprite en memoria

        self.ancho = 0  # aqui hay que añadir el ancho (x) del ladrillo en pixeles para cuando tengamos el archivo con los sprites
        self.largo = 0  # mas de lo mismo que arriba pero con el largo (y) en pixeles

class ladrillo_no_rompible(bloque):
    """un bloque con textura de ladrillo que no interactua con el jugador"""
    def __init__(self, coord: list) -> None:
        super().__init__(coord, ["""aqui va el sprite"""]) # una vez que el profesor nos pase el archivo con los sprites


class ladrillo_rompible(bloque):
    """un bloque con textura de ladrillo que cuando es golpeado por el jugador suelta le da una moneda"""
    def __init__(self, coord: list) -> None:
        super().__init__(coord, ["""aqui va el sprite"""])  # una vez que el profesor nos pase el archivo con los sprites
        self.esta_activo = True  # controla si el objeto tiene colisiones
    
    def golpear(self):
        self.sprite=[] # remplazar el sprite por el cielo
        self.esta_activo=False #para deshabilitar las colisiones con el objeto


class ladrillo_con_monedas(bloque):
    """visualmente es igual que los demas ladrillos pero contiene una cantidad aleatorea de monedas"""
    def __init__(self, coord: list) -> None:
        super().__init__(coord, ["""sprite del ladrillo """]) # una vez que el profesor nos pase el archivo con los sprites
        self.monedas=random.randint(1,6) # numero de monedas que contiene el bloque
        self.esta_activo = True # controla si el objeto tiene colisiones
    def golpear(self):
        if self.monedas<=1:
            self.romper()
        self.monedas-=1 # resta una moneda al contenido del bloque
        
    def romper(self):
        self.sprite = []  # remplazar el sprite por el cielo
        self.esta_activo = False  # para deshabilitar las colisiones con el objeto


        



class interrogacion(bloque):
    """este bloque es tanto el de la interrogacion como el bloque liso dependiendo en si esta activo o no"""
    def __init__(self, coord: list, sprite: list) -> None:
        super().__init__(coord, sprite)
        self.contenido=random.randint(0,6) # 0-3moneda, 4champi, 5flor, 6estrella
    def romper(self):
        self.sprite = ["""aqui va el nuevo sprite"""] # reemplazar el sprite de interrogacion por el liso




