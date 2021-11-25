import pyxel


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