'''
7-Crie uma classe Livro com atributos como título, autor e número de páginas.
 Implemente métodos para mostrar informações sobre o livro e para calcular a quantidade de palavras por página.
'''
# DECLARANDO A CLASSE:
class Livro:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,titulo,autor,numero_pag):
        self.titulo= titulo
        self.autor = autor 
        self.numero_pag = numero_pag 

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def informacoes(self):
        print("livro:", self.titulo)
        print("Autor:", self.autor)
        print("Numero de paginas:", self.numero_pag)

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def calcular_palavras_por_paginas (self , total_palavras):
        return total_palavras/self.numero_pag
        
# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=="__main__":
    Livro = Livro ("Dom quixote", "Miguel  de Cervantes", 280)
    Livro.informacoes()


    total_palavras = 320000
    palavras_por_pagina = Livro.calcular_palavras_por_paginas(total_palavras)

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print ("Palavras por paginas:", palavras_por_pagina)
    
   
   