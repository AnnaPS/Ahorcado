# Ana e Iván

#-*- coding: UTF-8 -*-
import random
'''
Variables del Ahorcado.
'''

moneco = ('''
    |\____________
    \|           #
    |\           #
    \|           
    |\          
    \|         
    |\       
    \|      
    |\     
    \|       
    |\      
    \|  /\_/\             
    |\ (◔ᴗ◔ ) @
    \|_(m__m)()______________
    '''
    ,
    '''
    |\____________
    \|           #
    |\           #
    \|         (◕︵◕)  
    |\          
    \|         
    |\       
    \|      
    |\     
    \|       
    |\      
    \|  /\_/\             
    |\ (◔ᴗ◔ ) @
    \|_(m__m)()______________
    '''
    ,
    '''
    |\____________            
    \|           #             
    |\           #               
    \|         (◕︵◕)            
    |\           ¡               
    \|         /   \           
    |\          | |             
    \|                          
    |\                        
    \|                       
    |\                      
    \|                      
    |\                       
    \|                      
    |\                      
    \|  /\_/\                 
    |\ (◔ᴗ◔ ) @              
    \|_(m__m)()______________
    '''  
    ,
    '''
    |\____________                  
    \|           #           
    |\           #               
    \|         (◕︵◕)       
    |\           ¡          
    \|         /   \         
    |\        / | | \       
    \|       /  |*|  \       
    |\                      
    \|                      
    |\                      
    \|                     
    |\                     
    \|                     
    \|  /\_/\              
    |\ (◔ᴗ◔ ) @            
    \|_(m__m)()____________
    '''
    ,
    '''
    |\____________
    \|           #                 
    |\           #                 
    \|         (◕︵◕)              
    |\           ¡               
    \|         /   \             
    |\        / | | \              
    \|       /  |*|  \             
    |\      ''  / \  ''            
    \|                           
    |\                           
    \|                           
    |\                           
    \|                           
    \|  /\_/\                    
    |\ (◔ᴗ◔ ) @                  
    \|_(m__m)()__________________
    '''
    ,
    '''
    |\____________
    \|           #              
    |\           #               
    \|         (◕︵◕)            
    |\           ¡                 
    \|         /   \             
    |\        / | | \             
    \|       /  |*|  \            
    |\      '' /  \  ''           
    \|        /    \            
    |\       /      \           
    \|                               
    |\                          
    \|                          
    \|  /\_/\                   
    |\ (◔ᴗ◔ ) @                 
    \|_(m__m)()________________ 
    '''
    ,
    '''
    |\___________              |
    \|          #              |
    |\          #              |
    \|        (x_x)            |
    |\          ¡              |
    \|        /   \            |
    |\       / | | \           |
    \|      /  |*|  \          |
    |\     '' /   \ ''         |
    \|       /     \           |
    |\      /       \          |
    \|    @@         @@        |
    |\                         |
    \|                         |
    \|  /\_/\                  |
    |\ (◔ᴗ◔ )@                 |
    \|_(m__m)()______________  |
    ''')
comida = ["PAELLA", "CALAMARES", "CHIPIRONES", "TORREZNOS", "TORTILLA", "MIGAS", "COCIDO", "LENTEJAS", "TOMATES", "GAMBAS", "PATATAS", "FIDEUA", "SOCARRAT", "BACALAO", "GAZPACHO", "CROQUETAS"]
animales = ["ABEJA", "ARAÑA", "BALLENA", "BURRO", "CABALLO", "CARACOL", "CEBRA", "CERDO", "CANARIO", "CAMELLO", "GALLINA", "GATO", "PERRO", "LORO", "MURCIELAGO", "HIPOPOTAMO"]
deporte = ["ATLETISMO", "SURF", "BADMINTON", "BALONCESTO", "BALONMANO", "BEISBOL", "BOXEO", "HOCKEY", "CICLISMO", "ESQUI", "CRIQUET", "GOLF", "KARATE", "JUDO", "WATERPOLO", "RUGBY"]
listaCompleta = (comida, animales, deporte)
estadoMoneco = 0
pistas = ["¡¡¡PISTA!!!:Es una comida.", "¡¡¡PISTA!!!:Es un animal.", "¡¡¡PISTA!!!:Es un deporte."]
numPista = 0
listaLetrasFalladas = []
letra = ""
palabraSecreta = ""        
palabraAdivinar = ""
puntuacionJugador = 0
nombreUsu = ""
respuesta = "s"
acabose = False
totalAcertadas = 0
totalFalladas = 0
totalPuntuacion = 0
''' Fin de las variables'''

'''
    Pedimos el nomnre al jugador
'''


def pedirNombre(nombreUsu):
    nombreUsu = input("   Inserte su nombre, por favor: ")
    return nombreUsu


''' 
Metodo que se encarga de cargar una palabra aleatoria, 
    de cualquiera de las 3 listas disponibles
'''  


def cargarPalabra(listaCompleta, palabraAdivinar):
    numRListaCompleta = random.randint(0, 2)
    listaElegida = listaCompleta[numRListaCompleta]
    numRLista = random.randint(0, len(listaElegida) - 1)
    palabraAdivinar = listaElegida[numRLista]
    pista(listaCompleta, palabraAdivinar, pistas, numPista)
    del listaElegida[numRLista]
    return palabraAdivinar


''' 
Metodo que busca que lista fue la elegida y muestra una pista 
    segun el tema elegido
    
    Indice 0= lista de comida
    Indice 1= lista de animales
    Indice 2= lista de deportes
'''

   
def pista(listaCompleta, palabraAdivinar, pistas, numPista):
    cont = 0
    for l in listaCompleta: 
        cont += 1       
        for i in l:
            if i == palabraAdivinar:
                numPista = cont - 1
    print("   " + pistas[numPista])  

 
''' 
    Convierte la palabra random a palabra secreta, cambiando
    sus letras por *
'''     


def convertirSecretitos(palabraAdivinar, palabraSecreta): 
    palabraSecreta = (len(palabraAdivinar) * "*")        
    return palabraSecreta


'''
    Pide letra al usuario y la retorna. Comprobamos que no
    introduzca mas de un caracter.
'''


def pedirletra(letra):
    letra = input("    Inserte una letra señol:\n").upper()
    while len(letra) > 1 or letra in listaPalabraSecreto:
        if(len(letra)>1):
            print("No puede introducir mas de una letra")
        else:
            print("La letra "+letra+" ya fue acertada")
        letra = input("    Inserte una letra señol:\n").upper()
    
    return letra


'''
    Comprueba que la letra que el usuario introduce,
    esta en la palabra adivinar. Si es correcta retorna True, y si no False.
'''


def comprobarLetraEnPalabra(listaPalabraAdivinar, letra, listaPalabraSecreto):
    encontrado = False
    for posicion, leter in enumerate(listaPalabraAdivinar):
            if leter == letra:
                listaPalabraSecreto[posicion] = leter 
                encontrado = True
    if encontrado:
        return True
    return False


'''
    Si la letra es incorrecta mostramos el siguiente dibujo,
    y añadimos la letra erronea a la lista de letras falladas.
'''


def quitarVidas(estadoMoneco, listaLetrasFalladas, listaPalabraSecreto, letra, moneco):
    if not comprobarLetraEnPalabra(listaPalabraAdivinar, letra, listaPalabraSecreto):
        estadoMoneco += 1
        print(moneco[estadoMoneco])
        listaLetrasFalladas.append(letra)  
        print("Letras falladas: ", ''.join(listaLetrasFalladas))
        print("\n")
    print("    Palabra:",''.join(listaPalabraSecreto))    
    return estadoMoneco


'''
    Usamos puntuacion y formula como globales para guardar su valor y poder utilizarlas fuera 
    de esta funcion. Comprobamos si el jugador acierta o falla, para aplicar una u otra
    formula.
'''


def comprobarPuntuacion():
    global puntuacionJugador
    global formula
    
    formula = (1 / (len(moneco) - 1)) * len(palabraAdivinar)
    comprobacion = comprobarLetraEnPalabra(listaPalabraAdivinar, letra, listaPalabraSecreto)
    if comprobacion == True:
        puntuacionJugador += formula * 2
    elif comprobacion == False:
        puntuacionJugador -= formula
       
    puntuacionJugador = round(puntuacionJugador, 2)
    


'''
    Controlamos la razon del fin de juego:
     - El jugador acierta la palabra
     - El jugador se queda sin vidas
'''


def finJuego(listaPalabraAdivinar, listaPalabraSecreto, estadoMoneco, moneco):
    global totalAcertadas
    global totalFalladas
    global puntuacionJugador
    print("Puntos:", puntuacionJugador)
    if listaPalabraAdivinar == listaPalabraSecreto:
        print("¡¡¡You Win!!!\n")
        puntuacionJugador =puntuacionJugador+ formula * 10
        totalAcertadas += 1
        return True 
    elif estadoMoneco == len(moneco) - 1:
        print("¡¡¡You Die!!!\n") 
        print("    La palabra era: ", palabraAdivinar) 
        totalFalladas += 1
        return True
    else:
        print("Le quedan ", (len(moneco) - estadoMoneco - 1), " oportunidades\n")
        return False


'''
    INICIO DEL JUEGO
'''
nombreUsu = pedirNombre(nombreUsu)
print("************************")
print("   *Bienvenido", nombreUsu + "*")
print("   *Puntos: ", estadoMoneco, "Vidas:", len(moneco)-1, "*")
print("************************\n")

palabraAdivinar = cargarPalabra(listaCompleta, palabraAdivinar)
listaPalabraAdivinar = list(palabraAdivinar)
palabraSecreta = convertirSecretitos(palabraAdivinar, palabraSecreta)
listaPalabraSecreto = list(palabraSecreta)  

print(moneco[estadoMoneco])
print("\n")
print("     Palabra:", len(palabraAdivinar) * "*")

while  acabose == False and respuesta.__contains__("s"):
    letra = pedirletra(letra)
    estadoMoneco = quitarVidas(estadoMoneco, listaLetrasFalladas, listaPalabraSecreto, letra, moneco)
    comprobarPuntuacion()
    if puntuacionJugador < 0:
            puntuacionJugador = 0
   
    acabose = finJuego(listaPalabraAdivinar, listaPalabraSecreto, estadoMoneco, moneco)
   
    if acabose == True :
        print("******************************************")
        print("Puntos tras acertar la palabra:", round(puntuacionJugador,2),"\n")
        print("TOTAL PALABRAS ACERTADAS:", totalAcertadas, "\n")
        print("TOTAL PALABRAS FALLADAS:", totalFalladas, "\n")
        print("******************************************\n")
        respuesta = input("¿Desea seguir jugando?(s/n)\n")
        totalPuntuacion+=puntuacionJugador
        if(respuesta.__contains__("s")):      
            palabraAdivinar = cargarPalabra(listaCompleta, palabraAdivinar)
            listaPalabraAdivinar = list(palabraAdivinar)
            palabraSecreta = convertirSecretitos(palabraAdivinar, palabraSecreta)
            listaPalabraSecreto = list(palabraSecreta)  
            estadoMoneco = 0
            puntuacionJugador=0
            listaLetrasFalladas = []
            print(moneco[estadoMoneco])
            acabose = False
            print("\n")
            print("     Palabra:", len(palabraAdivinar) * "*")
        else:
            print("PUNTUACION TOTAL DE TODAS LAS PARTIDAS:",round(totalPuntuacion,2),"\n")
            print("***********GRACIAS POR JUGAR**************")
            
   
