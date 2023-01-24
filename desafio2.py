'''
DESAFIO COM FUNCÕES - Calculadora para pintura

Criar um programa que calcula a quantidade de tinta
necessária para pintar uma parede. O usuário deverá fornecer
as seguintes informações: rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'você necessita
de x latas de tinta'

'''

def area (x,y):
    area_parede = (x*y)
    return area_parede

rendimento = int(input("Qual é o rendimentoda lata?"))
altura = float(input("Qual é a altura da parede?"))
largura = float(input("Qual é a largura da parede?"))

area_real = area (altura, largura)
quantidade_lata = (area_real/rendimento)
print (f' você precisará de {quantidade_lata} latas de tinta')