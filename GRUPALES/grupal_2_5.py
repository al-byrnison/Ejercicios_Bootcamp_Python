import random
import time
import os
import sys

def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')

def gato():
    tablero = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    fin_juego = False
    matriz_ganadora = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def dibuja_tablero(tab):
        '''
        Función: dibuja el tablero de juego con los elementos actualizados
        Parámetros:
        *tab: recibe el tablero en juego
        '''
        
        print('       |       |       ')
        print(f'   {tab[0]}   |   {tab[1]}   |   {tab[2]}   ')
        print('       |       |       ')
        print('-------+-------+-------')
        print('       |       |       ')
        print(f'   {tab[3]}   |   {tab[4]}   |   {tab[5]}   ')
        print('       |       |       ')
        print('-------+-------+-------')
        print('       |       |       ')
        print(f'   {tab[6]}   |   {tab[7]}   |   {tab[8]}   ')
        print('       |       |       ')    
        


    def juega_usuario():
        '''
        Función: jugada del usuario ingresada por teclado
        Variables:
        * jugada_us: almacena la jugada del usuario y resta 1 para elegir posición del array
        '''
        jugada_us=int(input())-1
        
        if tablero[jugada_us] == "X" or tablero[jugada_us] == "O":
            print("\nAlguien ya jugó esa opción, intenta de nuevo\n")
            juega_usuario()
        else:

             tablero[jugada_us] = "X"
                    
                
    def juega_pc():
        '''
        Función: jugada del PC elegida de manera random de espacios disponibles
        Variables:
        * posiciones_libres: array que tendrá las casillas libres
        * jugada_pc: jugada elegida random del PC
        *n: juega_pc-1 para elegir la posición en el array
        Return: jugada_pc
        '''
        posiciones_libres=[]
        for t in tablero:
            if t=='X' or t=='O':
                continue
            else:
                posiciones_libres.append(t)
            
        jugada_pc=random.choice(posiciones_libres)
        n = jugada_pc-1
        if tablero[n] == "X" or tablero[n] == "O":
            print("\nAlguien ya jugó esa opción, intenta de nuevo\n")
            juega_pc()
        else:
            tablero[n] = "O"
            
    def revisa_tablero():
        '''
        Función: revisa tablero si existe un ganador y quien, o si hay un empate.
        casillas: casillas ocupadas
        '''
        casillas = 0
        #REVISA SI HAY GANADORS
        for a in matriz_ganadora:
            if tablero[a[0]] == tablero[a[1]] == tablero[a[2]] == "X":
                print("\nGANASTE!!!!!!!!\n")
                return True

            if tablero[a[0]] == tablero[a[1]] == tablero[a[2]] == "O":
                print("\nPERDISTE CONTRA MI HUMANO, MUAJAJA\n")
                return True
        #REVISA SI HAY EMPATE    
        for a in range(9):
            if tablero[a] == "X" or tablero[a] == "O":
                casillas += 1
            if casillas == 9:
                print("\nEMPATE :V \n")
                return True

            
    while not fin_juego:
        #Dibuja el tablero de juego actualizado
        dibuja_tablero(tablero)
        #Revisa si ya hay un ganador o ha ocurrido un empate
        fin_juego = revisa_tablero()
        #si la revisión dio como resultado un ganador o empate, sale de while
        if fin_juego == True:
            break
           
        print("\nELIGE TU JUGADA :) \n")
        juega_usuario()
        clear()
        dibuja_tablero(tablero)
        fin_juego = revisa_tablero()
        if fin_juego == True:
            break
        print("\n...PC JUGANDO: :V\n")
        time.sleep(3)
        juega_pc()
        clear()

    fin = input("\n¿QUIERES VOLVER A JUGAR?(S/N): ")
    if  fin == "S" or fin =='s':
        clear()
        gato()

clear()
gato()