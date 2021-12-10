from clases.bloques.bloque import bloque
import random
import constants as c
from clases.objetos.champi import champi
from clases.objetos.flor import flor
from clases.objetos.moneda import moneda


class interrogacion(bloque):
    def __init__(self, coord: list, monedas = False) -> None:
        """este bloque es tanto el de la interrogacion como el bloque liso dependiendo en si esta activo o no"""
        self.__tiene_monedas = monedas
        super().__init__(coord, c.sprite_interrogacion,c.ancho_interrogacion,c.alto_interrogacion)
        # De base spwanea la seta, ya que es la más habitual
        # 1champi 2flor u 1monedas
        self.monedas = random.randint(1,6)
        self.__contenido = True
    
    @property 
    def contenido(self):
        return self.__contenido

    @contenido.setter
    def contenido(self,new_contenido):
        self.__contenido = new_contenido

    @property 
    def tiene_monedas(self):
        return self.__tiene_monedas

    @tiene_monedas.setter
    def tiene_monedas(self,new_tiene_monedas):
        self.__contenido = new_tiene_monedas


    def golpear(self, objetos:list, player):
        """Dará un objeto seta si es pequeño o si es grande dará una flor y se convertirta en un bloque plano"""
        self.v_y=-0.5
        if self.__tiene_monedas:   
            if self.monedas >= 1:
                self.monedas =(self.monedas- 1) # resta una moneda al contenido del bloque
                objetos.append(moneda([self.coord[0],self.coord[1]-15]))
                player.dinero += 1
            else:
                self.sprite = c.sprite_interrogacion_golpeado
        else:    
            if self.contenido and player.grande:
                objetos.append(flor([self.coord[0],self.coord_iniciales[1]-c.alto_flor-8]))#Crea una flor encima del bloque
                self.contenido = 0
            elif self.contenido:
                objetos.append(champi([self.coord[0],self.coord_iniciales[1]-c.alto_champi/2]))#Crea la seta al inicio de su animación
                self.contenido = 0
            else:
                pass
                
            self.sprite = c.sprite_interrogacion_golpeado  # reemplazar el sprite de interrogacion por el liso
