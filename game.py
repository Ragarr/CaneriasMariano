import pyxel
from clases import bloque
from clases import player
class App():
    def __init__(self) -> None:
        self.jugador = player.mario([20, 20])
        self.bloques = [bloque.interrogacion([20, 20]), bloque.ladrillo_no_rompible(
            [28, 20]), bloque.ladrillo_no_rompible([36, 20]), bloque.ladrillo_no_rompible([44, 20])]

        # esto tiene que ir al final del init
        pyxel.init(100, 100, caption="test")
        pyxel.load("assets/test_resource.pyxres")
        pyxel.run(self.update(), self.draw())

    def update(self):
        pass
    

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(*self.jugador.dibujo)
        for i in range(len(self.bloques)):
            pyxel.blt(*self.bloques[i].dibujo)

App()