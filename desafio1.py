'''
desafio com if, elif, else

criar um programa que dependendo da temperatura da carne
ele retorna o ponto de cozimento em portugues. O usuário
deverá fornecer a temperatura.

°C - cozimento
antes - cozinhar por mais alguns minutos
48 - Selada
54 - Ao ponto para mal
60 - Ao ponto
65 - Ao ponto para bem
71 - Bem passada
dps- bem passada
'''

temperatura = int (input ("Qual é a temperatura da carne? "))

if temperatura < 48:
    print ("Cozinhe a sua carne por mais alguns minutos")

elif temperatura in range (48,53):
    print ("Sua carne está: selada")

elif temperatura >= 54 and temperatura <60:
     print ("Sua carne está: ao ponto para mal")

elif temperatura >=60 and temperatura <65:
    print ("Sua carne está: ao ponto para bem")

else: 
    print ("Bem passada")
