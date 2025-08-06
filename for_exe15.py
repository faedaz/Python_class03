# Exercício 12: Removendo Duplicatas
# Objetivo: Dada uma lista com elementos duplicados, criar uma nova lista contendo apenas os elementos únicos, na ordem em que apareceram pela primeira vez.
# Dados Iniciais: lista_com_duplicatas = [1, 2, 2, 3, 4, 3, 5, 1, 6]
# Tarefa: Crie uma lista vazia. Percorra a lista original e, para cada item, verifique se ele já existe na sua nova lista. Se não existir, adicione-o.

list_with_duplicate = [1, 2, 2, 3, 4, 3, 5, 1, 6]
new_list = []

for x in list_with_duplicate:
    if not x in new_list:
        new_list.append(x)
    else:
        continue
print(new_list)