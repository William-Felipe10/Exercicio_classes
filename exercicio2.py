'''
2-Crie uma classe Animal com características como nome, idade e espécie. 
Implemente métodos para fazer o animal emitir um som e para mostrar informações sobre ele.

'''
# DECLARANDO A CLASSE:
class Animal:
    # CRIANDO FUNÇÃO NA CLASSE
    def __init__(self,nome,idade,raca):
        self.nome = nome
        self.idade = idade
        self.raca = raca

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def emitir_som (self):
        raise NotImplementedError("Método não implementado")

    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}")   
        print (f"idade:{self.idade} anos")  
        print (f"Raça:{self.raca}") 

# DECLARANDO UMA SUBCLASSE:
class cachorro (Animal):
    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def emitir_som (self):
        return "Au Au"  
    
# DECLARANDO UMA SUBCLASSE:
class gato (Animal): 
    # FUNÇÃO PARA OS MÉTODOS QUE SERÃO REALIZADO PELA CLASSE
    def emitir_som(self):
        return "Miau"       
    
# DECLARANDO VALORES PARA A FUNÇÃO DA CLASSE
if __name__=="__main__":
    cachorro = cachorro("Bob", 3 ,"Vira lata")
    gato = gato("Whiskers", 2 , "Castanho")

    cachorro.mostrar_informacoes ()
    gato.mostrar_informacoes ()

    # PRINTANDO E CONCECTANDO TODAS AS AÇÕES DOS VALORES
    print("Som:", gato.emitir_som ())
    print("Som:", cachorro.emitir_som())

    