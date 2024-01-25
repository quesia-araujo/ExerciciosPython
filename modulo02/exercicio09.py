#Questão 9
# O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário informar o valor zero.
# Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.

par = 0
impar = 0
numerow = int

while numerow != 0 :
    numerow = int(input('Digite um número: '))
    if (numerow%2) == 0 and (numerow > 0):
        par += 1
    else:
        if (numerow%2) != 0 and (numerow > 0): 
            impar += 1
            

print(f'Qtd de números pares: {par}')
print(f'Qtd de números ímpates: {impar}')