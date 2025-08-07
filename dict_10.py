# Exercício 10: Encontrando a Chave com o Maior Valor Considere um dicionário que mapeia o nome de estudantes às suas notas. 
# Escreva um código que identifique e imprima o nome do estudante com a nota mais alta.

grade: dict[str, float] = {
    'Ana': 7,
    'Bruno': 9.4,
    'Matheus': 10,
    'Carlos': 6.9
}

highest_grade: float = float('-inf')
better_studant: str = ""

# could use max function:
# better_studant: str = max(grade, key=grade.get)
# highest_grade: float = grade[better_studant]

for k, v in grade.items():
    if v > highest_grade:
        highest_grade = v
        better_studant = k
        
print(f"Higher grade: {highest_grade}, Student: {better_studant}")