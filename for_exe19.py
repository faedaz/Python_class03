# Exercício 16: Relatório de Vendas
# Objetivo: Calcular o faturamento total de uma lista de vendas.
# Dados Iniciais: vendas = [{'produto': 'Monitor', 'preco': 800, 'qtd': 2}, {'produto': 'Teclado', 'preco': 120, 'qtd': 5}]
# Tarefa: Percorra a lista. Para cada dicionário, multiplique o 'preco' pela 'qtd' para obter o subtotal. Some todos os subtotais para obter o faturamento total.

sell = [
    {'product': 'Monitor', 'price': 800, 'qtt': 2}, # primeiro dicionario
    {'product': 'Keyboard', 'price': 120, 'qtt': 5} # segundo dicionario
]

total_price = 0
total_qtt = 0
total = 0

# no primeiro for o X representa o primeiro dicionario 
for x in sell:
    total_price = x['price'] * x['qtt']
    total += total_price
print(f"Total price: {total}")