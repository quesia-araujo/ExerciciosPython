primeiro_numero = input("Insira seu primeiro numero: ")
segundo_numero = input("Insira seu segundo numero: ")


def calcular_maior_que(primeiro_numero, segundo_numero):
    try:
        primeiro_numero = int(primeiro_numero)
        segundo_numero = int(segundo_numero)
        if primeiro_numero > segundo_numero:
            return print(f"O maior número é: {primeiro_numero}")
        elif primeiro_numero == segundo_numero:
            return print("Ambos os numeros são iguais!")
        elif segundo_numero > primeiro_numero:
            return print(f"O maior número é: {segundo_numero}")
    except ValueError:
        print(
            "Não é possível fazer operações com esse tipo. Por favor, insira números inteiros ex: 1, 2, 3"
        )


if __name__ == "__main__":
    calcular_maior_que(primeiro_numero, segundo_numero)
