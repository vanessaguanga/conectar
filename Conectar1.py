#Vanessa Guanga 
Viernes 22 de Diciembre del 2023

Objetivo principal del programa:

El objetivo principal del desarrollo de software del juego del ahorcado fue crear una aplicación interactiva que entretenga a los usuarios. 
Considero que el juego debe proporciona una experiencia divertida y adictiva para sus usuarios.
Además, el desarrollo del juego del ahorcado me brindo la oportunidad de poner en práctica los conocimientos adquiridos del curso. 


Principales Funcionalidades del programa 

1.Selección aleatoria : El código utiliza la función random.choice() para seleccionar una palabra aleatoria de la lista de palabras predefinidas.

2.Generación de una cadena de guiones: El código utiliza la multiplicación de cadenas ("_" * len(secreta)) para generar una cadena de guiones 
que representa las letras ocultas de la palabra seleccionada.

3.Bucle de juego: El código utiliza un bucle while para permitir al jugador adivinar letras hasta que se agoten los intentos o adivinen la palabra.

4.Contador de intentos: El código utiliza una variable intentos para realizar un seguimiento del número de intentos del jugador.


    
          # Definición de la función
def saludar():
    print("¡Hola! Bienvenido al juego del ahorcado.")

# Llamada a la función
saludar()

# Código existente del juego del ahorcado
print("""EDICION PAISES """)
print("""REGLAS DEL JUEGO: Introduce letras para adivinar la palabra oculta .
                  Tienes 6 intentos, Buena Suerte!

                                                                                 """)
import random #Funcion que permite hacer selecciones aleatorias 

palabras = ['Ecuador', 'Peru', 'Mexico', 'Chile', 'Guatemala', 'Colombia'] #Variable que contiene las palabras 

secreta = random.choice(palabras) #Nueva variable creada para almacenar la elecccion aleatoria de la variable palabras
cadena = "_" * len(secreta) #Variale identificar numero de letras que tiene la palabra y lo convertira en guiones 
intentos = 0 # Empieza el contador 


letras_adivinadas = [] 
while intentos < 6: # Inicio de la condicoon 

    letra = input("Ingresa una letra: ") # Variable letra ingresada por el usuario 
    if letra in letras_adivinadas: #Comparacion 1 
        print("Intenta otra letra") 
    elif letra in secreta: #Comparacion 2 palabra corresponde 
        for i in range(len(secreta)): #Se usa un for para la cantidad de letras que tiene la palabra secreta 
            if secreta[i] == letra: # Comprobar si la letra se uso o no 
                cadena = cadena[:i] + letra + cadena[i+1:]
        #cadena pasada sustituidas el espacio + las letras que lleguen una posicion antes de la letra que se sustituye
        #despues de eso se sustituye eso por letra y le sumo la cadena que esta despues por si no es la ultima letra 
        print("La letra corresponde:", cadena)
        if "_" not in cadena:
            print("¡Felicidades!")
            break
    else: # para las vidas o oportunidades   
        intentos += 1
        print("Letra no corresponde, te quedan", 6-intentos, "intentos.")
        letras_adivinadas.append(letra)
        if intentos == 1:
            print("  O") #Imprimir el cuerpo
        elif intentos == 2:
            print("  O")
            print("  |")
        elif intentos == 3:
            print("  O")
            print(" /|")
        elif intentos == 4:
            print("  O")
            print(" /|\\")
        elif intentos == 5:
            print("  O")
            print(" /|\\")
            print(" /")
        elif intentos == 6:
            print("  O")
            print(" /|\\")
            print(" / \\")
            print("Lo siento, no adivinaste la palabra. La palabra era", secreta)
            break
          
    opcion = input("¿Deseas pasar al siguiente nivel? (s/n): ") # Preguntar si desea pasar al siguiente nivel
if opcion.lower() == "s":
    print("¡Pasando al siguiente nivel!")
    # Aquí se puede agregar el código para pasar al siguiente nivel
else:
    print("Gracias por jugar. ¡Hasta luego!")


        
