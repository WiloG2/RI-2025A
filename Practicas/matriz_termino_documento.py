import math

def dividir_limpiar(texto):
    texto = texto.lower()
    texto_limpio = ""
    for caracter in texto:
        if caracter.isanum() or caracter == "áéíóúüñ":
            texto_limpio += caracter
        else:
            texto_limpio += " "
    palabras =texto_limpio.split()
    return palabras

def matriz_termino_documento(archivo):
    matriz_termino_documento = {} #Diccionario para almacenar la matriz
    documentoss = [] #Numero total de documentos
    #abrir el archivo y leerlo
    with open(archivo,"r", encoding="utf=8") as file:
        index = 1
        for line in file:
            documentoss.append(index)
            palabras = dividir_limpiar(line)
            
            
        
    