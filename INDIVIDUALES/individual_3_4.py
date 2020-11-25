import random
import math


#Clase madre Cuenta con su constructor
class Cuenta:
    def __init__(self,titular): #solo pide el parametro titular
        self.titular = titular
        self.cantidad = random.randint(100000,1000000) #la cantidad se define mediante un random entre 
        print('\n**Se creo un objeto de Cuenta')       #100.000 y 1.000.000
    # metodo que muestra los datos segun el formato indicado
    def mostrar_datos(self):
        datos = '\n--- Datos de cuenta ---\nTitular : {}\nCantidad: ${:,}\n-----------------------\n'
        return datos.format(self.titular,self.cantidad).replace(',','.')


# clase PlazoFijo hereda de Cuenta, se pasa como argumento para creacion del objeto
class PlazoFijo(Cuenta):
    def __init__(self,titular): #se crea un constructor con el metodo super para heredar 
        super().__init__(titular) #los parametros de construccion y agregar nuevos
        self.plazo = 12 #declara el plazo en 12 para equivalente a un año
        self.interes = 0 #se inicializa el interes en 0
        print('**este objeto PlazoFijo, es hijo de Cuenta') #se agrega para indicar que que al crear 
                                                            #un objeto este se hereda de la clase Cuenta

    # la funcion tiene como parametro el porcentaje del interes
    def importe_interes(self,interes):
        self.interes = interes
        # se realiza el calculo del importe mensual
        self.importe_mensual = self.cantidad * self.interes / 100
        # se agrega un atributo que referencia al importe total para darle una logica al ejercicio
        self.importe_total = self.importe_mensual * self.plazo
        #solo para mostrar que se ingreso un valor de interes como argumento
        print('##Se ingreso un interes de {}% mensual##'.format(self.interes))
        
    # metodo que muestra los datos segun el formato indicado    
    def mostrar_datos(self):
        datos = '\n--- Datos Plazo fijo ---\nTitular              : {}\nPlazo                : {} meses\nTasa interes         : {}% mensual\nCantidad             : ${:,}\nInteres mensual      : ${:,}\nTotal Interes periodo: ${:,}\n-----------------------\n'
        return datos.format(self.titular,self.plazo,self.interes,self.cantidad,round(self.importe_mensual),round(self.importe_total)).replace(',','.')

# Clase que hereda de Cuenta
class CajaAhorro(Cuenta): #se implementa super en su constructor para obtener los parametros de Cuenta
    def __init__(self,titular):
        super().__init__(titular)
        print('**este objeto CajaAorro es hijo de Cuenta') #se agrega para indicar que que al crear 
                                                            #un objeto este se hereda de la clase Cuenta
     # metodo que muestra los datos segun el formato indicado  
    def mostrar_datos(self):
        self.ahorro = self.cantidad
        datos = '\n--- Datos de Caja Ahorro ---\nTitular: {}\nAhorro : ${:,}\n----------------------------\n'
        return datos.format(self.titular,self.ahorro).replace(',','.')
        



#### Se crean instancias de cada una de las clases con el argumento titular
cuenta1 = Cuenta('Juan Perez')
cajaAhorro1 = CajaAhorro('Lalo Landas')
plazoFijo1 = PlazoFijo('Beto A. Saber')



## se llama a los metodos de cada objeto instanciado

print(cuenta1.mostrar_datos())
print(cajaAhorro1.mostrar_datos())
plazoFijo1.importe_interes(4) #al llamar al importe interes se le entrega el 
                              #argumento equivalente al porcentaje del interes mensual
print(plazoFijo1.mostrar_datos())

#se realiza un cambio al interez mensual para cambiar el valor de interes mensual y 
# total de interes del periodo
plazoFijo1.importe_interes(10)
#se llama nuevamente mostrar datos de plazo fijo
print(plazoFijo1.mostrar_datos())


