#Paso 4

import random

etapas = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

fin_del_juego = False
lista_de_palabras = ["aardvark", "babuino", "camello"]
palabra_elegida = random.choice(lista_de_palabras)
longitud_palabra = len(palabra_elegida)

#TODO-1: - Crear una variable llamada 'vidas' para llevar el registro de las vidas restantes. 
#Establecer 'vidas' a 6.
vidas = 6

#Código de prueba
print(f'Pssst, la solución es {palabra_elegida}.')

#Crear espacios en blanco
mostrar = []
for _ in range(longitud_palabra):
    mostrar += "_"

while not fin_del_juego:
    adivinanza = input("Adivina una letra: ").lower()

    #Verificar letra adivinada
    for posicion in range(longitud_palabra):
        letra = palabra_elegida[posicion]
       #print(f"Posición actual: {posicion}\n Letra actual: {letra}\n Letra adivinada: {adivinanza}")
        if letra == adivinanza:
            mostrar[posicion] = letra

    #TODO-2: - Si la adivinanza no es una letra en la palabra_elegida,
    #entonces reducir 'vidas' en 1. 
    #Si vidas llega a 0, el juego debe detenerse y debe imprimir "Has perdido."
    if adivinanza not in palabra_elegida:
        vidas -= 1
        if vidas == 0:
            fin_del_juego = True
            print("Has perdido.")

    #Unir todos los elementos de la lista y convertirlos en una cadena.
    print(f"{' '.join(mostrar)}")

    #Verificar si el usuario ha obtenido todas las letras.
    if "_" not in mostrar:
        fin_del_juego = True
        print("Has ganado.")

    #TODO-3: - imprimir el arte ASCII de 'etapas' que corresponde al número actual de 'vidas' que le queda al usuario.
    print(etapas[vidas])
