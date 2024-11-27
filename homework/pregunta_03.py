"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    abrir= open(r"..\files\input\data.csv","r").readlines()
    sin_salto=[linea.replace("\n","") for linea in abrir]
    separado_tab=[string.split("\t") for string in sin_salto]
    doc=separado_tab
    col1=[linea[0] for linea in doc]
    col2=[linea[1] for linea in doc]
    lista_enteros = [int(numero) for numero in col2]
    completo=[[letra, numero] for letra, numero in zip(col1,lista_enteros)]

    diccionario = {letra: [numero for letra_interna, numero in completo if letra_interna == letra] 
                   for letra, _ in completo}
    suma_dict={key:sum(numeros) for key, numeros in diccionario.items()}
    
    organizado=sorted(suma_dict.items())

    return organizado

if __name__=="__main__":
    
    print(pregunta_03())
