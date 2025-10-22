def ROT13toBit(input_text):
    rot13_texto = ''
    for char in input_text:
        if 'A' <= char <= 'Z':
            rot13_texto += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            rot13_texto += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            rot13_texto += char
    bit_output = ' '.join(format(ord(c), '08b') for c in rot13_texto)
    return bit_output

def BitToROT13(bit_input):
    chars = bit_input.split()
    text = ''.join(chr(int(b, 2)) for b in chars)
    original_text = ''
    for char in text:
        if 'A' <= char <= 'Z':
            original_text += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            original_text += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            original_text += char
    return original_text

#Entrada desde terminal
mensaje = input("Escribe el mensaje que quieres cifrar y luego recuperar: ")

#Cifrado ROT13 a binario
cifrado = ROT13toBit(mensaje)
print("El mensaje cifrado en bits es:", cifrado)

#Desencriptado desde bits a texto original
descifrado = BitToROT13(cifrado)
print("EL mensaje original recuperado es:", descifrado)

