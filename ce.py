def transposicion(texto, largo_fila):
    texto = texto.replace(" ", "&")
    
    if len(texto) % largo_fila != 0:
        texto += "Z" * (largo_fila - len(texto) % largo_fila)
    
    filas = [texto[i:i + largo_fila] for i in range(0, len(texto), largo_fila)]
    
    print("Texto organizado en columnas:")
    for fila in filas:
        print(" ".join(fila))
    
    cifrado = ""
    for col in range(largo_fila):
        for fila in filas:
            cifrado += fila[col]
    
    return cifrado

texto = input("Ingrese la frase a cifrar: ")
largo_fila = int(input("Ingrese la longitud de fila: "))
cifrado = transposicion(texto, largo_fila)
print("Texto cifrado:", cifrado)












