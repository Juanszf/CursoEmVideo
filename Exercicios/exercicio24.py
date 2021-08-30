#Crie um programa que leia o nome de uma cidade e diga se ela começa com "Santo"

cidade = input('Qual o nome da sua cidade?\n')

if cidade.find('santo',0,5) == 0:
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')
