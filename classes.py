class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0 
         
    def vendeu(self, vendas): 
        self.vendas = vendas 
        
    def bateu_metas(self, meta):
        if self.vendas > meta:
            print(self.nome, 'bateu meta') 
        else:
            print(self.nome, 'nao bateu meta') 
            