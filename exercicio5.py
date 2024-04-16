'''
5-Crie  uma classe Triângulo com atributos para os lados do triângulo. 
Adicione métodos para calcular a área e o perímetro do triângulo.
'''
import math  

# DECLARANDO A CLASSE:
class triangulo:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,lado1,lado2,lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def calcular_perimetro (self):
        return self.lado1 + self.lado2 + self.lado3
    
    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def calcular_area (self):

        s= self.calcular_perimetro()/2
        area = math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))
        return area 

# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=="__main__":
    triangulo = triangulo(2, 3, 4)

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print ("Perímetro:", triangulo.calcular_perimetro())
    print ("triangulo:",  triangulo.calcular_area())
   