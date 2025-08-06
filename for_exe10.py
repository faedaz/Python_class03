# Exercício 7: Encontrando o Maior Número
# Objetivo: Dada uma lista de números, encontrar o maior valor sem usar a função max().
# Dados Iniciais: numeros = [1, 45, 23, 89, 2, 101, 5]
# Tarefa: Inicie uma variável maior_numero com o primeiro item da lista. Percorra o restante da lista e, se encontrar um número maior, atualize maior_numero.

numbers = [1, 45, 23, 89, 2, 101, 5]

max_value = 0

for x in numbers:
    if x > max_value:
        max_value = x
print(f'{max_value}')