def ROT13toBit(input_texto):
    # Aplicamos cifrado ROT13
    rot13_texto = ''
    for char in input_texto:
        if 'A' <= char <= 'Z':
            rot13_texto += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            rot13_texto += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            rot13_texto += char

    # Convertir a cadenas de bits
    bit_output = ' '.join(format(ord(c), '08b') for c in rot13_texto)
    return bit_output

#Cadena de texto desde la terminal
mensaje = input("Escribe el mensaje que quieres cifrar: ")
cifrado = ROT13toBit(mensaje)
print("Mensaje cifrado en bits:", cifrado)
