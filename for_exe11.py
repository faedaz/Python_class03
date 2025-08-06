# Exercício 8: Palíndromo
# Objetivo: Verificar se uma palavra é um palíndromo (lê-se da mesma forma de trás para frente, desconsiderando maiúsculas/minúsculas).
# Dados Iniciais: palavra = "Radar"
# Tarefa: Crie uma versão invertida da palavra e compare-a com a original (ambas em minúsculas). Imprima se a palavra é ou não um palíndromo.

word = "Radar"
reversed_word = " "

reversed_word = word[::-1]

if word.lower() == reversed_word.lower():
    print('right')
else:
    print('wrong')
print(reversed_word)