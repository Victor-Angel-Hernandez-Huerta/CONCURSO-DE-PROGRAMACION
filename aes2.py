
def map_to_custom_value(char):
    # Mapa para convertir caracteres a valores específicos
    mapping = {
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    return mapping.get(char.lower(), char)  # Devuelve el valor del mapa o el carácter original

def transposicion_vertical(texto, num_filas=4):
    texto = texto.replace(" ", "&")
    
    # Calcular el número de columnas necesarias
    num_columnas = -(-len(texto) // num_filas)  # División entera redondeada hacia arriba
    
    # Rellenar con 'Z' para completar la matriz si es necesario
    texto += "Z" * (num_filas * num_columnas - len(texto))
    
    # Construir la matriz de forma vertical (columna por columna)
    matriz = [[""] * num_columnas for _ in range(num_filas)]
    index = 0
    for fila in range(num_filas):
        for col in range(num_columnas):
            matriz[fila][col] = texto[index]
            index += 1
    
    print("Texto organizado en filas:")
    for fila in matriz:
        print(" ".join(fila))
    
    # Leer columna por columna para formar el texto cifrado
    cifrado = ""
    for col in range(num_columnas):
        for fila in matriz:
            cifrado += fila[col]
    
    return cifrado

def mix_columns(state, num_filas=4):
    # Mezcla las columnas dejando caracteres que no sean a-f sin cambios
    num_columnas = len(state) // num_filas
    resultado = []
    for i in range(num_columnas):
        col_sum = 0
        keep_chars = []
        for j in range(num_filas):
            char = state[j * num_columnas + i]
            value = map_to_custom_value(char)
            if isinstance(value, int):  # Solo sumar si es un número
                col_sum += value
            else:
                keep_chars.append(char)
        
        # Usar el resultado reducido al rango hexadecimal (si hay valores a-f)
        if col_sum > 0:
            resultado.append(str(col_sum % 16))
        # Si no, añadir los caracteres que no se convierten
        resultado.extend(keep_chars)
    return ''.join(resultado)

def add_round_key(state, key):
    # XOR con clave, aplicando el mapeo personalizado
    resultado = []
    for c, k in zip(state, key * (len(state) // len(key))):
        c_val = map_to_custom_value(c)
        k_val = map_to_custom_value(k)
        if isinstance(c_val, int) and isinstance(k_val, int):  # XOR solo si ambos son números
            xor_value = (c_val ^ k_val) % 16
            resultado.append(hex(xor_value)[2:])  # Convertir a hexadecimal
        else:
            resultado.append(c)  # Dejar el carácter sin cambios
    return ''.join(resultado)

def aes_simulado(texto, key):
    num_filas = 4  # Fijar el número de filas a 4
    
    # Ronda 1: Transposición vertical
    texto = transposicion_vertical(texto, num_filas)
    print("Después de transposición vertical:", texto)
    
    # Ronda 2: Mezcla de columnas
    texto = mix_columns(texto, num_filas)
    print("Después de mezcla de columnas:", texto)
    
    # Ronda 3: Agregar clave
    texto = add_round_key(texto, key)
    print("Después de agregar clave:", texto)
    
    return texto

# Ejemplo de uso
texto = input("Ingrese la frase a cifrar: ")
key = input("Ingrese la clave (texto): ")
cifrado = aes_simulado(texto, key)
print("Texto cifrado final:", cifrado)








