if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")
    quit()


class bloque():
    def __init__(self, coord: list, sprite: list, ancho, alto, izquierda = False, derecha = False ) -> None:
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
        self.es_caparazon=False
        self.__pared_izquierda = izquierda
        self.__pared_derecha = derecha
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
    @property
    def pared_izquierda(self):
        return self.__pared_izquierda
    @pared_izquierda.setter
    def pared_izquierda(self, New__pared_izquierda:bool):
        self.__pared_izquierda= New__pared_izquierda
    
    @property
    def pared_derecha(self):
        return self.__pared_derecha
    @pared_izquierda.setter
    def pared_derecha(self, New__pared_derecha:bool):
        self.__pared_derecha= New__pared_derecha


   
    
    def reposicionar(self):
        self.coord[1] = min(self.coord[1]+self.v_y,self.coord_iniciales[1]+2)
        if self.coord[1] < self.coord_iniciales[1]:
            self.v_y+=0.1
        else:
            self.v_y=0
        self.coord[0]+=self.__v_x



