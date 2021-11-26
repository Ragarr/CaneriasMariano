if __name__ == "__main__":
    print("este archivo no es el principal y no esta pensado para ser ejecutado")


class mario():
    def __init__(self, coord: list) -> None:
        self.score = 0
        self.monedas = 0
        self.tamaño = 0  # 0peque, 1supermario, 2con flor
        self.coord = coord  # ubicacion de el sprite
        self.sprite = [0, 48, 0, 8, 8, 0]
