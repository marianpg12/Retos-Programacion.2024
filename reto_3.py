#!/usr/bin/python3
import time
import os
os.system("clear")
print("""
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */        
 """)
time.sleep(1.2)
# Hacemos la funcion fibonacci y pasamos los valores

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(20):
    print(fibonacci(i))

