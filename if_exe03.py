# Antes de processar os dados de usuários em um sistema de recomendação, você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido. Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.

try:
    age = float(input('Type your age: '))
    email = input('Type your email: ')

    if age >= 18 and age <= 65:
        print('Valid age')
    else:
        print('Age not valid')

    if '@' in email or '.' in email:
        print('Valid email')
    else:
        print('Not valid email')
except TypeError:
    print('Type a valid type!')
except Exception as error:
    print(f'Error: {error}')