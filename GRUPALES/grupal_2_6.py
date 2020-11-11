import random
import os
import sys
import time

palabras = ['ASCENSOR', 'BELLOTA', 'CAFETERA', 'CHANCHO', 'DELIRIO',
            'ELEFANTE', 'FLAUTA', 'GIGANTESCO', 'HERMOSO', 'INDEPENDENCIA',
            'JEFATURA', 'KILOGRAMO', 'LEJANO', 'LLANURA', 'MATRIMONIO',
            'NORTE', 'ORQUESTA', 'POLICIA', 'QUESADILLA',
            'RETIRO', 'SOLEADO', 'TERMOMETRO', 'UMBRAL', 'VENTANA',
            'WHATSAPP', 'XILOFONO', 'YARDA', 'ZORRO']

# la funcion list convierte la palabra elejida por
# el modulo random en una lista iterable


def obtener_palabra_aleatoria():
    palabra = list(random.choice(palabras))
    return palabra


figura = ['''
                  +---+
                      | 
                      |   
                      |
                     ===
                 VIDAS = 6''', '''
                  +---+
                  O   | 
                      |
                      |
                     ===
                 VIDAS = 5''', '''
                  +---+
                  O   |
                  |   |
                      |
                     ===
                 VIDAS = 4''', '''
                  +---+
                  O   | 
                 /|   | 
                      |
                     ===
                 VIDAS = 3''', '''
                  +---+
                  O   | 
                 /|\  | 
                      |
                     ===
                 VIDAS = 2''', '''
                  +---+
                  O   | 
                 /|\  | 
                 /    |
                     ===
                 VIDAS = 1''', '''
                  +---+
                  O   | 
                 /|\  | 
                 / \  |
                     ===
                 AHORCADO''']

todas_las_letras = []  # lista para almacenar letras dichas
fallos = 0  # contador de fallos
resultado = []  # lista con _ para sustituir por letras adivinadas


def clear():  # funcion para limpiar consola dependiendo del sistema operativo
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


# agrgara _ segunlargo de la palabra escogida
palabra = obtener_palabra_aleatoria()
for a in range(len(palabra)):
    resultado.append('_')


while True:
    clear()
    print('************ JUEGO DEL AHORCADO ***********')
    print('*******************************************')
    print(figura[fallos])
    print()
    print('    ', end='')
    for c in resultado:
        print(c, end='')
    print()
    print()
    if resultado == palabra:
        print('*************** HAS GANADO ***************')
        break
    if fallos >= 6:
        print('La palabra era:', ''.join(palabra))
        print('************** HAS PERDIDO ***************')
        break
    while True:
        letra_sin_formato = input('Ingresa una letra: ')
        letra_usuario = letra_sin_formato.upper()
        if len(letra_usuario) != 1:
            print('Introduce una letra')
        elif letra_usuario in todas_las_letras:
            print('Ya ingreso esa letra')
        elif letra_usuario not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print('Introduce una letra')
        else:
            todas_las_letras.append(letra_usuario)
            break
    for d in range(len(palabra)):
        if palabra[d] == letra_usuario:
            resultado[d] = letra_usuario
    if letra_usuario not in palabra:
        fallos += 1
    print()
    print()
