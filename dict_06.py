# Exercício 6: Iteração sobre Chaves 
# Crie um dicionário com os nomes de cinco países como chaves e suas respectivas capitais como valores. 
# Utilize um laço for para imprimir todas as chaves (nomes dos países).

country = {
    'Brazil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Spain': 'Madrid',
    'Portugal': 'Lisboa'    
}

for k in country.keys():
    print(f"Country: {k}")

for v in country.values():
    print(f"Capital: {v}")
