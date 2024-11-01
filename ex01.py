#Vamos criar uma classe de clientes da netflix 

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano 
        else:
            print('Plano indisponivel')
     
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano 
        else:
            print('Plano inválido')

    def ver_filme(self, filme, plano_filme):
        if self.plano == plano_filme:
            print(f'Ver fime {filme}')
        elif self.plano == 'premium':
            print(f'Ver fime {filme}') 
        elif self.plano == 'basic' and plano_filme == 'premium':
            print(f'faça upgrade para premium para ver o filme') 
        else:
            print('Plano inválido')


cliente = Cliente('Lucas', 'lucascasotti1@gmail.com', 'basic' ) 
print(cliente.plano)
cliente.ver_filme('Harry Potter', 'premium')

#BOTAO DE UPGRADE
cliente.mudar_plano('premium')
print(cliente.plano) 
cliente.ver_filme('Harry Potter', 'premium')



