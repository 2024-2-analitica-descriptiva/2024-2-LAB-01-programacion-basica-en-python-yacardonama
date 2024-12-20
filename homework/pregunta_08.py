"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_07():

    abrir= open("./files/input/data.csv","r").readlines()
    sin_salto=[linea.replace("\n","") for linea in abrir]
    separado_tab=[string.split("\t") for string in sin_salto]
    doc=separado_tab
    
    letras=[linea[0] for linea in doc]
    numeros=[linea[1] for linea in doc]
    lista_enteros = [int(numero) for numero in numeros]
    completo=[[numero, letra] for numero, letra in zip(lista_enteros,letras)]
    
    diccionario = {numero: [letra for numero_interno, letra in completo if numero_interno == numero] 
                  for numero, _ in completo}
    organizado=sorted(diccionario.items())

    return organizado


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    todas_letras=pregunta_07()
    depurada = [(numero, sorted(list(set(letras)))) for numero, letras in todas_letras]
    return depurada

if __name__=="__main__":
    
    print(pregunta_08())

