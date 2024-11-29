"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    abrir= open("./files/input/data.csv","r").readlines() #ruta en colaboración con Maria
    sin_salto=[linea.replace("\n","") for linea in abrir]
    separado_tab=[string.split("\t") for string in sin_salto]
    
    doc=separado_tab
    col1=[linea[0] for linea in doc]
    
    col5=[linea[4] for linea in doc]
    lista_col5= [linea.split(",") for linea in col5]
    lista_de_numeros = [[int(elemento.split(':')[1]) for elemento in sublista] for sublista in lista_col5]
    suma_linea=[sum(linea) for linea in lista_de_numeros]

    lista_por_filas=list(zip(col1,suma_linea))
    diccionario = {letra: [numero for letra_interna, numero in lista_por_filas if letra_interna == letra] 
                   for letra, _ in lista_por_filas}
    suma = {clave: sum(valores) for clave, valores in diccionario.items()}
    organizado=dict(sorted(suma.items())) 

    return organizado

if __name__=="__main__":
    
    print(pregunta_12())
