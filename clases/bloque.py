import pyxel
import random
if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")


class bloque():
    def __init__(self, dibujo: list) -> None:
        """dibujo es una lista de 8 elementos 
        que contiene en este orden los siguienes valores n este orden:
            -x de inicio del dibujo
            -y de inicio del dibujo
            -el numero de banco del sprite
            -la pos x donde se inicia el sprite
            -la pos y donde se inicia el sprite
            -la pos x final del sprite
            -la pos y final del sprite
            -color de chroma
        """
        self.dibujo = dibujo
        self.esta_activo = True  # colisiones del bloque
        # aqui hay que añadir el ancho (x) del ladrillo en pixeles para cuando tengamos el archivo con los sprites
        self.ancho = 0
        # mas de lo mismo que arriba pero con el largo (y) en pixeles
        self.largo = 0


class ladrillo_no_rompible(bloque):
    def __init__(self, coord: list) -> None:
        """un bloque con textura de ladrillo que no interactua con el jugador"""
        # una vez que el profesor nos pase el archivo con los sprites
        super().__init__(coord+[0, 48, 88, 8, 8, -1])

    def golpear(self):
        pass


class ladrillo_rompible(bloque):
    def __init__(self, coord: list) -> None:
        """un bloque con textura de ladrillo que cuando es golpeado por el jugador suelta le da una moneda"""
        super().__init__(coord+[0, 48, 88, 8, 8, -1])  # una vez que el profesor nos pase el archivo con los sprites

    def golpear(self):
        """rompe el bloque"""
        # remplazar el sprite por uno vacio
        self.dibujo[2], self.dibujo[3], self.dibujo[4], self.dibujo[5], self.dibujo[6], self.dibujo[7] = 0, 144, 16, 8, 8, 0  
        # deshabilitar las colisiones con el objeto
        self.esta_activo = False  
        


class ladrillo_con_monedas(bloque):
    def __init__(self, coord: list) -> None:
        """visualmente es igual que los demas ladrillos pero contiene una cantidad aleatorea de monedas"""
        super().__init__(coord + [0, 48, 88, 8, 8, -1])  # cambiar una vez nos den los sprites
        # numero de monedas que contiene el bloque
        self.monedas = random.randint(1, 6)
        # controla si el objeto tiene colisiones

    def golpear(self):
        """dara monedas hasta que no haya, entonces se rompera"""
        if self.monedas <= 1:
            self.romper()
        self.monedas -= 1  # resta una moneda al contenido del bloque

    def romper(self):
        self.sprite = []  # remplazar el sprite por el cielo
        self.esta_activo = False  # para deshabilitar las colisiones con el objeto


class interrogacion(bloque):
    def __init__(self, coord: list) -> None:
        """este bloque es tanto el de la interrogacion como el bloque liso dependiendo en si esta activo o no"""
        super().__init__(coord+[0, 0, 0, 0, 0])
        # 0-3moneda, 4champi, 5flor, 6estrella
        self.contenido = random.randint(0, 6)

    def golpear(self):
        """dara un objeto y se convertirta en un bloque plano"""
        self.sprite = [
            """aqui va el nuevo sprite"""]  # reemplazar el sprite de interrogacion por el liso


class tuberia(bloque):
    def __init__(self, coord: list) -> None:
        super().__init__(coord+[0,24,96,8,8,0]
                         )  # una vez que el profesor nos pase el archivo con los sprites

