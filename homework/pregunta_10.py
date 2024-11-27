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


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    doc=limpiar()
    col1=[linea[0] for linea in doc]
    
    col4=[linea[3] for linea in doc]
    lista_col4= [linea.split(",") for linea in col4]
    ncol4=[len(linea) for linea in lista_col4]

    col5=[linea[4] for linea in doc]
    lista_col5= [linea.split(",") for linea in col5]
    ncol5=[len(linea) for linea in lista_col5]
    
    lista_tuplas=list(zip(col1,ncol4,ncol5))
    return lista_tuplas


if __name__=="__main__":
    
    print(pregunta_10())
