# Exercício 9: Filtrando uma Lista
# Objetivo: Criar uma nova lista contendo apenas os nomes que começam com a letra "A".
# Dados Iniciais: nomes = ["Ana", "Bruno", "Amanda", "Carlos", "Antonio"]
# Tarefa: Crie uma lista vazia. Percorra a lista nomes e, se um nome começar com "A", adicione-o à nova lista. Imprima a nova lista no final.

names = ['Ana', 'Bruno', 'Amanda', 'Carlos', 'Antonio']
names_with_a = []

for x in names:
    if x.startswith("A"):
        names_with_a.append(x)
    else:
        continue
print(names_with_a)