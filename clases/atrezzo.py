if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
class atrezzo():
    def __init__(self,dibujo:list) -> None:
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
        self.tiene_hitbox = False
        self.dibujo=dibujo

class montaña(atrezzo):
    def __init__(self, coord:list) -> None:
        self.coord=coord
        super().__init__(coord+[0,72,16,16,0])

class nube(atrezzo):
    def __init__(self, coord:list) -> None:
        self.coord=coord
        super().__init__(coord+[16,72,16,16,0])


class arbusto(atrezzo):
    def __init__(self, coord:list) -> None:
        self.coord=coord
        super().__init__(coord+[32,72,16,16,0])
