import pyxel
from clases import bloque
from clases import player
class App():
    def __init__(self) -> None:
        self.mario = player.mario()
        self.block=bloque.ladrillo_rompible([0,50])
        pyxel.init(256, 256, caption="test")
        pyxel.load("libraries/pyxel/examples/assets/jump_game.pyxres")
        pyxel.run(self.update(), self.draw())

    def update(self):

        if pyxel.frame_count>=300:
            self.block.golpear()



    def draw(self):
        pyxel.cls(12)
        pyxel.blt(*self.block.dibujo)
App()