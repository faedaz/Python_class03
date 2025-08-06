# Exercício 13: Imprimindo Itens de um Dicionário
# Objetivo: Percorrer um dicionário e imprimir suas chaves e valores de forma formatada.
# Dados Iniciais: aluno = {'nome': 'João', 'idade': 22, 'curso': 'Engenharia'}
# Tarefa: Use o método .items() para percorrer o dicionário e imprimir: "A chave é [chave], o valor é [valor]".

student = {
    'name': 'Joao', 
    'age': 22, 
    'class': 'Engineer',
}

# print(student)
# print(student.values())
# print(student.keys())
# print(student.items())

for key, value in student.items():
    print(f"Key: {key} and value {value}")