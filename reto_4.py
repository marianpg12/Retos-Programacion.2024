#!/usr/bin/python3
import time
import os

os.system("clear")
print("""
 *
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */        
""")
time.sleep(1.2)
def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Probemos algunos números
print(es_primo(2))   # True
print(es_primo(17))  # True
print(es_primo(15))  # False
print(es_primo(28))


