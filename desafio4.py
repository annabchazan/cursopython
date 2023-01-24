
'''
CALCULO DE IMC

usuário entra com altura em cm e peso em kg

menor que 18,5 - magreza
entre 18,5 e 24,9 normal
entre 25 e 29,9 sobrepeso
entre 30 e 39,9 obesidade
maior que 40 obesidade grave

1- buscar no google a fórmula de imc:

É calculado dividindo o peso (em kg) pela
 altura ao quadrado (em metros).

2- codificar
3- if, else, elif
'''


altura = float(input ("Qual é a sua altura em cm?"))
peso = float(input ("Qual é o seu peso em kg?"))

indice = peso/(altura/100)**2

if indice < 18.5:
    print ("Magreza")

elif indice >= 18.5 and indice < 24.9:
    print ("Normal")

elif indice >= 35 and indice < 29.9:
    print('Sobrepeso')

elif indice >= 30 and indice < 39.9:
    print('obesidade')

else:
    print ("obesidade grave")