'''
Created on 8/6/2015

@author: Javieres
'''
from scipy.sparse.dia import dia_matrix
print 'escribe tu DNI:'

raw_input()

class Ejemplo:
    def publico(self):
        print "publico"
        
    def __privado(self):
        print 'Privado'

ej = Ejemplo()
ej.publico()
# ej.__privado()
ej._Ejemplo__privado

class Fecha():
    def __init__(self):
        self.__dia = 1  
    
    def getDia(self):
        return self.__dia
    
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
           
        else:
            print 'Error'
                 
mi_fecha = Fecha()

print 'Valor inicial del dia: ' + str(mi_fecha.getDia())

mi_fecha.setDia(3)

print 'Valor modificado del dia: ' + str(mi_fecha.getDia())