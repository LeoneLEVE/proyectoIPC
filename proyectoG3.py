def ROT13toBit(texto_de_entrada):
    rot13_texto = ''
    for char in texto_de_entrada:
        if 'A' <= char <= 'Z':
            rot13_texto += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            rot13_texto += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            rot13_texto += char
    bit_de_salida = ' '.join(format(ord(c), '08b') for c in rot13_texto)
    return bit_de_salida

def BitToROT13(bit_de_entrada):
    chars = bit_de_entrada.split()
    text = ''.join(chr(int(b, 2)) for b in chars)
    texto_original = ''
    for char in text:
        if 'A' <= char <= 'Z':
            texto_original += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            texto_original += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            texto_original += char
    return texto_original

#Entrada desde terminal
mensaje = input("Escribe el mensaje que quieres cifrar y luego recuperar: ")

#Cifrado ROT13 a binario
cifrado = ROT13toBit(mensaje)
print("El mensaje cifrado en bits es:", cifrado)

#Desencriptado desde bits a texto original
descifrado = BitToROT13(cifrado)
print("EL mensaje original recuperado es:", descifrado)

