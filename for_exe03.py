# Contexto: Você tem uma lista com as temperaturas máximas de cada dia da semana e precisa descobrir qual foi a maior temperatura registrada e em que dia ela ocorreu (usando o índice da lista como o dia).

# temperaturas_semana = [28, 31, 27, 33, 32, 30, 29]
# maior_temperatura = 0
# dia_mais_quente = 0

# Crie um laço for que percorra os índices da lista temperaturas_semana. A melhor forma de fazer isso é usando range() junto com len().

# Dentro do laço, compare a temperatura do dia atual (temperaturas_semana[i]) com o valor armazenado na variável maior_temperatura.

# Se a temperatura do dia atual for maior, atualize o valor da maior_temperatura e também atualize a variável dia_mais_quente com o índice i atual.

# No final, fora do laço, imprima uma mensagem mostrando qual foi a maior temperatura e o "dia" (índice) em que ela ocorreu. Por exemplo: "A maior temperatura foi de 33°C no dia de índice 3."

week_temperature = [28, 31, 27, 33, 32, 30, 29]
higher_temperature = 0
hotter_day = 0

for i in range(len(week_temperature)):
    day_temperature = week_temperature[i]
    if day_temperature > higher_temperature:
        higher_temperature = day_temperature
        hotter_day = i
print(f'hotter day is {hotter_day}th day, with {higher_temperature} Celsius')