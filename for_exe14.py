# Exercício 11: Índice e Valor
# Objetivo: Imprimir cada item de uma lista juntamente com seu índice correspondente.
# Dados Iniciais: frutas = ["Maçã", "Banana", "Cereja"]
# Tarefa: Use a função enumerate() em um laço for para obter o índice e o valor. Imprima no formato: "Índice 0: Maçã".

fruits = ['Apple', 'Banana', 'Cherry']

for x, y in enumerate(fruits):
    print(f'Indice {x}: {y}')