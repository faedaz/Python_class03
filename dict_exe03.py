# Exercício 3: Modificação de um Valor Suponha que o ano de publicação do livro estava incorreto. Altere o valor da chave 'ano_publicacao' para um novo ano e, em seguida, imprima o dicionário atualizado.



book = {
    'title': 'Lord of Rings',
    'author': 'J. R. R. Tolkien',
    'year_publish': 1953
}

book['year_publish'] = 1954
print(book)
book['author'] = 'John Ronald Reuel Tolkien'
print(book)