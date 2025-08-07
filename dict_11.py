# Exercício 11: Dicionário com Valores em Lista 
# Crie um dicionário onde as chaves são nomes de categorias (ex: 'frutas', 'legumes') e os valores são listas de itens pertencentes a cada categoria.

categories: dict[str, list[str]] = {
    'fruits': ['apple', 'banana', 'oranje'],
    'vegetables': ['carrot', 'potato', 'broccoli']
}

print(categories.values())