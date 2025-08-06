# Exercício 7: Iteração sobre Valores Utilizando o mesmo dicionário de países e capitais, use um laço for para imprimir todos os valores (nomes das capitais).

country = {
    'Brazil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Spain': 'Madrid',
    'Portugal': 'Lisboa'    
}

for v in country.values():
    print(f"Capital: {v}")