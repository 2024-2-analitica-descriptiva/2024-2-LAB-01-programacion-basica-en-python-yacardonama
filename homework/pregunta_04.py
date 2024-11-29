"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


from collections import Counter

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    abrir= open("./files/input/data.csv","r").readlines() #ruta en colaboración con Maria
    sin_salto=[linea.replace("\n","") for linea in abrir]
    separado_tab=[string.split("\t") for string in sin_salto]
    
    doc=separado_tab
    mes=[linea[2][5:7]for linea in doc]
    lista=list(Counter(mes).items())
    lista=sorted(lista)
    return lista

if __name__=="__main__":
    
    print(pregunta_04())

