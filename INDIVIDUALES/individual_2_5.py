import random  # Se importa random para generar aleatorio

# Declaro variables
ordenes_de_sandwitch = []  # lista vacia para los sandwitches
sandwitches_listos = []  # lista vacia para pedidos listos
# lista con los 5 sandwitch de base
sandw = ['Barros Luco', 'Ave mayo', 'Chacarero', 'Churrasco', 'Lomito']
stock = 20  # cantidad total para los sandwitches.
val = 0  # valor para while asignacion de items a lista ordenes_de_sandwitch

# mientras val sea = 0, entra al bucle for en el cual se recorre en rango de
# stock agregando un elemento al azar de la lista sandw a ordenes_de_sandwitch,
# entra al if en caso que la cantidad de barros luco generados aleatoriamente
# sea >= a 3, si esto ocurre se agregara 1 a val y saldra del bucle, si no la
# lista se limpia.
while val == 0:
    for e in range(stock):
        ordenes_de_sandwitch.append(random.choice(sandw))
    if ordenes_de_sandwitch.count('Barros Luco') >= 3:
        val = val+1
    else:
        ordenes_de_sandwitch.clear()
    print(ordenes_de_sandwitch)

# Ciclo while hasta que ordenes_de_sandwitch quede vacia.
while len(ordenes_de_sandwitch) > 0:
    # imprime una lista con los tipos de sandwitch
    print('Lista de Sandwitches:\n')
    for e in range(5):
        # iteracion en el rango de 5 imprimira el numero
        print(e+1, '-', sandw[e])
        # y el valor de sanwitch
    # se lanza un try para comprobar que el valor ingresado por usuario es un entero
    try:
        pedido = int(input('\nIngrese el numero de su Sandwitch: '))
    except Exception as ex:
        print('El valor ingresado no es valido\n')
        continue
    # si el valor ingresado es mayor al rango realizara un continue y volvera al inicio del while
    if pedido > 5:
        print('valor de sandwitch no corresponde\n')
        continue
    # se asignan los valores de sandwitch segun valor ingresado
    if pedido == 1:
        n_pedido = sandw[0]
    elif pedido == 2:
        n_pedido = sandw[1]
    elif pedido == 3:
        n_pedido = sandw[2]
    elif pedido == 4:
        n_pedido = sandw[3]
    elif pedido == 5:
        n_pedido = sandw[4]
    # Si n_pedido existe dentro de ordenes_de_sandwitch realizara lo siguiente:
    if n_pedido in ordenes_de_sandwitch:
        # pregunta la posicion del valor n_pedido dentro de ordenes_de_sandwiches
        indice = ordenes_de_sandwitch.index(n_pedido)
        # agregara el item guardado en indice a la lista sandwitches_listos
        sandwitches_listos.append(ordenes_de_sandwitch[indice])
        # eliminara el item de la lista ordenes_de_sandwitch
        ordenes_de_sandwitch.pop(indice)
    # Si n_pedido no existe en ordenes_de_sandwitch imprimira un mensaje indicando
    # que ya no quedan y mostrara un listado de los sandwitches disponibles
    # volviendo al inicio del while
    else:
        print('\nYa no quedan', n_pedido, ', seleccione otro.\n')
        print('Sandwitches restantes:\n')
        print(ordenes_de_sandwitch, '\n')
        continue
    # en cada iteracion mostrara el listado de los sandwitches listos
    print('\nSandwitches listos:\n')
    print(sandwitches_listos, '\n')

# una vez vacia la lista ordenes_de_sandwitch mostrara
# el siguiente mensaje y terminara la ejecucion
print('Lamentablemente ya no quedan sandwitches :(\n')
exit()
