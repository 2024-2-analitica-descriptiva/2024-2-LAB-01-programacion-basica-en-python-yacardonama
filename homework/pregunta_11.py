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

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    doc=limpiar()
    col2=[linea[1] for linea in doc]
    col2_int=[int(numero) for numero in col2]
    col4=[linea[3] for linea in doc]
     
    compacta=list(zip(col4,col2_int))
    expandida=[(letra, numero) for letras, numero in compacta for letra in letras.split(',')]
    diccionario = {letra: [numero for letra_interna, numero in expandida if letra_interna == letra] 
                   for letra, _ in expandida}
    
    suma = {clave: sum(valores) for clave, valores in diccionario.items()}
    organizado=dict(sorted(suma.items()))

    return organizado

if __name__=="__main__":
    
    print(pregunta_11())