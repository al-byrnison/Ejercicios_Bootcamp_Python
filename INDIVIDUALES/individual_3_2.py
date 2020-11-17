import uuid
import random
import time
import os
import sys

#funcion clear para limpiar consola
def clear():
#cada caso del if corresponde a un sistema operativo distinto windows,mac y linux
    if sys.platform.startswith('win'):
        os.system('cls') #corresponde a la funcion de limpiar consola en cmd de windows
    elif sys.platform.startswith('darwin'):
        os.system('clear') #corresponde a la funcion limpiar consola en terminal de mac
    elif sys.platform.startswith('linux'):
        os.system('clear') #corresponde a la funcion limpiar consola en terminal de linux

'''
PARTE 1) Usuarios
Usuarios: cree una clase llamada Usuario. Cree dos atributos llamados nombre y apellido, y luego cree varios otros atributos que normalmente se almacenan en un perfil de usuario. Cree un método llamado describir_usuario() que imprima un resumen de la información del usuario. Cree otro método llamado saludar_usuario() que imprima un saludo personalizado para el usuario.
Cree varias instancias que representen a diferentes usuarios y llame a ambos métodos para cada usuario.
'''


class Usuario:
    #constructor del objeto
    def __init__(self,nombre,apellido,correo,password):
        self.nombre = nombre
        self.apellido = apellido
        self.id = uuid.uuid4()
        self.edad = random.randint(13,99)
        self.correo = correo
        self.password = password
        self.intentos_de_login = 0
    #metodo que pinta la informacion del usuario en consola (exepto el password)
    def describir_usuario(self):
        print('--- Datos del usuario ---\nNombre : {} {}\nId     : {}\nEdad   : {} años\nCorreo : {}\nPassword: #secreto#'.format(self.nombre,self.apellido,self.id,self.edad,self.correo))
    #metodo que da la bienvenoida al usuario por consola
    def saludar_usuario(self):
        print()
        time.sleep(1)
        print('Checkeando datos ...')
        print()
        time.sleep(3)
        print('\n{} {} Bienvenido al sistema\n'.format(self.nombre,self.apellido))
        time.sleep(3)
        clear() #una vez salude al usuario limpiara la consola
    #metodo que incrementa intentos de login en 1 cada vez que es invocado
    def incrementar_inicio_de_sesion(self):
        time.sleep(2)
        self.intentos_de_login += 1
        print('\nUsuario: {} {} intentando iniciar sesion....\n\nIntentos de logeo: {}\n'.format(self.nombre,self.apellido,self.intentos_de_login))
    #metodo que reestablece los intentos de login en 0
    def reset_intentos_de_login(self):
        time.sleep(2)
        print('\nRestableciendo...\n')
        time.sleep(3)
        self.intentos_de_login = 0
        print('Los intentos de login del usuario: {} {} se han restablecido\n\nIntentos de logeo: {}\n'.format(self.nombre,self.apellido,self.intentos_de_login))
        time.sleep(5)
        clear()

    
clear() #se limpia la consola para iniciar programa
#Se crean instancias(objetos) de la clase
usuario1 = Usuario('Alfonso','Madrid','Alfonsots09@gmail.com','iza090211')
usuario2 = Usuario('Lalo','Landas','lalol@yahoo.com','lalo123')
usuario3 = Usuario('Beto','Asaber','betitobellaco@hotmail.com','4815162342')

#Se invoca el metodo describir_usuario y luego saludar _usuario por cada instancia de la clase
usuario1.describir_usuario()
usuario1.saludar_usuario()
usuario2.describir_usuario()
usuario2.saludar_usuario()
usuario3.describir_usuario()
usuario3.saludar_usuario()

'''
PARTE 2) Intentos de Inicio de Sesión
Intentos de inicio de sesión: agregue un atributo llamado intentos_de_login a su clase Usuario ya escrita. Escriba un método llamado incrementar_inicios_de_sesion() que incremente el valor de intentos_de_login en 1.
Escriba otro método llamado reset_intentos_de_login que restablezca el valor de intentos_de_login a 0.
Cree una instancia de la clase Usuario y llame a incrementar_inicios_de_sesion() varias veces. Imprima el valor de intentos_de_login para asegurarse de que se incrementó correctamente y luego llame a reset_intentos_de_login(). Imprima intentos_de_login nuevamente para asegurarse de que se restableció a 0.
'''
#mediante un for se le asigna con random un numero al azar de intentos de logeo por cada usuario
#luego se llama al metodo reset_intentos_de_login que restablece los intentos a 0 e imprime la cantidad actual de intentos. 
for i in range(random.randint(1,5)):
    usuario1.incrementar_inicio_de_sesion()
usuario1.reset_intentos_de_login()
for i in range(random.randint(1,5)):
    usuario2.incrementar_inicio_de_sesion()
usuario2.reset_intentos_de_login()
for i in range(random.randint(1,5)):
    usuario3.incrementar_inicio_de_sesion()
usuario3.reset_intentos_de_login()
