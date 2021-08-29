name = input('Qual seu nome? ')
lastName = input('Qual seu sobrenome? ')
spaced_fullName = name.strip() +" "+ lastName.strip()
notSpaced_fullName = name.strip() + lastName.strip()

print(f'\nSeu nome com todas as letras em maiúsculo é: {spaced_fullName.upper()}')
print(f'Seu nome com todas as letras em minúsculo é: {spaced_fullName.lower()}')
print(f'Seu nome possui {len(notSpaced_fullName)} caracteres sem contar os espaços')
print(f'Seu primeiro nome possui {len(name)} caracteres')