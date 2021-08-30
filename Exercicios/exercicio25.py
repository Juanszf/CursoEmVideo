#Crie um programa que leia o nome de uma pessoa e indique se esse nome possui "Silva"

nome = input('Qual o seu nome completo?\n')
capnome = nome.title()

if 'Silva' in capnome:
    print('\nVocê possui Silva em seu nome')
else:
    print('\nVocê não possui Silva em seu nome')