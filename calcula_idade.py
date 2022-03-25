from datetime import datetime

ano_nasci = int(input('Digite o ano de nascimento: '))
mes_nasci = int(input('Digite o mês de nascimento: '))
dia_nasci = int(input('Digite o dia de nascimento: '))

datanascimento = datetime(ano_nasci, mes_nasci, dia_nasci)
dataatual = datetime.now()
dif = dataatual - datanascimento

diadevida = dif.days
ano_nasci = diadevida // 365
mes_nasci = (diadevida % 365) // 30

print(f"Você tem {ano_nasci} anos, {mes_nasci} meses e {diadevida % 365} dias de vida.")