"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    abrir= open(r"..\files\input\data.csv","r").readlines()
    sin_salto=[linea.replace("\n","") for linea in abrir]
    separado_tab=[string.split("\t") for string in sin_salto]
    doc=separado_tab
    col5=[linea[4] for linea in doc]
    lista_filas= [linea.split(",") for linea in col5]
    lista_cv=[cv for listita in lista_filas for cv in listita]
    lista_c_v=[cv.split(':') for cv in lista_cv]
    lista_con_enteros = [(clave, int(valor)) for clave, valor in lista_c_v]
    
    diccionario = {letra: [numero for letra_interna, numero in lista_con_enteros if letra_interna == letra] 
                   for letra, _ in lista_con_enteros}
    valores_por_clave= {letra: len(numeros) for letra, numeros in diccionario.items()}
    organizado=dict(sorted(valores_por_clave.items()))
    
    return organizado

if __name__=="__main__":
    
    print(pregunta_09())
