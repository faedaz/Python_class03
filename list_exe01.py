# Soma de Todos os Itens
# Crie um programa que, a partir de uma lista de números pré-definida, calcule e exiba a soma de todos os seus elementos.

# Exemplo de Lista: [10, 25, 30, 45, 50]

# # Saída Esperada: 160

numbers_list: list = [10, 25, 30, 45, 50]
total: int = 0

for x in numbers_list:
    total = total + x
print(total)