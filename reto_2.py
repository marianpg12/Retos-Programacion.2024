#!/usr/bin/python3
import time
import os
os.system("clear")

print("""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
 """)
time.sleep(1.5)

print("""
>> Bien, chequeamos si ambas palabras tienen la misma longitud. Caso contrario >> False
>> Luego chequeamos a traves de una lista o diccionario que cada letra este en ambos casos. Caso contrario >> False
>> Si la frecuencia de todas las letras es la misma en ambas palabras, entonces son anagramas y debes devolver True. De lo contrario, devuelves False.
>> Hago un ordenamiento (sorted) de la lista, poniendolas alfabeticamente. Luego chequeo la longitud. Si esta bien, retorno True, comparando ambas palabras sorted y lista.
""")
time.sleep(2.0)
# Comparamos

def comparar(str1, str2):
    palabra1 = sorted(list(str1))
    palabra2 = sorted(list(str2))
    if len(palabra1) != len(palabra2):
        return False
    
    return palabra1 == palabra2

print(comparar("pasajee", "pasajero"))
print(comparar("amor", "roma"))
print(comparar("miko", "milo"))


