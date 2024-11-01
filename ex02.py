from datetime import datetime

ultima_compra = datetime(2024, 5, 10)
data_hora_atual = datetime.now() 

diferenca = data_hora_atual - ultima_compra 

if diferenca.days > 30:
    print(diferenca)
    print('Parabens, voce ganhou um desconto')
else: 
    print('Voce nao ganhou desconto')