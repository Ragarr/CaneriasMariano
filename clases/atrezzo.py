if __name__ == "__main__":
    #print("este archivo no es el principal y no esta pensado para ser ejecutado")
    #quit()
    pass

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

        self.__tiene_hitbox = False
        self.__coord=coord
        self.__sprite=sprite
    @property # el getter
    def coord(self):
            return self.__coord

    @coord.setter # el setter
    def coord(self,coord:list):
        # modificando las coordenadas
        if not isinstance(coord,list):
            raise ValueError("las coordenadas deben ser una lista")
        if len(coord) !=2:
            raise ValueError("la lista de coordenadas debe tener exactamente dos elementos")
        if not isinstance(coord[0], (int,float)) or not isinstance(coord[1], (int,float)):
            raise ValueError("las coordenadas deben ser enteros o floats")
        self.__coord=coord


class montaña(atrezzo):
    def __init__(self, coord:list) -> None:
        super().__init__(coord, [0,72,16,16,0])

class nube(atrezzo):
    def __init__(self, coord:list) -> None:
        super().__init__(coord, [0,16,72,16,16,0])


class arbusto(atrezzo):
    def __init__(self, coord:list) -> None:
        super().__init__(coord, [0,32,72,16,16,0])

a=montaña([1,2])
print(a.coord)