from Abstract.Abstract  import Expression
import math

class T(Expression):

    def __init__(self, left, right, tipo, fila, columna):
        self.left = left
        self.right = right
        self.tipo = tipo
        super().__init__(fila, columna)

    def operar(self, arbol):
        leftValue = ''
        rightValue = ''
        print(self.tipo.operar(arbol))
        if self.left != None:
            leftValue = self.left.operar(arbol)


        if self.tipo.operar(arbol) == 'seno':
            radianes = math.radians(leftValue)
            return (math.sin(radianes))
        elif self.tipo.operar(arbol) == 'coseno':
            radianes = math.radians(leftValue)            
            return (math.cos(radianes)) 
        elif self.tipo.operar(arbol) == 'tangente':
            radianes = math.radians(leftValue)            
            return (math.tan(radianes) )
        elif self.tipo.operar(arbol) == 'inverso':
            return 1 / leftValue   
        else:
            return None

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()

