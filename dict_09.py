# Exercício 9: Cálculo com Valores Numéricos 
# Crie um dicionário que armazene os produtos de um carrinho de compras, onde a chave é o nome do produto e o valor é o seu preço. Calcule e imprima o valor total da compra somando todos os preços.

car_list = {
    'product': 'Monitor',
    'qtt': 3,
    'setor': 'eletronic',
    'price': 200.90  
    
}

total_price = car_list['qtt'] * car_list['price']

print(total_price)