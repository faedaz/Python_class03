# Exercício 12: Adição de Itens a uma Lista Interna 
# A partir do dicionário do exercício anterior, adicione um novo item à lista de 'frutas'. Imprima o dicionário atualizado para verificar a alteração.

categories: dict[str, list[str]] = {
    'fruits': ['apple', 'banana', 'oranje'],
    'vegetables': ['carrot', 'potato', 'broccoli']
}

categories['fruits'].append('pineapple')
print(categories)

categories['vegetables'].append('Beetroot')
print(categories)