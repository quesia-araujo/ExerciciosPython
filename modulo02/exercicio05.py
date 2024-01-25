#Questão 5
#Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno. 
# equilátero: todos os lados com o mesmo valor isósceles: dois lados com o mesmo valor escaleno: todos os lados com medidas distintas

lado1 = float(input('Qual o comprimento do primeiro lado do triangulo? '))
lado2 = float(input('Qual o comprimento do segundo lado do triangulo? '))
lado3= float(input('Qual o comprimento do terceiro lado do triangulo? '))

if (lado1 + lado2 < lado3) or (lado1 + lado3 < lado2) or (lado2 + lado3 < lado1):    # Para conferir se é um triângulo
    print('Não é um triângulo!')
else:
    if (lado1 == lado2) and (lado2 == lado3):
        print ('Triângulo equilatero')
    else:
        if (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
            print('Triângulo isosceles')
        else:
            print('Triângulo escaleno')
