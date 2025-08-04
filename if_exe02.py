# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

try:
    temperature = float(input('Type the temperature: '))

    if temperature < 18:
        print('Low temperature')
    elif temperature >= 18 and temperature <= 26:
        print('Ambient temperature')
    else:
        print('High temperature')
except ValueError:
    print('Type a number!')
except Exception as error:
    print(f'Error: {error}')