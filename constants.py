

# --------------------inicializacion del juego--------------------

ancho_pantalla = 256
alto_pantalla = 200
fps = 60
assets_path = "assets/editor/assets/mario_assets.pyxres"


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
v_avance = 0.5
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
alto_mario=15
ancho_smario = 15
alto_smario = 31
ancho_goompa=16
ancho_koopa_troopa=16
alto_goompa=16
alto_koopa_troopa=16
ancho_interrogacion = ancho_bloque_inamovible = ancho_ladrillo = 15
alto_interrogacion = alto_ladrillo = alto_bloque_inamovible= 15
altura_suelo = alto_pantalla-alto_pantalla/8  +3
ancho_tuberia=31
ancho_suelo=15
alto_concha=12
tolerancia_colisiones=2

#-----------------sprites en general-----------------------------
sprite_moneda=[0,2,29,9,13,azul]
sprite_moneda_girada=[0,40,41,9,13,azul]
sprite_champi=[0,0,45,14,15,azul]
sprite_estrella=[0,17,42,15,15,azul]
sprite_flor=[0,55,47,14,14,azul]
sprite_nube=[0,39,48,153,13,azul]
sprite_interrogacion_golpeado=[0,145,27,16,16,azul]
sprite_interrogacion=[0,177,27,16,16,azul]
sprite_mario_quieto=[0,3,98,15,15,azul]
sprite_mario_saltando=[0,1,79,15,15,azul]
sprite_mario_andando=[0,18,99,15,15,azul]
sprite_mario_girando=[0,36,99,15,15,azul]
sprite_smario_quieto=[0,54,82,15,31,azul]
sprite_smario_andando1=[0,89,82,15,31,azul]
sprite_smario_andando2=[0,107,84,15,31,azul]
sprite_smario_girando=[0,124,83,15,31,azul]
sprite_smario_saltando=[0,148,80,15,31,azul]
sprite_smario_fuego = [0, 168, 81, 15, 31, azul]
sprite_smario_agachado = [0, 187, 92, 15, 21, azul]
sprite_mario_verde=[0,206,82,15,31,azul]
sprite_smario_lanzando_fuego=[0,0,132,15,31,azul]
sprite_fireball=[0,21,147,7,7,azul]
def tuberia(alto:int=48):
    return [0,79,178,31,alto,azul]
sprite_suelo=[0,0,227,ancho_suelo,22,azul] # el suelo puede medir hasta 250 de ancho
sprite_ladrillo=[0,160,208,15,15,-1]
sprite_transparente=[0,0,0,0,0,azul]
sprite_goompa=[0,16,0,16,16,azul]
sprite_goompa_aplastado=[0,32,0,16,16,azul]
sprite_koopa_troopa=[0,16,16,16,16,azul]
sprite_concha=[0,32,22,16,10,azul]
sprite_bloque_inamovible= [0,1,114,16,16,azul]

