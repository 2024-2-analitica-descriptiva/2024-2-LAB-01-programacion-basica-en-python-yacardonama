"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

path="./files/input/data.csv"
with open(path,"r") as file:
     datos = file.readlines()

datos=[linea.replace("\n","") for linea in datos]
datos=[linea.split("\t") for linea in datos]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    suma=0
    for linea in datos:
        suma += int(linea[1])
    
    return suma

if __name__=="__main__":
    
    print(pregunta_01())