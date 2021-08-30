'''Faça um programa que leia uma frase e mostre:
Quantas vezes aparece a letra "a"
Qual a primeira posição que o "a" aparece
Qual a última posição que o "a" aparece'''

frase = input('Digite uma frase').strip()
fraseLow = frase.lower()

print(f'Sua frase possui {fraseLow.count("a")} "a"')
print(f'A posição em que o primeiro "a" aparece é: {fraseLow.find("a")}')
print(f'A posição em que o último "a" aparece é: {fraseLow.rfind("a")}')


