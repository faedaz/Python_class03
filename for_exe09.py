# Exercício 6: Contando Vogais
# Objetivo: Contar quantas vogais (a, e, i, o, u) existem em uma determinada frase.
# Dados Iniciais: frase = "A persistência é o caminho do êxito"
# Tarefa: Percorra cada caractere da frase. Se o caractere for uma vogal (considere maiúsculas e minúsculas), incremente um contador. Imprima o total no final.


phrase = "A persistencia e o caminho do exito"
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

for x in phrase.lower():
    if x == 'a':
        count_a += 1
    elif x == 'e':
        count_e += 1
    elif x == 'i':
        count_i += 1
    elif x == 'o':
        count_o += 1
    elif x == 'u':
        count_u += 1
    else:
        continue
print(f' count a: {count_a} \n count e: {count_e} \n count i: {count_i} \n count o: {count_o} \n count u: {count_u}')    