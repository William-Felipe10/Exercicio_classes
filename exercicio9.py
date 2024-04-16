'''
9-Crie uma classe Estudante com características como nome, idade e notas. 
Adicione métodos para calcular a média das notas e para mostrar se o estudante foi aprovado ou reprovado.
'''
# DECLARANDO A CLASSE:
class estudante:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,nome,idade,notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def calcular_media (self, *outras_notas):
        total_notas = sum (outras_notas) + self.notas
        quantidade_notas = len (outras_notas) + 1
        return total_notas / quantidade_notas

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def verificar_aprovacao(self, media_minima=6.0):
        media = self.calcular_media()
        if media >= media_minima:
           return f"{self.nome} foi aprovado(a) com media {media:.2f} "
        else:
            return f"{self.nome} foi aprovado (a)com media {media:.2f}" 

# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=="__main__":
    estudante1 = estudante("João", 20, 7.5)
    estudante2 = estudante("Maria", 19 , 5.8)
    media_joao = estudante1.calcular_media (8.0 , 7.0)
    media_maria= estudante2.calcular_media (6.0 , 6.0)

    
    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print(estudante1.verificar_aprovacao())
    print (estudante1.verificar_aprovacao())
    print (estudante1.verificar_aprovacao (media_minima=7.0))
    print (estudante2.verificar_aprovacao (media_minima=7.0))           