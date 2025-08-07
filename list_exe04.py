# Elabore um programa que conte quantas vezes um determinado elemento aparece em uma lista. O programa deve solicitar ao utilizador a lista e o elemento a ser contado.

# Exemplo:

# Lista: ['a', 'b', 'c', 'a', 'd', 'a']

# Elemento a ser contado: 'a'

# Saída Esperada: O elemento 'a' aparece 3 vezes na lista.

list_n: list = input("Type your letters: ").split()

print(list_n)

find_letter: str = input("Type the letter that you wanna count: ")
print(f"The letter '{find_letter}' is your counter")

counter: int = 0

for x in list_n:
    if x == find_letter:
        counter = counter + 1
if counter == 0:
    print(f"{find_letter} ins't in the list!")
else:
    print(f"Total find: {counter}")