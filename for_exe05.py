# Exercício 2: Tabuada de Multiplicação
# Objetivo: Imprimir a tabuada de um número específico (por exemplo, 7).
# Dados Iniciais: numero_tabuada = 7
# Tarefa: Crie um laço que vá de 1 a 10 e imprima a multiplicação de numero_tabuada por cada número do laço. Ex: "7 x 1 = 7".

TABUADA = 7

for x in range (1, 11, 1):
    tabuada = TABUADA * x
    print(f'{x} * {TABUADA} = {tabuada}')