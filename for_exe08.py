# Exercício 5: Soma de uma Lista
# Objetivo: Calcular a soma de todos os números em uma lista.
# Dados Iniciais: lista_numeros = [10, 20, 30, 40, 50]
# Tarefa: Crie uma variável soma_total iniciada em 0. Percorra a lista e, a cada iteração, adicione o número atual à soma_total. No final, imprima o resultado.

numbers_list = [10, 20, 30, 40, 50]


total_sum = 0

for x in numbers_list:
    total_sum += x
print(f'Total sum: {total_sum}')