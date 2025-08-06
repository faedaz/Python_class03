# Exercício 14: Média de Notas
# Objetivo: Calcular a média das notas de um aluno armazenadas em um dicionário.
# Dados Iniciais: notas_aluno = {'Matemática': 8.5, 'Português': 9.0, 'História': 7.5, 'Ciências': 8.0}
# Tarefa: Percorra os valores do dicionário (as notas) para calcular a soma total. Depois, divida pela quantidade de matérias para obter a média.

student_grade = {
    'mathematics': 8.5,
    'portuguese': 9.0,
    'history': 7.5,
    'science': 8.0
}
total_grade = 0.0


for g in student_grade.values():
    total_grade += g
final_grade = total_grade / len(student_grade)
print(f'Final grade: {final_grade}')