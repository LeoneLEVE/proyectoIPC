import tkinter as tk

#####################################

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

#####################

def mostrarBits(cadenaBits, contenedor, fila, columna):
    anchoCuadro = 30
    altoCuadro = 30
    anchoTotal = len(cadenaBits) * anchoCuadro

    canva = tk.Canvas(contenedor, width=anchoTotal, height=altoCuadro)
    canva.grid(row=fila, column=columna, columnspan=2, pady=10, padx=10)

    for i, bit in enumerate(cadenaBits):
        coordenadaInicial = i * anchoCuadro
        coordenadaFinal = coordenadaInicial + anchoCuadro
        color = "black" if bit == "0" else "white"
        canva.create_rectangle(coordenadaFinal, 0, coordenadaFinal, altoCuadro, fill=color, outline="gray")
    #esto crea un rectangulo con "i" cantidad de cuadros, donde cada cuadro esta formado por las puntos (coordenadaFinal, 0) y (coordeanadaFinal, altoCuadro)

def crearVentanaVisualizacion():
    segundaVentana = tk.Toplevel(menu)
    segundaVentana.title("Proceso de encriptación paso a paso")
    
    botonContinuar = tk.Button(segundaVentana, text="Ver mensaje resultante", command=lambda:[segundaVentana.destroy(), crearVentanaResultado("pepe")])
    botonContinuar.grid(row=1, columnspan=2, pady=10, padx=10)

def crearVentanaResultado(mensajeDesencriptado):
    terceraVentana = tk.Toplevel(menu)
    terceraVentana.title("Mensaje Desencriptado")

    tk.Label(terceraVentana, text="El texto que encriptaste y que ha sido desencriptado es el siguiente: ").grid(row=0,column=0, pady=10, padx=10)
    tk.Label(terceraVentana, text=mensajeDesencriptado).grid(row=0,column=1, padx=10, pady=10)

    botonCerrar = tk.Button(terceraVentana, text="Cerrar/Volver al menú principal", command=terceraVentana.destroy)
    botonCerrar.grid(row=1, columnspan=2, pady=10, padx=10)
    

menu = tk.Tk()
menu.title("Sistema de encriptación - IPC G#3")
menu.grid_rowconfigure(0, weight=1)
menu.grid_columnconfigure(0, weight=1)

tk.Label(menu, text="Sistema de encriptacion avanzado yeah").grid(row=0,columnspan=2, pady=10)
inputMensaje = tk.Entry(menu)
tk.Label(menu, text="Ingresa el mensaje que deseas encriptar y mandar: ").grid(row=1,column=0, padx=10)
inputMensaje.grid(row=1,column=1, padx=10)
boton = tk.Button(menu, text="Encriptar mensaje",command=crearVentanaVisualizacion)
boton.grid(row=2, pady=10, columnspan=2)


menu.mainloop()


