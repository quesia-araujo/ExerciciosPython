'''
Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721.
'''

def reverso_numero(numero):

    # Converter o número para string, inverte e converte de volta para inteiro
    reverso = int(str(numero)[::-1])
    return reverso

# Solicita ao usuário um número inteiro
numero_usuario = int(input("Digite um número inteiro: "))

# Chama a função e imprime o reverso do número
resultado = reverso_numero(numero_usuario)
print(f"O reverso do número {numero_usuario} é: {resultado}")