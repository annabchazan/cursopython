
'''
DESAFIO COM SETs

Criar um programa que gera 3 listas de acordo com a necessidade
logo abaixo:

lista1 = funcionários que têm carro e trabalham a noite
lista2 = funcionários que têm carro e trabalham durante o dia
lista3 = funcionários que não têm carro 
'''

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sofia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sofia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

palavras1 = set(funcionarios)
palavras2 = set (turno_dia)

lista1= set(tem_carro) & set(turno_noite)
print (lista1)

lista2= set(tem_carro) & set(turno_dia)
print (lista2)

lista3 = set(funcionarios) - set(tem_carro)
print (lista3)