

# --------------------inicializacion del juego--------------------

ancho_pantalla = 256
alto_pantalla = 200
fps = 60
assets_path = "assets/editor/assets/mario_assets.pyxres"
tiempo=400 #segundos

# ----------------------------colores-----------------------------
negro = 0
azul_muy_oscuro = 1
morado = 2
turquesa = 3
marron = 4
azul_oscuro = 5
cian = 6
blanco = 7
rosa = 8
naranja = 9
amarillo = 10
verde = 11
azul = 12
gris = 13
salmon = 14
carne = 15

# ---------------------------fisicas------------------------------
v_gravedad = 0.25
v_salto =5
v_rozamiento =0.1
v_avance = 0.2
v_player_max_x=1.5
v_player_max_y= 2
v_objeto_x=2
v_rebote= 4
v_npc= 1
v_goompa, v_koopa_troopa = v_npc, v_npc
v_caparazon=3

#----------------------animaciones-------------------------------
frames_duracion_concha= 10*fps


#-----------------coeficientes para las hitboxes-------------------
ancho_mario = 15
alto_mario=alto_smario_agachado=15
ancho_smario = 15
alto_smario = 31
ancho_goompa=16
ancho_koopa_troopa=16
alto_goompa=16
alto_koopa_troopa=16
ancho_interrogacion = 15
ancho_escalera = 15
ancho_ladrillo = 15
alto_interrogacion = 15
alto_ladrillo = 15
alto_escalera= 15

altura_suelo = alto_pantalla-alto_pantalla/8  +3
ancho_tuberia= 31
ancho_suelo=15
alto_concha=12
tolerancia_colisiones=2
alto_champi = alto_estrella = alto_flor = 15
ancho_champi = ancho_estrella = ancho_flor = 15


#----------------------puntuaciones------------------------------
punt_goompa=100
punt_koopa_troopa=200
punt_moneda=200
punt_champi=1000
punt_flor=1000
punt_estrella=1000


#-----------------sprites en general-----------------------------
sprite_moneda_chiquita = [0, 2, 29, 9, 13, azul] # editar esto
sprite_moneda=[0,2,29,9,13,azul]
sprite_moneda_girada=[0,40,41,9,13,azul]
sprite_champi=[0,0,45,15,15,azul]
sprite_estrella=[0,17,42,15,15,azul]
sprite_flor=[0,55,47,15,15,azul]
sprite_nube=[0,39,48,153,13,azul]
sprite_interrogacion_golpeado=[0,145,27,16,16,blanco]
sprite_interrogacion=[0,177,27,16,16,blanco]
sprite_mario_verde=[0,206,82,15,31,azul]
sprite_smario_lanzando_fuego=[0,0,132,15,31,azul]
sprite_fireball=[0,19,143,15,15,azul]
sprite_cartel=[1,0,0,208,80,azul]
## como el tamaño de la tuberia es variable en vez de una constante tenemos una funcion
def tuberia(alto:int=48):
    """el alto se cuenta en pixeles"""
    return [0,79,178,32,alto,azul]

## como el tamaño de la escalera es variable en vez de una constante tenemos una funcion
def escalera(alto: int):
    '''El alto se cuenta en bloques y no en pixeles'''
    return [0, 113, 1, 17, alto*15, azul] 

sprite_suelo=[0,0,227,ancho_suelo,22,azul] # el suelo puede medir hasta 250 de ancho
sprite_ladrillo=[0,160,208,15,15,-1]
sprite_transparente=[0,0,0,0,0,azul]
sprite_goompa=[0,16,0,16,16,azul]
sprite_goompa_aplastado=[0,32,0,16,16,azul]
sprite_koopa_troopa=[0,16,16,16,16,azul]
sprite_concha=[0,32,22,16,10,azul]


#-----------sprites mario-------------
# mirando a der
sprite_mario_quieto = [0, 3, 98, 15, 15, azul]
sprite_mario_saltando = [0, 1, 79, 15, 15, azul]
sprite_mario_andando = [0, 18, 99, 15, 15, azul]
sprite_mario_girando = [0, 36, 99, 15, 15, azul]
sprite_smario_quieto = [0, 54, 82, 15, 31, azul]
sprite_smario_andando1 = [0, 89, 82, 15, 31, azul]
sprite_smario_andando2 = [0, 107, 84, 13, 30, azul]
sprite_smario_girando = [0, 124, 83, 15, 31, azul]
sprite_smario_saltando = [0, 148, 80, 15, 31, azul]
sprite_smario_agachado = [0, 187, 82, 16, 31, azul]
sprite_smario_fuego_andando1=[0,200,4,17,31,azul]
sprite_smario_fuego_andando2 = sprite_smario_fuego_disparando = [0, 0, 134, 15, 30, azul]
sprite_smario_fuego_quieto = [0, 168, 81, 15, 31, azul]
sprite_smario_fuego_girando = [0, 36, 131, 15, 31, azul]
sprite_smario_fuego_saltando= [0,59,128,15,31,azul]
sprite_smario_fuego_agachado = [0, 83, 130 ,16, 31, azul]

# mirando a izq
sprite_mario_quieto_i = [0, 3, 98, -15, 15, azul]
sprite_mario_saltando_i = [0, 1, 79, -15, 15, azul]
sprite_mario_andando_i = [0, 18, 99, -15, 15, azul]
sprite_mario_girando_i = [0, 36, 99, -15, 15, azul]
sprite_smario_quieto_i = [0, 54, 82, -15, 31, azul]
sprite_smario_andando1_i = [0, 89, 82, -15, 31, azul]
sprite_smario_andando2_i = [0, 107, 84,- 13, 30, azul]
sprite_smario_girando_i = [0, 124, 83, -15, 31, azul]
sprite_smario_saltando_i = [0, 148, 80, -15, 31, azul]
sprite_smario_agachado_i = [0, 187, 82, -15, 31, azul]
sprite_smario_fuego_andando1_i = [0, 200, 4, -17, 31, azul]
sprite_smario_fuego_andando2_i = sprite_smario_fuego_disparando_i = [0, 0, 134, -15, 30, azul]
sprite_smario_fuego_quieto_i = [0, 168, 81, -15, 31, azul]
sprite_smario_fuego_girando_i = [0, 36, 131, -15, 31, azul]
sprite_smario_fuego_saltando_i = [0, 59, 128, -15, 31, azul]
sprite_smario_fuego_agachado_i = [0, 83, 130, -16, 31, azul]