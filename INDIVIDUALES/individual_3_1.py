'''
PARTE 1) Restaurante:
Haga una clase llamada Restaurante. El método __init __() para Restaurante debe almacenar dos atributos: un restaurant_nombre y un cocina_tipo. Cree un método llamado describe_restaurant() que imprima estas dos piezas de información, y un método llamado abrir_restaurant() que imprima un mensaje indicando que el restaurante está abierto.
Cree una instancia llamada restaurante de la clase. Imprima los dos atributos individualmente y luego llame a ambos métodos.
'''
import time  # se importa para usar por un asunto estetico solamente


# se crea la clase
class Restaurante:
    def __init__(self, nombre, tipo):  # inicializamos su constructor con parametros que usaremos
        self.restaurant_nombre = nombre
        self.cocina_tipo = tipo
        # de la tercera parte
        self.numero_servicio = 0

    def describe_restaurant(self):  # funcion que imprime la descripcion del objeto
        return 'Restaurante {} y su especialidad {}.'.format(self.restaurant_nombre, self.cocina_tipo)
        # retorna en el formato especificado ejemplo: Restaurante(nombre) y su especialidad(tipo)

    # funcion para imprimir estado del restaurante
    def abrir_restaurante(self, estado):
        self.estado = estado  # se moodifica la sentencia para dar el estado de
        if(self.estado == True):  # abierto o cerrado a traves de un bool
            return 'El restaurant se encuentra abierto!!'
        else:
            return 'El restaurante esta cerrado'

    # de la tercera parte
    # setea el numero de clientes atendidos al indicado por el parametro numero
    def set_numero_servicio(self, numero):
        # toma numero de servicio y lo modifica por el valor de numero
        self.numero_servicio = numero
        # retorna en el formato indicado restaurante(nombre) atendiendo a (numero) clientes
        return 'Restaurante {}, atendiendo a {} clientes'.format(self.restaurant_nombre, self.numero_servicio)
    # funcion incrementa el numero clientes atendidos desde 0 a la cantidad indicada por parametro

    def incrementar_numero_servicio(self, incremento):
        self.incremento = incremento
        # mediante un for imprime el mensaje por cada iteracion se agrega un +1 para que se
        # refleje la misma cantidad que la indicada por parametro
        for i in range(incremento+1):
            print('{} atendiendo a {} clientes'.format(
                self.restaurant_nombre, i))
            # en cada iteracion descansara 0.5 segundos antes de iniciar la proxima
            time.sleep(0.5)
        # una vez completadas todas la iteraciones dara un salto de linea y retornara el mensaje
        print()
        return 'Clientes atendidos en su totalidad !!'


a = '###########################################'
# Instancia restaurant parte 1
print()
restaurante = Restaurante('restaurante', 'comida')
print(restaurante.restaurant_nombre)
print(restaurante.cocina_tipo)
print(restaurante.describe_restaurant())
# en primera instanca el restaurante estara cerrado ya que se le indico un
# argumento 0 que equivale a un bool False
print(restaurante.abrir_restaurante(0))
time.sleep(2)
print('......')
time.sleep(2)
# se hace un salto de linea y una espera para cambiar el valor de cerrado a abierto por medio de un bool como argumento en este caso 1 que vale True
print(restaurante.abrir_restaurante(1))
print()
print(a)
time.sleep(2)

###################################################
'''
PARTE 2) Tres restaurantes:
Comience con su clase de la Parte 1. Cree tres instancias diferentes de la clase y llame a describe_restaurant() para cada instancia.
'''
# Instancias
macmurder = Restaurante('McDonalds', 'Comida rapida')
piccola = Restaurante('La Piccola Italia', 'despidos')
arriero = Restaurante('El Arriero', 'Parrilladas')

print(macmurder.describe_restaurant())
print()
print(piccola.describe_restaurant())
print()
print(arriero.describe_restaurant())
print()
print(a)
time.sleep(2)
####################################################
'''
PARTE 3) Número servicio:
Comience con su programa de la clase Restaurante. Agregue un atributo llamado numero_servicio con un valor predeterminado de 0. Cree una instancia llamada restaurante de esta clase. Imprima el número de clientes que ha atendido el restaurante y luego cambie este valor e imprímalo nuevamente.
'''
print()
print(restaurante.restaurant_nombre, 'atendio a',
      restaurante.numero_servicio, 'clientes')
print()
print('___se cambian valores___')
time.sleep(0.5)
# setea el atributo numero_servicio a un valor nuevo '6' en este caso
setattr(restaurante, 'numero_servicio', 6)
print(restaurante.restaurant_nombre, 'atendio a',
      restaurante.numero_servicio, 'clientes')
print()
print(a)
time.sleep(2)
'''
Agregue un método llamado set_numero_servicio() que le permita establecer el número de clientes que han sido atendidos. Llame a este método con un nuevo número e imprima el valor nuevamente.
'''
# se llama a la funcion set_numero_servicio y se le entrega el
# argumento para indicar la cantidad de clientes atendidos.
print()
print(restaurante.set_numero_servicio(0))
time.sleep(0.5)
print(restaurante.set_numero_servicio(5))
time.sleep(0.5)
print(restaurante.set_numero_servicio(16))
print()
print(a)
time.sleep(2)
'''
Agregue un método llamado incrementar_numero_servicio() que le permite incrementar la cantidad de clientes que han recibido servicios. Llame a este método con el número que desee y que pueda representar cuántos clientes se atendieron, digamos, en un día de trabajo.
'''
print()
# se llama a la funcion incrementar_numero_servicio y
# se le da un argumento de 10 que refleja a los clientes atendidos.
print(restaurante.incrementar_numero_servicio(10))
print()
