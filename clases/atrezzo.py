if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()
import constants as c
class atrezzo():
    def __init__(self,coord, sprite:list) -> None:
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


        self.__coord=coord
        self.__sprite=sprite
    @property 
    def sprite(self):
        return self.__sprite
    @property # el getter
    def coord(self):
            return self.__coord

    @coord.setter # el setter
    def coord(self,coord:list):
        if not isinstance(coord,list):
            raise ValueError("las coordenadas deben ser una lista")
        if len(coord) !=2:
            raise ValueError("la lista de coordenadas debe tener exactamente dos elementos")
        if not isinstance(coord[0], (int,float)) or not isinstance(coord[1], (int,float)):
            raise ValueError("las coordenadas deben ser enteros o floats")
        self.__coord=coord


class montaña(atrezzo):
    def __init__(self, coord:list) -> None:
        super().__init__(coord, c.sprite_montaña)

class nube(atrezzo):
    def __init__(self, coord:list) -> None:
        super().__init__(coord, c.sprite_nube)


class arbusto(atrezzo):
    def __init__(self, coord:list) -> None:
        super().__init__(coord, c.sprite_arbusto)


