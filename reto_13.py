#!/usr/bin/python3
import time
import os
os.system("clear")
print("""
/*
 * Escribe una función que reciba un texto y retorne verdadero o
 * falso (Boolean) según sean o no palíndromos.
 * Un Palíndromo es una palabra o expresión que es igual si se lee
  * de izquierda a derecha que de derecha a izquierda.
 * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
 * Ejemplo: Ana lleva al oso la avellana.
 */
""")


def es_palindromo(cadena):
    cadena = cadena.lower()

    return str(cadena == cadena[::-1])


texto = ["radar", "reconocer", "rotor", "somos", "chamaco", "anilina", "oso", "salas", "toribio", "neuquen", "aviva", "sauzas"]

for i in texto:
    print(i + " es palindromo? >> " +  es_palindromo(i))
    time.sleep(0.8)

