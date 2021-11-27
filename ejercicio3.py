import random as rnd 
class Dado():
    def __init__(self, name, num_tiradas) -> None:
        '''Dado es una clase con dos valores el nombre de la perosna que juega y el número de tiradas de dado que se realizan'''
        tiradas = []
        for i in range(num_tiradas):
            tiradas.append(rnd.randint(1,6))
        self.nombre = name
        self.tiradas = tiradas
    def iguales(self):
        '''Iguales es un método que nos permite saber la cantidad de veces que un número se repite en una tirada y el máximo de estos se devuelve como parámetro'''
        iguales = 0
        for i in range(len(self.tiradas)):
            contador = 0
            for c in range(len(self.tiradas)):
                if self.tiradas[i]==self.tiradas[c]:
                    contador += 1
            if iguales < contador:
                iguales = contador
        return iguales
    def suma_tirada(self):
        '''Suma_tirada nos da como resultado la suma de todos los valores de los dados'''
        suma = 0
        for i in range(len(self.tiradas)):
            suma += self.tiradas[i]
        return suma
    
'''Vamos a simular una partida de 4 jugadores a 6 tiradas cada uno'''
jugador1 = Dado('Carlos', 6 )
jugador2 = Dado('Raúl', 6)
jugador3 = Dado('Luis', 6 )
jugador4 = Dado('Jaime', 6 )

jugadores = []
jugadores.append((jugador1.iguales(), jugador1.suma_tirada()))
jugadores.append((jugador2.iguales(),jugador2.suma_tirada()))
jugadores.append((jugador3.iguales(), jugador3.suma_tirada()))
jugadores.append((jugador4.iguales(), jugador4.suma_tirada()))
empate = False
ganador = []
rganador = 0
ganadorf = []
'''Realizamos la primera parte que es ver cual es el máximo de dados que se repiten en cada jugador(método: iguales)'''
for i in range(len(jugadores)):
    if jugadores[i][0] > rganador:
        rganador = jugadores [i][0]
'''Los que sean iguales al máximo se agregan a la lista de los ganadores'''
for i in range(len(jugadores)):
    if jugadores[i][0] == rganador:
        ganador.append((i, jugadores[i][1]))
rganador= 0
'''Realizamos el mismo proceso entre los ganadores(empatados), ahora con el método suma'''
for i in range(len(ganador)):
    if ganador[i][1]> rganador:
        rganador = jugadores [i][1]
for i in range(len(ganador)):
    if jugadores[i][1] == rganador:
        ganadorf.append(ganador[i][0])
imprimir = ''
for i in range(len(ganadorf)):
    imprimir += 'jugador' + str(ganadorf[i] +1) + ' '
'''Por último imprimimos dependiendo de cuantos ganadores tengamos'''
if len(ganadorf) == 1:
    print('El ganador es ' + imprimir)
else:
    print('Los ganadores son:' + imprimir)

print(jugadores)
print(ganador)