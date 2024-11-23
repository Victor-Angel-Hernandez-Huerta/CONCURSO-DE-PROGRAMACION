def generar(desplazamiento):
    
    alfabeto = 'ABCDEFGHIJKLMNÑOPQRSTUVWXWZ'
    cifrado ={}
    decifrado= {}
    
    for i , letras in enumerate(alfabeto):
        letras_cifrada = alfabeto[(i+desplazamiento)%26]
        cifrado[letras]=letras_cifrada
        decifrado[letras_cifrada]=letras
        
    return cifrado, decifrado
def cifrar_texto(texto, diccionario_cifrado):
    texto_cifrado=""
    for letra in texto.upper():
        if letra in diccionario_cifrado:
            texto_cifrado+=diccionario_cifrado[letra]
        else:
            texto_cifrado+=letra
    return texto_cifrado
def descifrar_texto(texto_cifrado,cifrado)
    