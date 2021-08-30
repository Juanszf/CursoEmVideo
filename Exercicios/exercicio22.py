'''Crie um programa que leia o nome de uma pessoa e mostre:
O nome com todas as letras em maiúsculo
O nome com todas as letras em minúsculo
Quantas letras ao todo sem contar os espaços
Quantas letras tem o primeiro nome'''

name = input('Qual seu nome? ')
lastName = input('Qual seu sobrenome? ')
spaced_fullName = name.strip() +" "+ lastName.strip()
notSpaced_fullName = name.strip() + lastName.strip()

print(f'\nSeu nome com todas as letras em maiúsculo é: {spaced_fullName.upper()}')
print(f'Seu nome com todas as letras em minúsculo é: {spaced_fullName.lower()}')
print(f'Seu nome possui {len(notSpaced_fullName)} caracteres sem contar os espaços')
print(f'Seu primeiro nome possui {len(name)} caracteres')