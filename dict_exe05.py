# Exercício 5: Remoção de um Elemento Imagine que você decidiu não mais armazenar o gênero do livro. Remova a chave 'genero' e seu valor correspondente do dicionário. Imprima o resultado.

book = {
    'title': 'Lord of Rings',
    'author': 'J. R. R. Tolkien',
    'year_publish': 1953,
    'theme': 'fantasy',
    'grade': "9/10"
}

del book['theme']
print(book)
del book['grade']
print(book)