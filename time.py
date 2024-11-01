import time #Importando biblioteca
data_fixa = time.time_ns() #aplicando a funçao na variavel


inicio = time.time() #Esse valor serve como a marca inicial para medir quanto tempo o loop vai levar para ser executado.
for i in range (100_000_000): #loop em 100milhoes para fazer controle de desempenho 
    pass #Como o loop precisa ser válido, o pass é usado para preencher o bloco

fim = time.time()#Captura o tempo atual novamente, agora no final da execução do loop.
#print(fim - inicio) #Calcula a diferença entre o tempo final (fim) e o tempo inicial (inicio), mostrando quanto tempo (em segundos) o loop levou para ser executado.

data_fixa = time.time()
tempo_hoje = time.ctime(data_fixa) #Passando o tempo em segundos para a data atual
#print(tempo_local)

data_fixa = time.time()
tempo_hoje = time.localtime(data_fixa) #Passando a data atual separada em dia/mes/ano
#print(tempo_hoje.tm_year) #mostrando separado so o ano
#print(tempo_hoje.tm_hour) #mostrando separado so a hora 
#print(tempo_hoje.tm_mday) #mostrando separado so o dia 