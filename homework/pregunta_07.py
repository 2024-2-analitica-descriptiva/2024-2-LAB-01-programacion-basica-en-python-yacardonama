"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
#from pregunta_01 import limpiar
def limpiar():
    abrir= open("files\\input\\data.csv","r").readlines()
    sin_salto=[linea.replace("\n","") for linea in abrir]
    separado_tab=[string.split("\t") for string in sin_salto]
    return separado_tab

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 2 y una lista con todas las letras
    asociadas (columna 1) a dicho valor de la columna 2.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]

    """
    doc=limpiar()
    letras=[linea[0] for linea in doc]
    numeros=[linea[1] for linea in doc]
    lista_enteros = [int(numero) for numero in numeros]
    completo=[[numero, letra] for numero, letra in zip(lista_enteros,letras)]
    
    diccionario = {numero: [letra for numero_interno, letra in completo if numero_interno == numero] 
                  for numero, _ in completo}
    organizado=sorted(diccionario.items())

    return organizado

if __name__=="__main__":
    
    print(pregunta_07())


