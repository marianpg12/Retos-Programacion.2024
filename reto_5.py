#!/usr/bin/python3
import time
import os
os.system("clear")

print("""
#5 ÁREA DE UN POLÍGONO
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */        
""")
time.sleep(1.2)
print("""
triangulo >> base x altura / 2
rectangulo >> base x altura
cuadrado >> lado x lado
""")

# creo una funcion poligono (pasandole el string si es cuadrado, rectangulo o triangulo y las dimensiones)
# en base a eso hago el respectivo calculo:
# >> triangulo = base x altura / 2
# >> rectangulo = base x altura 
# >> cuadrado = lado x lado
# luego devuelvo con un return el dato final

def poligono(s, *dimensiones):
    if s == "triangulo":
        base, altura = dimensiones
        area = (base * altura) / 2
    elif s == "rectangulo":
        base, altura = dimensiones
        area = base * altura
    elif s == "cuadrado":
        lado, = dimensiones
        area = lado * lado
    else:
        return "Poligono incorrecto"

    return area

print("Área del triángulo:", poligono("triangulo", 5, 3))
print("Área del rectángulo:", poligono("rectangulo", 4, 6))
print("Área del cuadrado:", poligono("cuadrado", 5))

