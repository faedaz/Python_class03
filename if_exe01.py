# Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.



try:    
    q = int(input('Type a quantity value: '))
    p = int(input('Type a price value: '))

    if q > 0 and p > 0:
        print('Valid data')
    else:
        print('Data not valid! must be positive value.')
except ValueError:
    print('Type not valid!')
except Exception as error:
    print(f'Error! {error}')