from datetime import datetime, timedelta

agora = datetime.datetime.now()
hoje = datetime.date.today()
print(f'Ano: {agora.year}')
print(agora.month)
print(agora.day)
print(agora.hour)
print(agora.minute)
print(agora.second)
print(hoje)
 
data_atual = datetime.now() #pegamos a data atual 
print(data_atual)
data_futura = data_atual + timedelta(days = 10) #somamos a data atual +10 dias 
print(f'Data futuro: {data_futura}') 
data_passada = data_atual - timedelta(days=3) #subtraimos a data atual  -3 dias 
print(f'Data passada: {data_passadax}') 
#Isso pode ser feito com horas, minutos, e segundos

