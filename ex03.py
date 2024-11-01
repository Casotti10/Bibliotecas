import locale
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")

#Saber o fuso horario de cada lugar
fuso_horario_sp = ZoneInfo('America/Sao_Paulo')
fuso_horario_tokyo = ZoneInfo("Asia/Tokyo")
fuso_horario_ny = ZoneInfo("America/New_York")

#Saber o horario de cada lugar
tokyo_time = datetime.now(fuso_horario_tokyo)
sp_time = datetime.now(fuso_horario_sp)
ny_time = datetime.now(fuso_horario_ny) 

print("Data e hora em Sao Paulo", sp_time)
print("Data e hora em Nova York", ny_time)
print("Data e hora em Tokyo", tokyo_time) 

def verificar_horario (data_hora): 
    if  9 <= data_hora.hour < 17: 
        return "aberto"
    else:
        return "fechado" 
print(f'Escritorio de Sao Paulo esta {verificar_horario(sp_time)}')
print(f'Escritorio de Tokyo esta {verificar_horario(ny_time)}')
print(f'Escritorio de Nova York esta {verificar_horario(tokyo_time)}')

