# Exercício 2: Acesso a Dados A partir do dicionário criado no exercício anterior, acesse e imprima apenas o valor associado à chave 'autor'.

book = {
    'title': 'Lord of Rings',
    'author': 'J. R. R. Tolkien',
    'year_publish': 1954
}

author_book = book['author']
print(f"Book author: {author_book}")