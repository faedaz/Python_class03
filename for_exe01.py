# Contexto: Você recebeu uma lista de números de um sensor e precisa processar apenas os valores que são pares para uma análise futura.
# Dados Iniciais:
# numeros = [11, 24, 33, 48, 51, 62, 75, 80, 99, 104]
# Sua Tarefa:
# Crie um laço for que percorra cada número na lista numeros.
# Dentro do laço, use uma condição if para verificar se o número é par.
# Se o número for par, imprima uma mensagem na tela, como por exemplo: "O número 48 é par.".

numeros = [11, 24, 33, 48, 51, 62, 75, 80, 99, 104]

for i in numeros:
    if i % 2 ==0:
        print(f'{i} is even')
    
    