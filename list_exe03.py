# Escreva um programa que receba uma lista de números inteiros e crie uma nova lista contendo apenas os números pares da lista original.

# Exemplo de Lista: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Saída Esperada: [2, 4, 6, 8, 10]

full_list: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list: list = []
odd_list: list = []

for x in full_list:
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)
print(f"Even numbers: {even_list} \n Odd numbers: {odd_list}")