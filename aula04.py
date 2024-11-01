import locale
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
#Definir para o portugues (locale.LC_TIME, "Portuguese_Brazil.1252")
locale.setlocale(locale.LC_TIME, "Portuguese_Brazil.1252")
agora = datetime.now()
data_formatada = agora.strftime('%A, %d de %B de %Y, %H:%M:%S') 
print(data_formatada) 

#exemplo com uso horario
fuso_horario = datetime.now(ZoneInfo('America/Sao_Paulo')) #Definir o fuso horario do pais 
