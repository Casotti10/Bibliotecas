import time 
data_hoje = time.localtime()

#a funçao strtime() converte o struct para uma string de a cordo com o format especifico
print(time.strftime('%d %B %Y %X', data_hoje)) 