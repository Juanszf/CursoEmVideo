'''Faça um programa que leia do número 0 ao 9999 e mostre cada número na tela separado:
Unidade:
Dezena:
Centana:
Milhar: '''

num = (input('Digite um número de 0 até 9999\n'))
y=-1
if num.isnumeric():
    if (int(num)>= 0 and int(num) <= 9999):
        for x in num:
            if y == -1:
                print(f'\nUnidade: {num[y]}')
            elif y == -2:
                print(f'Dezena: {num[y]}')
            elif y == -3:
                print(f'Centena: {num[y]}')
            elif y == -4:
                print(f'Milhar: {num[y]}')
            y=y-1
    else:
        print('Você digitou um número inválido')
else:
    print('Você digitou uma texto não numérico')
