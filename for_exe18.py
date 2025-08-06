# Exercício 15: Buscando em Lista de Dicionários
# Objetivo: Encontrar o dicionário de um produto específico pelo seu 'id'.
# Dados Iniciais: estoque = [{'id': 1, 'produto': 'Monitor'}, {'id': 2, 'produto': 'Teclado'}, {'id': 3, 'produto': 'Mouse'}]
# Tarefa: Percorra a lista estoque. Se o valor da chave 'id' do dicionário atual for igual a 2, imprima o dicionário inteiro e pare o laço.

store = [
    {'id': 1, 'produto': 'Monitor'}, 
    {'id': 2, 'produto': 'Teclado'}, 
    {'id': 3, 'produto': 'Mouse'}]

ID = 2
for item in store:
    if item['id'] == ID:
        print(f"ID find! {item}")


