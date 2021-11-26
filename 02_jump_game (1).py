from random import randint

import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Pyxel Jump") #define tamaño de la ventana y caption es el nombre de la ventana#

        pyxel.load("assets/test_resource.pyxres") #carga todo un fichero con recursos del juego como imagenes, sonido, etc.#

        self.score = 0
        self.player_x = 72
        self.player_y = -16
        self.player_vy = 0 #velocidad
        self.player_is_alive = True

        self.far_cloud = [(-10, 75), (40, 65), (90, 60)] #posicion de una nube
        self.near_cloud = [(10, 25), (70, 35), (120, 15)]
        self.floor = [(i * 60, randint(8, 104), True) for i in range(4)] #posicion aleatoria del suelo
        self.fruit = [(i * 60, randint(0, 104), randint(0, 2), True) for i in range(4)]

        pyxel.playm(0, loop=True) #cuando la musica termina se repite

        pyxel.run(self.update, self.draw) #bucle que actualiza y dibuja el juego constantemente

    def update(self): 
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        self.update_player()

        for i, v in enumerate(self.floor):
            self.floor[i] = self.update_floor(*v)

        for i, v in enumerate(self.fruit):
            self.fruit[i] = self.update_fruit(*v)

    def update_player(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD_1_LEFT):
            self.player_x = max(self.player_x - 2, 0) #obliga al jugador a mantenerse en la pantalla sin dejarle ir a +x

        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD_1_RIGHT):
            self.player_x = min(self.player_x + 2, pyxel.width - 16) #lo mismo q el anterior comentario pero hacia -x

        self.player_y += self.player_vy
        self.player_vy = min(self.player_vy + 1, 8)

        if self.player_y > pyxel.height: #si el personaje cae, muere
            if self.player_is_alive:
                self.player_is_alive = False
                pyxel.play(3, 5)

            if self.player_y > 600: #reinicia el personaje
                self.score = 0
                self.player_x = 72
                self.player_y = -16
                self.player_vy = 0
                self.player_is_alive = True

    def update_floor(self, x, y, is_active): #si el personaje pisa el suelo cuando esta activo, el suelo desaparece
        if is_active: #si el suelo es pisable
            if (
                self.player_x + 16 >= x
                and self.player_x <= x + 40
                and self.player_y + 16 >= y   #y lo pisa
                and self.player_y <= y + 8
                and self.player_vy > 0
            ):
                is_active = False #deja de ser pisable
                self.score += 10
                self.player_vy = -12 #aumenta velocidad
                pyxel.play(3, 3) #play(musica, canal)
        else: #si el suelo no es pisable
            y += 6 #el suelo se cae

        x -= 4 #el suelo va a la izquierda

        if x < -40:
            x += 240
            y = randint(8, 104)
            is_active = True

        return x, y, is_active

    def update_fruit(self, x, y, kind, is_active):
        if is_active and abs(x - self.player_x) < 12 and abs(y - self.player_y) < 12:
            is_active = False
            self.score += (kind + 1) * 100
            self.player_vy = min(self.player_vy, -8)
            pyxel.play(3, 4)

        x -= 2

        if x < -40: #si esta en -40 x, reaparece en 240 x
            x += 240
            y = randint(0, 104)
            kind = randint(0, 2) #el tipo de fruta cambia aleatoriamene pero tienen el mismo comportamiento
            is_active = True

        return (x, y, kind, is_active)

    def draw(self):
        pyxel.cls(12)
        
        # draw sky
        pyxel.blt(0, 88, 0, 0, 88, 160, 32) #pintar cielo en: (x, y, )

        # draw mountain
        pyxel.blt(0, 88, 0, 0, 64, 160, 24, 12)

        # draw forest
        offset = pyxel.frame_count % 160
        for i in range(2): #pinta 2 bosques
            pyxel.blt(i * 160 - offset, 104, 0, 0, 48, 160, 16, 12)

        # draw clouds
        offset = (pyxel.frame_count // 16) % 160
        for i in range(2): #pinta 2 nubes lejanas
            for x, y in self.far_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 64, 32, 32, 8, 12)

        offset = (pyxel.frame_count // 8) % 160
        for i in range(2): #pinta dos nubes cercanas
            for x, y in self.near_cloud:
                pyxel.blt(x + i * 160 - offset, y, 0, 0, 32, 56, 8, 12)

        # draw floors
        for x, y, is_active in self.floor:
            pyxel.blt(x, y, 0, 0, 16, 40, 8, 12) #pinta en posicion x, y, carga la imagen 0, desde la posicion 0,16 hasta la 40, 8 y 12 es la transaprencia 

        # draw fruits
        for x, y, kind, is_active in self.fruit:
            if is_active:
                pyxel.blt(x, y, 0, 32 + kind * 16, 0, 16, 16, 12)

        # draw player
        pyxel.blt(
            self.player_x,
            self.player_y,
            0,
            16 if self.player_vy > 0 else 0,
            0,
            16,
            16,
            12,
        )

        # draw score
        s = "SCORE {:>4}".format(self.score)
        #pyxel.text(5, 4, s, 1)
        #pyxel.text(4, 4, s, 7)
        pyxel.text(4, 4, str(pyxel.frame_count), 7)


App()
