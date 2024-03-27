#!/usr/bin/python3
import time
import os

os.system("clear")
print("""
/*
 * Escribe una función que calcule y retorne el factorial de un número dado
 * de forma recursiva.
 */
 """)
os.system("figlet Recursividad")
time.sleep(1.2)
print("n! = n x (n-1)!")

def recursividad(n):
    if n == 1:
        return n
    else:
        return n * recursividad(n-1)


print(recursividad(8))
print(recursividad(7))
print(recursividad(6))
print(recursividad(5))

