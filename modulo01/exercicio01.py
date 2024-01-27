def multiplicar(primeiro_numero: any, segundo_numero: any):
    resultado = float(primeiro_numero) * float(segundo_numero)
    return print(f"O resultado da multiplicação é: {resultado}")


def dividir(primeiro_numero: any, segundo_numero: any):
    resultado = float(primeiro_numero) / float(segundo_numero)
    return print(f"O resultado da divisão é {resultado}")


def subtrair(primeiro_numero: any, segundo_numero: any):
    resultado = float(primeiro_numero) - float(segundo_numero)
    return print(f"O resultado da subtração é {resultado}")


def somar(primeiro_numero: any, segundo_numero: any):
    resultado = float(primeiro_numero) + float(segundo_numero)
    return print(f"O resultado da soma é {resultado}")


if __name__ == "__main__":
    primeiro_numero = input("Digite seu primeiro número: ")
    segundo_numero = input("Digite seu segundo número: ")
    multiplicar(primeiro_numero, segundo_numero)
    dividir(primeiro_numero, segundo_numero)
    subtrair(primeiro_numero, segundo_numero)
    somar(primeiro_numero, segundo_numero)
