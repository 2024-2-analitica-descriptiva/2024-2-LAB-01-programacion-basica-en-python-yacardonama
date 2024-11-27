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

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    doc=limpiar()
    letras=[linea[0] for linea in doc]
    col2=[linea[1] for linea in doc]
    lista_enteros = [int(numero) for numero in col2]
    completo=[[letra, numero] for letra, numero in zip(letras,lista_enteros)]

    diccionario = {letra: [numero for letra_interna, numero in completo if letra_interna == letra] 
                   for letra, _ in completo}
    resumen = [(letra, max(numero), min(numero)) for letra, numero in diccionario.items()]
    organizado=sorted(resumen)
    
    return organizado


if __name__=="__main__":
    
    print(pregunta_05())
