#!/usr/bin/python3
import time
import os
os.system("clear")
print("""
*
 * Crea un programa que cuente cuantas veces se repite cada palabra
 * y que muestre el recuento final de todas ellas.
 * - Los signos de puntuación no forman parte de la palabra.
 * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
 * - No se pueden utilizar funciones propias del lenguaje que
 *   lo resuelvan automáticamente.
 */
 """)
def contar_palabras(cadena):
    # pasamos todo el texto a minuscula
    cadena = cadena.lower()
    # Spliteamos
    palabras = cadena.split()
    # Creamos Diccionario
    recuento_palabras = {}
    for i in palabras:
    # Eliminar signos de puntuación
        i = i.strip('.,!?;:')

        # Actualizar el recuento de la palabra
        recuento_palabras[i] = recuento_palabras.get(i, 0) + 1

    return recuento_palabras    
# Usamos un extracto del Quijote de la mancha
texto_ejemplo = """
En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lentejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de velludo para las fiestas con sus pantuflos de lo mismo, los días de entre semana se honraba con su vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años, era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia en los autores que deste caso escriben; aunque, por conjeturas verosímiles, se deja entender que se llamaba Quejana. Pero esto importa poco a nuestro cuento; basta que en la narración dél no se salga un punto de la verdad.
"""

recuento = contar_palabras(texto_ejemplo)
for palabra, count in recuento.items():
    print(f"{palabra}: {count}")

