# -*- encoding: utf-8 -*-

def linhas():
    return print('-='*25)

def data():
    from datetime import datetime
    dia = datetime.now()
    datatex = dia.strftime('%d/%m/%Y %Hh%Mmin')
    return print(f'\033[1;32m{datatex}')

from datetime import date
def dataextenso():
    data_atual = date.today()
    data_em_texto = data_atual.strftime('%d/%m/%Y')
    mes_ext = {1 : 'janeiro', 2 : 'fevereiro', 3 : 'março', 4 : 'abril', 5 : 'maio', 6: 'junho', 7: 'julho', 8: 'agosto',
               9: 'setembro', 10: 'outubro', 11: 'novembro', 12: 'dezembro'}
    aniver = data_em_texto
    dia, mes, ano = aniver.split("/")
    print('%s de %s de %s' % (dia, mes_ext[int(mes)], ano))

