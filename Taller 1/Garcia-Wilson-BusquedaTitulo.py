query = "Ecuador"
resultados = []

try: 
    with open('01_corpus_turismo_500.txt', 'r') as file:
        line = file.readline()
        index = 0
        while line:
            index += 1
            if not line:
                continue #Skipea la linea vacia
            search = line.split()
            if query in search:
                resultados.append((index))
            line = file.readline()
except FileNotFoundError:
    print("El archivo no se encontró.")

# Print the results
NumeroResultados = len(resultados)
print(f"Número de Documentos encontrados: {NumeroResultados}")
print(f"Resultados de la búsqueda para '{query}':")
print(resultados)
