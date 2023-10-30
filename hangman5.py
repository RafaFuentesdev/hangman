# Paso 5

import random

# TODO-1: - Actualizar la lista de palabras para usar 'lista_de_palabras' de hangman_words.py
# Eliminar esta línea: lista_de_palabras = ["ardvark", "baboon", "camel"]
from hangman_words import lista_de_palabras

palabra_elegida = random.choice(lista_de_palabras)
longitud_palabra = len(palabra_elegida)

fin_del_juego = False
vidas = 6

# TODO-3: - Importar el logo de hangman_art.py y mostrarlo al comienzo del juego.
from hangman_art import logo

print(logo)

# Código de prueba
print(f"Pssst, la solución es {palabra_elegida}.")

# Crear espacios en blanco
mostrar = []
for _ in range(longitud_palabra):
    mostrar += "_"

while not fin_del_juego:
    adivinanza = input("Adivina una letra: ").lower()

    # TODO-4: - Si el usuario ha ingresado una letra que ya adivinó, mostrar la letra y hacerle saber.
    if adivinanza in mostrar:
        print(f"Ya adivinaste {adivinanza}")

    # Verificar letra adivinada
    for posicion in range(longitud_palabra):
        letra = palabra_elegida[posicion]
        # print(f"Posición actual: {posicion}\n Letra actual: {letra}\n Letra adivinada: {adivinanza}")
        if letra == adivinanza:
            mostrar[posicion] = letra

    # Verificar si la adivinanza del usuario es incorrecta.
    if adivinanza not in palabra_elegida:
        # TODO-5: - Si la letra no está en la palabra_elegida, mostrar la letra y hacerle saber que no está en la palabra.
        vidas -= 1
        print(
            f"Adivinaste {adivinanza}, esa letra no está en la palabra. Te quedan {vidas} vidas."
        )
        if vidas == 0:
            fin_del_juego = True
            print("Has perdido.")

    # Unir todos los elementos de la lista y convertirlos en una cadena.
    print(f"{' '.join(mostrar)}")

    # Verificar si el usuario ha obtenido todas las letras.
    if "_" not in mostrar:
        fin_del_juego = True
        print("Has ganado.")

    # TODO-2: - Importar las etapas de hangman_art.py y hacer que este error desaparezca.
    from hangman_art import etapas

    print(etapas[vidas])
