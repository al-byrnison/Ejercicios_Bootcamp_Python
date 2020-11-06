'''
Enunciado:
Escriba un programa en python que posea las siguientes funciones: 1. pregunta_usuario(): Que pregunta el nombre de usuario.
2. preguntar_numero(): Que obtenga un número desde el usuario a través de la consola, y sólo acepte números enteros.
3. calcular_factorial(): Que calcule el factorial del número ingresado por el usuario.
4. almacenar_factorial(): Que almacene los datos de factorial en un diccionario que agrupe los numeros ingresados por el usuario, el factorial calculado y estos datos estén agrupados por usuario.
Estas funciones deberán estar en un módulo .py que debe ser importado por un script principal, que ejecute un loop while infinito para la operación de la aplicación. Este loop podrá ser terminado sólo ingresando ‘salir’. Al momento de terminar, el programa debe imprimir en pantalla el diccionario completo de datos en el diccionario hasta el momento de recibir la instrucción ‘salir’.
'''
import time  # se importa para utilizar funcion de espera
import os
import sys
# os y sys se importan para funcion clear


# funcion clear limpia la consola dependiendo del sistema operativo
def clear():
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


# funcion que recibe el nombre de usuario y retorna nombre
def pregunta_usuario():
    nombre = input('\nIngrese su Nombre: ')
    return nombre


# funcion que solicita un valor entero y retorna numero
def preguntar_numero():
    a = 0
    while a == 0:
        try:  # intentara solicitar un valor entero si tiene exito agregara a sera = 1 y saldra del bucle
            numero = int(input('Ingrese un numero entero: '))
            a = a+1
        except Exception as e:  # en caso contrario volvera a solicitar el valor
            print('El valor ingresado no es valido\n')
            continue
    return numero


# calcula el factorial del numero y retorna el factorial
# el argumento de la funcion sera multiplicacion x numero
def calcular_factorial(*numero):
    for x in numero:  # recorre el valor de numero
        factorial = 1  # inicializa factorial en 1
        for a in range(1, x+1):  # recorre en el rango de 1 al valor de numero dentro del for
            # el valor de factorial sera factorial por el valor de a en el for
            factorial = factorial*a
    return factorial


# funcion creara un diccionario con los parametros ingresados del siguiente modo
# clave:valor, su argumento se debe ingresar (clave=valor)
def almacenar_factorial(**kwargs):
    print('\nDatos ingresados: ')
    for clave, valor in kwargs.items():
        print(clave, valor)
    return kwargs  # retornara el diccionario


# funcion diccionario sera la que invoque
# el programa principal, no recibe argumentos
def diccionario():
    diccionario = {}  # crea un diccionario vacio
    contador = 1  # inicializa un contador
    while True:  # loop infinito
        nombre = pregunta_usuario()  # almacena nombre desde funcion pregunta_usuario
        numero = preguntar_numero()  # almacena numero desde funcion preguntar_numero
        # almacena el factorial con el argumento numero
        factorial = calcular_factorial(numero)
        # almacenado guardara un diccionario por cada vuelta del loop con los datos ingresados
        almacenado = almacenar_factorial(
            nombre=nombre, numero=numero, factorial=factorial)
        # se agrega al diccionario vacio un nuevo dato que contiene el diccionario
        # almacenado en cada vuelta de loop
        diccionario['Usuario '+str(contador)] = almacenado
        contador = contador+1  # agrega +1 al contador para la siguiente iteracion del loop
        # pregunta si continuara con el loop infinito o terminara para mostrar resultados
        salir = input(
            "\nPara terminar escriba 'salir'  o prsione Enter para continuar : ")
        # si el valor ingresado es salir imprimira un salto de linea y saldra del loop
        if salir == 'salir':
            print('\n')
            break
        # usa la funcion sleep para esperar 0.5´ antes de seguir
        time.sleep(0.5)
        clear()  # funcion clear limpiara la consola despues de que pase time.sleep
        # en cada iteracion del loop
    clear()  # una vez termidao el loop infinito limpiara la consola
    # se imprimira uno por uno los valores del diccionario resultante
    print('Diccionario de datos:')
    print('=====================')
    for k, v in diccionario.items():
      # el formato de salida sera: Ususario(valor) = {nombre, numero,factorial}
        print("%s = %s" % (k, v))
    print('=====================')
    print('Programa terminado !\n')
