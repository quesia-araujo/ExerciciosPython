'''
Faça um Programa que peça as quatro notas de 5 alunos, calcule
e armazene numa lista a média de cada aluno, imprima o número
de alunos com média maior ou igual a 7.0.

'''

alunos = 0 # iniciar o contador de alunos
media_notas_alunos = [] # lista para armazenar as médias 
 

for aluno in range(5): # uso do laço para os alunos
    print("Aluno", aluno + 1)
    alunos += 1

    notas_alunos = [] # armazar as notas dos alunos em uma lista

    for nota in range(4): # segundo for para as notas (for aninhado)
        notas = float(input(f"Digite a {nota + 1}ª nota: "))
        notas_alunos.append(notas)
       
    
    media = sum(notas_alunos) / len(notas_alunos)
    media_notas_alunos.append(media)
    
#sum é uma função embutida com valor True(1)
alunos_aprovados = sum(media >= 7.0 for media in media_notas_alunos)

print(f"Quantidade de alunos com média maior ou igual a 7.0: {alunos_aprovados}")
