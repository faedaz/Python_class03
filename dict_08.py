# Exercício 8: Iteração sobre Pares Chave-Valor Ainda com o dicionário de países, 
# 
# empregue um laço for para imprimir cada país e sua capital no formato: "A capital de [País] é [Capital]".

country = {
    'Brazil': 'Brasilia',
    'Argentina': 'Buenos Aires',
    'Spain': 'Madrid',
    'Portugal': 'Lisboa'    
}

for k, v in country.items():
    print(f"Country: {k}, capital: {v}")