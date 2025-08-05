# Contexto: Em um jogo de espionagem, você precisa inverter mensagens para criar códigos secretos. Sua tarefa é pegar uma palavra e criar uma nova string com seus caracteres na ordem inversa.

# palavra_secreta = "desenvolvimento"
# palavra_invertida = "" # Comece com uma string vazia para construir o resultado
# Sua Tarefa:

# Crie um laço for que percorra cada caractere da palavra_secreta.

# A cada iteração, adicione o caractere atual no início da variável palavra_invertida.

# Após o término do laço, imprima o resultado final contido na variável palavra_invertida.

palavra_secreta = "desenvolvimento"
palavra_invertida = ""

for i in reversed(palavra_secreta):
    print(i)
    palavra_invertida = palavra_invertida + i
print(palavra_invertida)