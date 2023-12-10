

print("""BIENVENIDO AL JUEGO DEL AHORCADO EDICION PAISES """)

print("""REGLAS DEL JUEGO: Introduce letras para adivinar la palabra oculta . 
                 Tienes 6 intentos, Buena Suerte!
      
                                                                                 """)#Mensaje de Bienvenida 


import random  #Funcion que permite hacer selecciones aleatorias

palabras = ['Ecuador', 'Peru', 'Mexico', 'Chile', 'Guatemala', 'Colombia'] #Variable que contiene las palabras 

secreta = random.choice(palabras) #Nueva variable creada para almacenar la elecccion aleatoria de la variable palabras
cadena = "_" * len(secreta) #Variale identificar numero de letras que tiene la palabra y lo convertira en guiones 
intentos = 0 # Empieza el contador 


letras_adivinadas = [] 
while intentos < 6: # Inicio de un ciclo 

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