#Hacemos un juego de laberinto que sea 12x12
import random

def crear_laberinto():
  while True:
    try:
      #definimos y como el tamano del laberinto cuadrado.
      menu_opciones = ("\nMenú de opciones:\n"
        "1. Dificil\n"
        "2. Extremo\n"
        "Ingrese la dificultad del juego:  "
      )              
                       
      dificultad = int(input(menu_opciones))
      if dificultad not in range(1,3):
        raise ValueError("Debe elegir un numero entre 1-2")
      elif dificultad in range(1,3):
        break
    except ValueError:
      print("Debe elegir una de las opciones del menu")
  laberinto = [ ]
  #relacionamos la dificultad del juego con el tamano del laberinto.
  dificultad_juego = {1: 12, 2:20}
  tamano = int(dificultad_juego[dificultad])

  laberinto.append(["#" for _ in range(tamano)])
  for x in range(tamano-2):
    aumento = []
    aumento += ["#"] + [" " for _ in range(tamano-2)] + ["#"]
    laberinto.append(aumento)
  laberinto.append(["#" for _ in range(tamano)])
  #definimos los obstaculos para dificil y extremo
  lista_obstaculos_dificil = [[4,4], [4,5], [4,6], [4,7], [5,7],[6,7],[7,7],[5,4],[6,4],[7,4]]
  lista_obstaculos_extremo= [[7,7], [7,8], [7,9], [7,10], [7,11],[7,12],[8,12],[9,12],[10,12],[11,12],[12,12],[8,7],[9,7],[10,7],[11,7],[12,7]]
  lista_posibles_salidas = []
  lista_posicion_zodiac = []
  if dificultad == 1:
    lista_eliminar_de_grid = lista_obstaculos_dificil
  elif dificultad == 2:  
    lista_eliminar_de_grid = lista_obstaculos_extremo
  for obstaculos in lista_eliminar_de_grid:
    obstaculo_y, obstaculo_x = obstaculos
    laberinto[obstaculo_y][obstaculo_x] = "#"
  #Ahora aleariamente se selecciona la posicion de la salida y de zodiac
  for x in range(1,tamano-1):
    lista_posibles_salidas.append([0,x])
    lista_posibles_salidas.append([tamano -1,x])
    lista_posibles_salidas.append([x,0])
    lista_posibles_salidas.append([x,tamano -1])
  for x in range(1,4):  
    lista_posibles_salidas.remove([x,0])
    lista_posibles_salidas.remove([0,x])
  # Para dificultad 1 hay solo 2 salidas y para 2 son 4. Solo 1 salida es la correcta
  lista_posicion_salida = random.sample(lista_posibles_salidas,dificultad*2)  
  for salidas in lista_posicion_salida:
    j, i = salidas
    laberinto[j][i] = "O"
    if j == 0:
      posicion_zodiac = [j+1,i]
    elif j == tamano -1:
      posicion_zodiac = [j-1,i]
    elif i == 0: 
      posicion_zodiac = [j,i+1]
    elif i == tamano -1:
      posicion_zodiac = [j,i-1]
    lista_posicion_zodiac.append(posicion_zodiac)    
  for x in lista_posicion_zodiac:
    j, i = x
    laberinto[j][i] = "Z"
    lista_eliminar_de_grid.append(x)

  return laberinto, tamano, dificultad, lista_eliminar_de_grid, lista_posicion_zodiac, lista_posicion_salida


def mostrar_laberinto(laberinto):
  for fila in laberinto:
    print(fila)
  return
    

def movimiento(posicion_inicial, laberinto):
  menu_opciones = (
        "\nMenú de opciones:\n"
        "1. Arriba\n"
        "2. Derecha\n"
        "3. Abajo\n"
        "4. Izquierda\n"
        "\n"
         "Eliga un movimiento: "
        )
  while True:
    try:
  
      jugada = int(input(menu_opciones))
      if jugada not in range (1, 5):
        raise ValueError("El numero debe estar entre 1-4")
      if jugada in range (1, 5):
        if jugada ==1:
          x, y = -1, 0 
        elif jugada == 2:
          x, y = 0, 1
        elif jugada == 3:
          x, y = 1, 0
        elif jugada == 4:
          x, y = 0, -1   
        a, b = posicion_inicial
        posicion_final = [a + x, b + y]
        if laberinto[a + x][b + y] == "#":
          print("La jugada no es valida")
        else:
          break
    except ValueError:
      print("Debe introducir un valor de 1-4")
  return posicion_final
 




def condiciones_iniciales(laberinto, tamano, dificultad, lista_eliminar_de_grid, lista_posicion_zodiac, lista_posicion_salida):
  # en esta funciones reaizaremos una asignacion aleatoria de las posiciones de los monstruos, del veneno, de las armas secretas y de la vida extra.
  
  #lista_grid es donde podremos extraer las ubicaciones
  lista_grid = []
  #en esta lista almacenamos las posiciones extraidas de lista_grid
  lista_posiciones = []
  #creamos 2 diccionarios. Uno donde los keys son los eventos y otro donde las ubicaciones lo son
  diccionario_posiciones = {}
  diccionario_eventos = {}
  for z in range(1, tamano -1):
    for y in range(1, tamano-1):
      lista_grid.append([z, y])
  #Quitamos estas posiciones iniciales, las ocupadas por zodiac y obstaculos:
  lista_grid.remove([1,2])    
  lista_grid.remove([2,1]) 
  lista_grid.remove([2,2]) 
  lista_grid.remove([1,1])
  for x in lista_eliminar_de_grid:
    lista_grid.remove(x) 
  
  # 3 posiciones de monstruos. 3 de puzzles energia. 3 de puzzles con pistas. 3 de vida extra. x de veneno (8 dificil, 16 extremo). 2-4 pociones de energia (+ 50 cada una) 
  if dificultad == 1:
    numero_trampas = 8
    cantidad_vida_extra = 3
    cantidad_pociones_energia = 2
    cantidad_posiciones_aleatorias = 22
    # falta elegir los puzzles de una lista si es dificil o extremo

  elif dificultad == 2:
    numero_trampas = 16
    cantidad_vida_extra = 5
    cantidad_pociones_energia = 4
    cantidad_posiciones_aleatorias = 34

  while cantidad_posiciones_aleatorias != 0:
    extraer_posicion = random.choice(lista_grid) 
    lista_posiciones.append(extraer_posicion)
    lista_grid.remove(extraer_posicion)
    cantidad_posiciones_aleatorias -= 1
  posiciones_monstruos = []
  posiciones_puzzles_energia = []
  posiciones_puzzles_pistas = []
  posiciones_vida_extra = []
  posiciones_trampas = []
  posiciones_energia = []
  for x in range(0,3):
    posiciones_monstruos.append(lista_posiciones[x]) 
    diccionario_posiciones[tuple(lista_posiciones[x])] = "Monstruo"
  diccionario_eventos["Monstruo"] = posiciones_monstruos
  for x in range(3,6):
    posiciones_puzzles_energia.append(lista_posiciones[x])   
    diccionario_posiciones[tuple(lista_posiciones[x])] = "Puzzles de energia"
  diccionario_eventos["Puzzles de energia"] = posiciones_puzzles_energia    
  for x in range(6,9):
    posiciones_puzzles_pistas.append(lista_posiciones[x]) 
    diccionario_posiciones[tuple(lista_posiciones[x])] = "Puzzles con pistas" 
  diccionario_eventos["Puzzles con pistas"] = posiciones_puzzles_pistas  
  for x in range(9,9+cantidad_vida_extra):
    posiciones_vida_extra.append(lista_posiciones[x])
    diccionario_posiciones[tuple(lista_posiciones[x])] = "Vida extra" 
  diccionario_eventos["Vida extra"] = posiciones_vida_extra        
  for x in range(9+cantidad_vida_extra,9+cantidad_vida_extra+numero_trampas):
    posiciones_trampas.append(lista_posiciones[x])
    diccionario_posiciones[tuple(lista_posiciones[x])] = "Trampas"   
  diccionario_eventos["Trampas"] = posiciones_trampas      
  for x in range(9+cantidad_vida_extra+numero_trampas, 9+cantidad_vida_extra+numero_trampas+cantidad_pociones_energia):
    posiciones_energia.append(lista_posiciones[x])
    diccionario_posiciones[tuple(lista_posiciones[x])] = "Energia"     
  diccionario_eventos["Energia"] = posiciones_energia
  laberinto[1][1] = "P"
  for x in range(0,3):
    # utilizaremos m, n para describir las posiciones de los puzzles de energia. w y q para los puzzles con pistas
    m, n = diccionario_eventos["Puzzles de energia"][x]
    laberinto[m][n] = "?"
    w, q = diccionario_eventos["Puzzles con pistas"][x]
    laberinto[w][q] = "?"
  for x in range(0,cantidad_vida_extra): 
    m, n = diccionario_eventos["Vida extra"][x]
    laberinto[m][n] = "+"  
  #Creamos los puzzles_pistas
  puzzles_energia = {}
  puzzles_pistas = {}
  lista_posiciones_monstruos = diccionario_eventos["Monstruo"] 
  lista_puzzles_pistas = diccionario_eventos["Puzzles con pistas"] 
  for m in range(0,3):
    x , y = lista_posiciones_monstruos[m]
    w, q = lista_puzzles_pistas [m]
    posicion_y = x - w
    posicion_x = y - q
    mensaje_pista = f"En [{posicion_y} (eje Y),{posicion_x} (eje X)] de donde estas yace algo monstruoso"
    puzzles_pistas[(w,q)] = [mensaje_pista, [x , y] ]
  #ahora creamos el puzzle_energia: chatGPT nos puede crear una lista de diccionarios para elegir aleatoriamente segun la dificultad.

  puzzles_dificil = [
    {
        "enunciado": "Soy alto cuando soy joven y corto cuando soy viejo. ¿Qué soy?",
        "respuesta_correcta": "Una vela",
        "opciones": ["Un árbol", "Una vela", "Una montaña", "Un río"]
    },
    {
        "enunciado": "Si me nombras, desaparezco. ¿Qué soy?",
        "respuesta_correcta": "El silencio",
        "opciones": ["El viento", "La sombra", "El silencio", "El eco"]
    },
    {
        "enunciado": "Tengo ciudades pero no casas, montañas pero no árboles y agua pero no peces. ¿Qué soy?",
        "respuesta_correcta": "Un mapa",
        "opciones": ["Un espejo", "Un sueño", "Un mapa", "Una pintura"]
    },
    {
        "enunciado": "Avanzo y nunca retrocedo. Nadie me ve, pero todos me sienten. ¿Qué soy?",
        "respuesta_correcta": "El tiempo",
        "opciones": ["El viento", "El tiempo", "La oscuridad", "La gravedad"]
    },
    {
        "enunciado": "¿Qué objeto tiene agujeros por todas partes y aun así puede contener agua?",
        "respuesta_correcta": "Una esponja",
        "opciones": ["Un colador", "Una esponja", "Una red", "Un cubo"]
    },
    {
        "enunciado": "¿Cuál es la palabra que se escribe incorrectamente en todos los diccionarios?",
        "respuesta_correcta": "Incorrectamente",
        "opciones": ["Increíble", "Incorrectamente", "Imposible", "Indescriptible"]
    },
    {
        "enunciado": "Me rompo sin ser tocado, y si me nombras, desaparezco. ¿Qué soy?",
        "respuesta_correcta": "El silencio",
        "opciones": ["Una promesa", "Una burbuja", "El silencio", "Un hechizo"]
    },
    {
        "enunciado": "¿Qué es tan frágil que al decir su nombre lo rompes?",
        "respuesta_correcta": "El silencio",
        "opciones": ["El cristal", "El silencio", "Una sombra", "Un sueño"]
    },
    {
        "enunciado": "¿Qué puede viajar por el mundo mientras permanece en una esquina?",
        "respuesta_correcta": "Un sello postal",
        "opciones": ["Una sombra", "Un sello postal", "Un recuerdo", "Un susurro"]
    }
    ]

  puzzles_extremo = [
    {
        "enunciado": "Un hombre mira un retrato y dice: 'No tengo hermanos ni hermanas, pero el padre de este hombre es el hijo de mi padre'. ¿A quién pertenece el retrato?",
        "respuesta_correcta": "A su hijo",
        "opciones": ["A él mismo", "A su hijo", "A su padre", "A su sobrino"]
    },
    {
        "enunciado": "En un cuarto hay 100 personas. Todas menos 5 salen. ¿Cuántas personas quedan en el cuarto?",
        "respuesta_correcta": "5",
        "opciones": ["95", "5", "0", "100"]
    },
    {
        "enunciado": "Tres médicos dicen que Robert es su hermano, pero Robert dice que no tiene hermanos. ¿Cómo es posible?",
        "respuesta_correcta": "Los médicos son sus hermanas",
        "opciones": ["Robert miente", "Son medio hermanos", "Los médicos son sus hermanas", "No es el mismo Robert"]
    },
    {
        "enunciado": "Tengo dos monedas que suman 30 céntimos, y una de ellas no es de 10 céntimos. ¿Qué monedas tengo?",
        "respuesta_correcta": "Una de 20 céntimos y una de 10 céntimos",
        "opciones": ["Dos de 15 céntimos", "Una de 20 céntimos y una de 10 céntimos", "Tres de 10 céntimos", "Una de 25 céntimos y una de 5 céntimos"]
    },
    {
        "enunciado": "Un prisionero es condenado a muerte. Se le da la opción de elegir su forma de ejecución: si dice una mentira, será electrocutado; si dice la verdad, será ahorcado. El prisionero dice una frase y es liberado. ¿Qué dijo?",
        "respuesta_correcta": "'Me van a electrocutar'",
        "opciones": ["'Me van a electrocutar'", "'Me van a ahorcar'", "'Soy culpable'", "'No diré nada'"]
    },
    {
        "enunciado": "Un hombre sale a caminar bajo la lluvia torrencial sin paraguas ni sombrero. Su ropa se empapa, pero ni un solo cabello de su cabeza se moja. ¿Cómo es posible?",
        "respuesta_correcta": "Es calvo",
        "opciones": ["Usa impermeable", "La lluvia es mágica", "Es calvo", "Camina bajo un techo"]
    },
    {
        "enunciado": "¿Cuál es el número que, si lo multiplicas por cualquier otro número, el resultado siempre será el mismo?",
        "respuesta_correcta": "Cero",
        "opciones": ["Uno", "Cero", "Infinito", "El número mismo"]
    },
    {
        "enunciado": "Un agricultor tiene 17 ovejas. Todas menos 9 mueren. ¿Cuántas ovejas le quedan?",
        "respuesta_correcta": "9",
        "opciones": ["0", "8", "9", "17"]
    },
    {
        "enunciado": "Lo puedes sostener sin usar tus manos ni brazos. ¿Qué es?",
        "respuesta_correcta": "El aliento",
        "opciones": ["El tiempo", "El aliento", "La respiración", "La paciencia"]
    }
    ]
  if dificultad == 1:
    puzzles_segun_dificultad = puzzles_dificil
  elif dificultad == 2:
    puzzles_segun_dificultad = puzzles_extremo
  puzzles_seleccionados = random.sample(puzzles_segun_dificultad, 3)
  for i in range(0,3):
    posicion_puzzle = diccionario_eventos["Puzzles de energia"][i]
    puzzles_energia[tuple(posicion_puzzle)] = puzzles_seleccionados[i]
  #Ahora definimos un diccionario con salidas (1 salida es correcta) 
  salida_correcta = random.choice(lista_posicion_salida) 
  lista_posicion_salida.remove(salida_correcta)
  diccionario_salidas = {}
  diccionario_salidas[tuple(salida_correcta)] = "Salida correcta"
  for incorrecta in lista_posicion_salida:
    diccionario_salidas[tuple(incorrecta)] = "Salida incorrecta"
  #ahora creamos los puzzles del zodiac, una lista de diccionarios creada con chatgpt.

  puzzle_zodiac_dificil = [
      {
          'enunciado': 'Soy un número entero positivo que al multiplicarme por dos y sumarle tres da el mismo resultado que al elevarme al cuadrado. ¿Quién soy?',
          'respuesta_correcta': 'TRES'
      },
      {
          'enunciado': 'En un estanque hay nenúfares que duplican su área cada día. Si en 30 días cubren todo el estanque, ¿en cuántos días cubrían la mitad?',
          'respuesta_correcta': 'VEINTINUEVE'
      },
      {
          'enunciado': 'Tengo ciudades pero no casas, montañas pero no árboles, y agua pero no peces. ¿Qué soy?',
          'respuesta_correcta': 'MAPA'
      },
      {
          'enunciado': 'Soy un número cuyo número de letras en español es igual a mi valor. ¿Qué número soy?',
          'respuesta_correcta': 'CINCO'
      },
      {
          'enunciado': 'Siempre estoy delante de ti, pero nunca me verás. ¿Qué soy?',
          'respuesta_correcta': 'FUTURO'
      },
      {
          'enunciado': 'Un hombre mira un retrato y dice: "No tengo hermanos ni hermanas, pero el padre de ese hombre es el hijo de mi padre". ¿A quién está mirando?',
          'respuesta_correcta': 'HIJO'
      },
      {
          'enunciado': 'Si me nombras, desaparezco. ¿Qué soy?',
          'respuesta_correcta': 'SILENCIO'
      },
      {
          'enunciado': 'Tiene agujeros por todas partes y aun así puede contener agua. ¿Qué es?',
          'respuesta_correcta': 'ESPONJA'
      },
      {
          'enunciado': 'Avanzo sin caminar, tengo boca pero no hablo, tengo un lecho pero no duermo. ¿Qué soy?',
          'respuesta_correcta': 'RIO'
      },
      {
          'enunciado': 'Me puedes romper sin tocarme ni verme. ¿Qué soy?',
          'respuesta_correcta': 'PROMESA'
      },
      {
          'enunciado': 'Tengo teclas pero no puertas, espacio pero no habitaciones, y puedes entrar pero no salir. ¿Qué soy?',
          'respuesta_correcta': 'TECLADO'
      },
      {
          'enunciado': 'Vuelo sin alas y lloro sin ojos. ¿Qué soy?',
          'respuesta_correcta': 'NUBE'
      },
      {
          'enunciado': 'Cuanto más seco, más mojo. ¿Qué soy?',
          'respuesta_correcta': 'TOALLA'
      },
      {
          'enunciado': 'Todos me tienen pero nadie puede perderme. ¿Qué soy?',
          'respuesta_correcta': 'SOMBRA'
      },
      {
          'enunciado': 'Cuanto más hay de mí, menos ves. ¿Qué soy?',
          'respuesta_correcta': 'OSCURIDAD'
      },
      {
          'enunciado': 'No tengo vida, pero puedo morir. ¿Qué soy?',
          'respuesta_correcta': 'BATERIA'
      }
  ]

  # Lista de puzzles de dificultad "extremo"
  puzzle_zodiac_extremo = [
      {
          'enunciado': 'En una calle hay cinco casas de diferentes colores. En cada casa vive una persona de distinta nacionalidad. Cada propietario bebe una bebida, fuma una marca de cigarrillos y tiene una mascota diferentes. El británico vive en la casa roja. El sueco tiene perros. El danés bebe té. La casa verde está a la izquierda de la blanca. El dueño de la casa verde bebe café. La persona que fuma Pall Mall cría pájaros. El propietario de la casa amarilla fuma Dunhill. El hombre que vive en la casa del centro bebe leche. El noruego vive en la primera casa. El hombre que fuma Blends vive al lado del que tiene gatos. El hombre que tiene caballos vive al lado del que fuma Dunhill. El propietario que fuma BlueMaster bebe cerveza. El alemán fuma Prince. El noruego vive al lado de la casa azul. El hombre que fuma Blends tiene un vecino que bebe agua. ¿Quién es el dueño del pez?',
          'respuesta_correcta': 'ALEMAN'
      },
      {
          'enunciado': 'Soy un número de cuatro dígitos que es simultáneamente un cuadrado perfecto y un cubo perfecto. ¿Qué número soy?',
          'respuesta_correcta': 'CUATROMILNOVENTAYSEIS'
      },
      {
          'enunciado': 'En una isla hay un tesoro enterrado. Las instrucciones dicen: "Desde el viejo roble, camina 50 pasos al norte hasta una roca. Desde allí, 30 pasos al este hasta una palmera. Luego, 40 pasos al sur hasta el punto exacto". Sin embargo, al llegar, descubres que la palmera ha sido talada. ¿Cómo encuentras el tesoro?',
          'respuesta_correcta': 'MEDIANTE'
      },
      {
          'enunciado': 'Un hombre debe transportar un lobo, una cabra y una col al otro lado de un río. Solo puede llevar consigo una cosa a la vez, y si deja al lobo con la cabra, el lobo se comerá a la cabra. Si deja a la cabra con la col, la cabra se comerá la col. ¿Cómo lo hace?',
          'respuesta_correcta': 'INGENIO'
      },
      {
          'enunciado': 'En un país, solo se permiten monedas de 3 y 5 unidades. ¿Cuál es el mayor monto que no se puede obtener con estas monedas?',
          'respuesta_correcta': 'SIETE'
      },
      {
          'enunciado': 'Encuentra el número entero positivo más pequeño que al dividirlo por 2, 3, 4, 5 y 6 deja un resto de 1 en cada caso.',
          'respuesta_correcta': 'SESENTA Y UN'
      },
      {
          'enunciado': 'Tres personas comparten un hotel que cuesta 30 dólares. Cada uno paga 10 dólares. Más tarde, el recepcionista se da cuenta de que el hotel solo cuesta 25 dólares y envía al botones a devolver 5 dólares. El botones, sin embargo, decide quedarse con 2 dólares y devuelve 1 dólar a cada persona. Así, cada persona ha pagado 9 dólares, sumando 27 dólares, más los 2 dólares que tiene el botones, suman 29 dólares. ¿Dónde está el dólar faltante?',
          'respuesta_correcta': 'PARADOJA'
      },
      {
          'enunciado': 'Si A es el hermano de B, B es la hermana de C, y C es el padre de D, ¿cómo está A relacionado con D?',
          'respuesta_correcta': 'TIO'
      },
      {
          'enunciado': 'En un torneo de ajedrez, cada jugador juega exactamente una vez contra cada uno de los otros jugadores. Si se jugaron 45 partidas en total, ¿cuántos jugadores participaron?',
          'respuesta_correcta': 'DIEZ'
      },
      {
          'enunciado': 'Eres un prisionero frente a dos puertas custodiadas por dos guardias. Una puerta lleva a la libertad y la otra a la muerte. Un guardia siempre dice la verdad y el otro siempre miente, pero no sabes quién es quién. Solo puedes hacer una pregunta para decidir qué puerta elegir. ¿Qué pregunta haces?',
          'respuesta_correcta': 'PUERTA'
      },
      {
          'enunciado': 'Un hombre nace en 1995 y muere en 1953. ¿Cómo es posible?',
          'respuesta_correcta': 'CALENDARIO'
      },
      {
          'enunciado': 'Tienes 12 bolas idénticas, pero una pesa diferente. Usando una balanza de dos platillos solo tres veces, ¿cómo identificas la bola diferente?',
          'respuesta_correcta': 'PESANDO'
      },
      {
          'enunciado': 'En una caja hay dos tarjetas: una es negra por ambos lados y la otra es blanca por ambos lados. Sacas una tarjeta al azar y uno de sus lados es negro. ¿Cuál es la probabilidad de que el otro lado también sea negro?',
          'respuesta_correcta': 'DOS-TERCIOS'
      },
      {
          'enunciado': 'Hay 100 prisioneros numerados del 1 al 100. El director coloca 100 cajas en una sala, cada una con un número dentro. Cada prisionero puede abrir 50 cajas. Si todos encuentran su número, son liberados. Si alguno falla, todos son ejecutados. ¿Qué estrategia deben seguir?',
          'respuesta_correcta': 'CICLOS'
      },
      {
          'enunciado': 'Encuentra el número menor entero positivo que es divisible por 1 a 10 sin dejar resto.',
          'respuesta_correcta': 'DOSCIENTOCINCUENTA'
      },
      {
          'enunciado': 'Si 2^x = 8 y 3^y = 27, ¿cuánto es x + y?',
          'respuesta_correcta': 'CINCO'
      },
      {
          'enunciado': 'Un reloj da las campanadas en las horas en punto. ¿Cuántas veces suena la campana en un día completo?',
          'respuesta_correcta': 'OCHENTA Y SEIS'
      }
  ]
  if dificultad == 1:
    puzzles_zodiac = random.sample(puzzle_zodiac_dificil, 2)
  elif dificultad == 2:
    puzzles_zodiac = random.sample(puzzle_zodiac_extremo, 4)  

  return laberinto, lista_posiciones, diccionario_posiciones, puzzles_energia, puzzles_pistas, puzzles_zodiac, diccionario_salidas


def mostrar_estado(vida, gemas, energia):
  if not gemas:
    mensaje_estado = f"Tienes {vida} de vida, {energia} de energia y todavia no tienes las Gemas del heroe legendario"
  elif gemas:
    mensaje_estado = f"Tienes {vida} de vida, {energia} de energia y tienes las gemas {gemas}"
  print(mensaje_estado)
  return  

def cambiar_posicion(posicion_inicial, valor, laberinto):
  x, y = posicion_inicial
  laberinto[x][y] = valor
  return laberinto

def juego_laberinto():
  print("Bienvenido al juego del laberinto. No te pierdas en el. \n Este juego es para los valientes de corazon")
  laberinto, tamano, dificultad, lista_eliminar_de_grid, lista_posicion_zodiac, lista_posicion_salida = crear_laberinto()
  laberinto, lista_posiciones, diccionario_posiciones, puzzles_energia, puzzles_pistas, puzzles_zodiac, diccionario_salidas = condiciones_iniciales(laberinto, tamano, dificultad, lista_eliminar_de_grid, lista_posicion_zodiac, lista_posicion_salida)
  gemas = []
  extraer_gemas = ["Sabiduria", "Coraje", "Templanza"]
  energia = 0
  vida = 100*(dificultad + 2)
  posicion_inicial = [1, 1]
  mensaje_inicial =(f"El objetivo del juego es salir del laberinto con vida. En la salida del laberinto ('O') te espera el Final Boss Zodiac ('Z'), el guardian del Laberinto,\n"
                     "el cual usa tacticas de confusion, retos y acertijos para que solamente los dignos puedan vencer su Laberinto.\n"
                     "Una de sus tacticas es crear ilusiones de salidas del laberinto para confundir a los viajeros.\n"
                    "Solamente hay una salida al laberinto! Tendras que adivinar y confiar en el destino.\n"
                     "Para poder enfrentarte a 'Z', tendras que conseguir las 'Gemas del Heroe Legendario':\n"
                     "a) Sabiduria.\n"
                     "b) Coraje\n"
                     "c) Templanza\n"
                     "Estas gemas son custodiadas por terribles monstruos que acechan el laberinto, a los que no podras ver en el mapa.\n"
                     "Deberas ir a su encuentro, y una vez que te topes con ellos mostraran su verdadero rostro ('M').\n"
                     "Pero no tan rapido! Antes de pelear con ellos necesitas recolectar energia, la cual obtienes superando los 'acertijos' de Zodiac ('?')\n"
                     "Ten cuidado, los puzzles te quitaran vida por cada respuesta incorrecta.\n"
                     "Iniciaras el juego con {vida} de vida y {energia} de energia. Ten cuidado en tu viaje, en el laberinto hay trampas invisibles ('T') que te quitaran 30 de vida si caes en ellas\n"
                     "Como ayuda, tendras unas pociones con el elixir de la vida (marcadas por '+') que te daran 40 de vida extra.\n"
                     "Verdad! un ultimo detalle. Por un hechizo de Zodiac, en cada movimiento perderas 5 de vida!"
                  )
  print(mensaje_inicial)
  mostrar_laberinto(laberinto)
  print("Esta es tu posicion inicial. Buena suerte!")
  mostrar_estado(vida, gemas, energia)
  #Aca empezamos con la primera jugada

  while  vida >= 0:
    posicion_final = movimiento(posicion_inicial, laberinto)
    inicial_y, inicial_x = posicion_inicial
    m, n = posicion_final
    #Para cuando en el turno anterior el jugador se topo con una salida falsa o una trampa y se pueda mostrar su estado.
    if tuple(posicion_inicial) in diccionario_posiciones:
      if diccionario_posiciones[tuple(posicion_inicial)] == "Trampa":
        laberinto[inicial_y][inicial_x] = "T"
    if laberinto[inicial_y][inicial_x] == "O":
      laberinto[inicial_y][inicial_x] = "#"
    if laberinto[m][n] == "O":
      if diccionario_salidas[m, n] == "Salida correcta":
        laberinto = cambiar_posicion(posicion_final, "x", laberinto)
        mostrar_laberinto(laberinto)
        vida -= 5
        mostrar_estado(vida, gemas, energia)
        print("ZODIAC: Felicitaciones, conseguiste salir del Laberinto. Eres el primero en siglos!\n Eres digno de salir con vida. Sin duda eres el heroe que la leyenda prometio.")
        return
      else:
        print("Esta salida era una ilusion de Zodiac!\n Animo! Intenta con otra salida del Laberinto")  
    #Definimos los tipos de eventos:  
    elif posicion_final in lista_posiciones:
      tipo_evento = diccionario_posiciones[tuple(posicion_final)]
      if tipo_evento == "Trampa":
        print("Te topaste con una trampa, tienes -20 de vida")
        vida -= 20
        lista_posiciones.remove(posicion_final)
      elif tipo_evento == "Energia": 
        print("Felicitaciones, te encontraste con 50 de energia!")
        energia += 50 
        lista_posiciones.remove(posicion_final)

      elif tipo_evento == "Vida extra": 
        print("Conseguiste +50 de Vida!")
        vida += 50 
        lista_posiciones.remove(posicion_final)
      elif tipo_evento == "Monstruo":
        laberinto[m][n] = "M"
        print("Peligro! Te encontraste un monstruo!")
        if energia >= 100:
          print(f"Pero tienes suficiente energia para vencerlo: {energia} Energia")
          premio = random.choice(extraer_gemas)
          gemas.append(premio)
          extraer_gemas.remove(premio)
          energia -= 100
          lista_posiciones.remove(posicion_final)
          print(f"Felicitaciones! Conseguiste {premio}")
          if len(gemas) == 3:
            print("Ya tienes todas las Gemas del Heroe Legendario para enfrentarte al 'Z'.\n El camino del heroe te espera")
          else:
            print(f"Te falta {3 - len(gemas)} de las gemas Todavia no puedes enfrentarte a 'Z'")  
        elif energia < 100:
          resto = 100 - energia
          print(f"No tienes suficiente energia para vencer al monstruo. Te falta {resto} de energia")
          vida -= 30
          #el jugador regresa a la posicion inicial del juego como castigo
          posicion_final = [1, 1]
          print("El monstruo te ha quitado -30 de vida y con su hechizo te ha llevado a la posicion inicial")
      elif tipo_evento == "Puzzles de energia":
        print("Te has encontrado con un puzzle. Resuelvelo para conseguir 100 de energia!")
        #Completar. Cada opcion incorrecta se resta 15 de vida.
        puzzle = puzzles_energia[tuple(posicion_final)]  
        opciones = puzzle["opciones"].copy()
        random.shuffle(opciones)
        # Crear un diccionario para mapear letras a opciones
        letras_opciones = ['a', 'b', 'c', 'd']
        mapeo_opciones = dict(zip(letras_opciones, opciones))
        print(puzzle["enunciado"])
        for letra, opcion in mapeo_opciones.items():
            print(f"{letra}) {opcion}") 
        respuesta = input("Tu respuesta: ").lower()
        while respuesta not in letras_opciones:
          respuesta = input("Por favor ingresa una opción válida (a/b/c/d): ").lower()
          # Comprobar si la respuesta es correcta
        while  mapeo_opciones[respuesta] != puzzle["respuesta_correcta"]:
          print("¡Incorrecto! Pierdes 20 de vida")
          vida -= 20
          respuesta = input("Intentalo otra vez: ").lower()
        print("Respuesta correcta. Has ganado 100 de energia! Esto te servira para vencer a los monstruos que acechan el laberinto") 
        energia += 100
        lista_posiciones.remove(posicion_final) 

      elif tipo_evento == "Puzzles con pistas":  
        print("Valiente viajero, gracias por querer salvarnos del horror. Como ayuda te dare un mensaje de salvacion")
        #posicion del monstruo relacionado a este puzzle para mostrarlo en el laberinto
        posicion_monstruo = puzzles_pistas[(m, n)][1]
        if posicion_monstruo in lista_posiciones:
          posicion_monstruo_y, posicion_monstruo_x  = posicion_monstruo 
          mensaje = puzzles_pistas[(m, n)][0]
          print(mensaje)
          laberinto[posicion_monstruo_y][posicion_monstruo_x] = "M"
        elif posicion_monstruo not in lista_posiciones:
          print("El mal que acechaba ya ha sido derrotado")

    #Ahora el enfrentamiento con Zodiac:
    elif laberinto[m][n] == "Z": 
      if len(gemas) < 3:
        print("ZODIAC: En el Laberinto de Zodiac no hay atajos.\nNo eres digno de salir con vida de mi Laberinto.")  
        print("FIN DEL JUEGO. INTENTALO OTRA VEZ")
        return
      elif len(gemas) == 3:
        puzzle_aleatorio = random.choice(puzzles_zodiac)
        print("ZODIAC: De este Laberinto no sale con vida ningun hombre ordinario. \nDebes demostrar ser digno y pasar mi prueba.\n Preparate, que no tendre piedad en eliminarte")
        enunciado_zodiac = puzzle_aleatorio['enunciado']
        adivinanza = puzzle_aleatorio['respuesta_correcta']
        lista_letras_avidinadas = []
        errores = 0
        print("ZODIAC: Deberas resolver el siguiente puzzle. Tendras hasta 5 intentos para completarlo\n Escribe una letra que crees que contiene la respuesta")    
        print(enunciado_zodiac) 
        representacion_oculta = ["_"]*len(adivinanza)
        

        while vida > 0 and errores < 5:  
          #Funcion para crear el mensaje con '_' para letras sin adivinar  la letras para las adivinadas
          print("El codigo secreto es:", ' '.join(representacion_oculta))
          while True:
              respuesta_jugador = input(f"Errores {errores}. Letras ocultas: {len(adivinanza) - len(lista_letras_avidinadas)}.\n Coloca una de ellas:  ").upper()
              if len(respuesta_jugador) == 1 and respuesta_jugador.isalpha():
                if respuesta_jugador in lista_letras_avidinadas:
                  print("Esta letra ya la has adivinado")
                else:
                  break
              else:
                print("Debe introducir una letra")

          if respuesta_jugador in adivinanza:
            for indice, letra in enumerate(adivinanza):
              if letra == respuesta_jugador:
                representacion_oculta[indice] = respuesta_jugador
                lista_letras_avidinadas.append(letra)
            print("Correcto")
            if "_" not in representacion_oculta:
              print("ZODIAC: Felicitaciones, has completado el puzzle. La salida del laberinto te espera.")
              #Aca recien poner la eliminacion del puzzle de zodiac.
              puzzles_zodiac.remove(puzzle_aleatorio)
              break
          else:
            print("Error! Pierdes 10 de vida")   
            errores += 1
            vida -= 10
          

        if vida <= 0:
          print("Perdiste! Te quedaste sin vida.Tranquilo, no eres el primero en perderse en el laberinto.\n Tu valor no sera olvidado!")
          print("FIN DEL JUEGO")
          return
        if errores == 5:
          print(f"ZODIAC: Superaste el numero de intentos ({errores}). Por misericordia, te dare otra oportunidad, regresaras al inicio del laberinto")
          posicion_final = [1, 1]  

    vida -= 5
    laberinto = cambiar_posicion(posicion_inicial, "x", laberinto)
    laberinto = cambiar_posicion(posicion_final, "P", laberinto)
    posicion_inicial[:] = posicion_final
    mostrar_laberinto(laberinto)
    mostrar_estado(vida, gemas, energia)  
  print("Perdiste! Te quedaste sin vida.Tranquilo, no eres el primero en perderse en el laberinto.\n Tu valor no sera olvidado!")
  print("FIN DEL JUEGO. INTENTALO OTRA VEZ")
  return

#Probamos el juego
juego_laberinto()








