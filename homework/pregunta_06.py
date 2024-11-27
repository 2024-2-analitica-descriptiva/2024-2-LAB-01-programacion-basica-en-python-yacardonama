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


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    doc=limpiar()
    col5=[linea[4] for linea in doc]
    lista_filas= [linea.split(",") for linea in col5]
    lista_cv=[cv for listita in lista_filas for cv in listita]
    lista_c_v=[cv.split(':') for cv in lista_cv]
    lista_con_enteros = [(clave, int(valor)) for clave, valor in lista_c_v]
    
    diccionario = {letra: [numero for letra_interna, numero in lista_con_enteros if letra_interna == letra] 
                   for letra, _ in lista_con_enteros}
    resumen = [(letra, min(numero), max(numero)) for letra, numero in diccionario.items()]
    organizado=sorted(resumen)
    
    return organizado

if __name__=="__main__":
    
    print(pregunta_06())

