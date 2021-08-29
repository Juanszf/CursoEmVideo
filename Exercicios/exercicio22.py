name = input('Qual seu nome? ')
lastName = input('Qual seu sobrenome? ')
spaced_fullName = name.strip() +" "+ lastName.strip()
notSpaced_fullName = name.strip() + lastName.strip()

print(f'\n\nSeu nome com todas as letras em maiúsculo é: {spaced_fullName.upper()}')
print(f'Seu nome com todas as letras em minúsculo é: {spaced_fullName.lower()}')
print(f'A quantidade de caracteres em seu nome é: {len(notSpaced_fullName)}')