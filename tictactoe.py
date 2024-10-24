import numpy as np
import random
matriz1 = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]
tictactoe = np.array(matriz1)
#innecesario usar numpy porque no estamos usando operaciones con matrices.
equivalencias = {1 : [0, 0], 2: [0, 1],3: [0, 2],4: [1, 0],5: [1, 1],6: [1, 2],7: [2, 0],8: [2, 1],9: [2, 2] }
#funcion para la jugada del primer jugador. Haremos otra para el movimiento de la pc.
def jugada(matriz, contador):
  print("\n ")
  for fila in matriz:
    print(fila)
  movimiento = int(input("\nMenu de opciones:\n1. Arriba-izquierda\n2. Arriba-medio\n3. Arriba-derecha\n4. Medio-izquierda\n5. Medio\n6. Medio-derecha\n7. Abajo-izquierda\n8. Abajo-medio\n9. Abajo-derecha\n Eliga su movimiento: "))
  while movimiento not in contador:
    movimiento = int(input("Debe elegir otra opcion porque ya esta tomada o es un valor incorrecto"))
  posicion = equivalencias[movimiento]
  x= posicion[0]
  y= posicion[1]
  matriz[x][y] = "X"
  contador.remove(movimiento)
  return matriz, contador
#funcion para el movimiento aleatorio de la PC
def jugada_pc(matriz, contador):
  # aleatorio = random.randint(1, 9). Mejor la siguiente forma para evitar el while
  if contador:
    aleatorio = random.choice(contador)
    x, y = equivalencias[aleatorio]
    matriz[x][y] = "O"
    contador.remove(aleatorio)
  return matriz, contador

#las condiciones para ganar son 8 combinaciones de rayas con el mismo valor, y distinto de " "
def condicion(matriz):
  condiciones_juego = True
  for i in range (0, 3):
    if matriz[i,0] == matriz[i,1] and  matriz[i,0] == matriz[i,2] and matriz[i,0] != " " :
      condiciones_juego = False
    elif matriz[0,i] == matriz[1,i] and  matriz[0,i] == matriz[2,i] and matriz[0,i] != " ":
      condiciones_juego = False
  if matriz[0,0] == matriz[1,1] and  matriz[0,0] == matriz[2,2] and matriz[0,0] != " ":
      condiciones_juego = False
  if matriz[0,2] == matriz[1,1] and  matriz[0,2] == matriz[2,0] and matriz[0,2] != " ":
      condiciones_juego = False
  return condiciones_juego

# funcion para que una vez haya un ganador lo calcule
def ganador(matriz):
  for i in range (0, 3):
    if matriz[i,0] == matriz[i,1] and  matriz[i,0] == matriz[i,2] and matriz[i,0] != " " :
      vencedor = matriz[i,0]
    elif matriz[0,i] == matriz[1,i] and  matriz[0,i] == matriz[2,i] and matriz[0,i] != " ":
      vencedor = matriz[0,i]
  if matriz[0,0] == matriz[1,1] and  matriz[0,0] == matriz[2,2] and matriz[0,0] != " ":
      vencedor = matriz[0,0]
  if matriz[0,2] == matriz[1,1] and  matriz[0,2] == matriz[2,0] and matriz[0,2] != " ":
      vencedor = matriz[0,2]
  return vencedor

# funcion del juego que englobe todo
def juego_tic_tac_toe(matriz):
  contador = list(range(1, 10))
  condiciones_juego = True
  while condiciones_juego and contador:
    matriz, contador = jugada(matriz, contador)
    #verificar contador y ganado
    if not condicion(matriz):
      break
    if not contador:
      break
    matriz, contador = jugada_pc(matriz, contador)
    if not condicion(matriz):
      break
    if not contador:
      break
  if not condicion(matriz):
    print(matriz)
    vencedor = ganador(matriz)
    if vencedor == "X":
      print("Felicitaciones, has ganado!")
    elif vencedor == "O":
      print("Has perdido ante la maquina")
  elif not contador:
    print("El juego ha terminado en empate")

#probamos si funciona:

juego_tic_tac_toe(tictactoe)
