#!/usr/bin/python3
import time
import os

os.system("clear")
print("""
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
 """)
time.sleep(1.2)
os.system("figlet Reto 7")

def invertir(str):
    rev = list(str)
    rev.reverse()
    return "".join(rev)

cadena = "Buen dia"
cadena1 = "Sayonara"
cadena2 = "Kiitos"
print(cadena + " >> " + invertir(cadena))
print(cadena1 + " >> " + invertir(cadena1))
print(cadena2 + " >> " + invertir(cadena2))

time.sleep(2)

    


