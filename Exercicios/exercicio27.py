#Faça um programa que leia o nome completo de uma pessoa mostrando o primeiro e o útlimo nome separadamente

fullName = input('Digite seu nome completo ')

fullName = fullName.split()
firstName = fullName[0]
lastName = fullName[-1]

print(f'Nome: {firstName}')
print(f'Sobrenome: {lastName}')
