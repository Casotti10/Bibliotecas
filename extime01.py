import time
import locale
'''for i in range(5, -1, -1):
    time.sleep(1)
    print(i, end= ' \r')
print('O evento começou')    
'''
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_atual = time.localtime()
data_hoje = time.strftime('%A, %d %B %Y, %H:%M')
print(data_hoje)
