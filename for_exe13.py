# Exercício 10: Transformando uma Lista
# Objetivo: Criar uma nova lista onde cada elemento é o dobro do valor da lista original.
# Dados Iniciais: valores = [1, 2, 3, 4, 5]
# Tarefa: Crie uma lista vazia. Percorra a lista valores, calcule o dobro de cada número e adicione o resultado à nova lista.


values = [10, 20, 30, 40, 50]
double_values = []

for x in values:
    double_values.append(x * 2)
print(double_values)