from datetime import datetime 

data_nascimento = input('Digite sua data de nascimento (dd/mm/aaaa):')
idade_hoje = datetime.strptime(data_nascimento, '%d/%m/%Y')
data_atual = datetime.now()
print(data_nascimento)


idade = data_atual.year - idade_hoje.year
print(idade)


