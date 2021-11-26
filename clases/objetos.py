if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")

class objeto():
    def __init__(self,coord:list,tipo=int) -> None:
        self.tipo=tipo
        self.sprite = [0,0+8*tipo,64,8,8,0]
        self.coord = coord
        self.velocidad_x=0
        self.velocidad_y=4
    def actualizar_posicion(self):
        self.coordenada[0] += self.velocidad_x
        self.coordenada[1] += self.velocidad_y
        
    def colisionar_bloque(self):
        self.velocidad_x = 0 - self.velocidad_x

