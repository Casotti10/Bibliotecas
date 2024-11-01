from datetime import datetime 
# Criando um objeto datetime com uma data específica
data = datetime(2003, 9, 22, 12, 30)
print(data) 

data_hoje = datetime(2024, 10, 29, 9)
data_amanha= datetime(2028, 10, 29, 9)
diferenca = data_amanha - data_hoje
print(f'A diferença entre as duas data é de: {diferenca.days} dias ')