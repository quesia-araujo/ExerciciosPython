import locale

locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")


class SalarioLiquido:
    def __init__(self):
        self.salario_bruto = 0
        self.salario_liquido = 0
        self.desconto = 0

    def validar_formato(self, salario_bruto: any):
        if type(salario_bruto) is not float and type(salario_bruto) is not int:
            raise ValueError(
                "Por favor, coloque o valor de seu salário bruto em inteiro ou decimal de duas casas!"
            )

        self.salario_bruto = salario_bruto
        self.__formatar_salario_bruto()

    def __formatar_salario_bruto(self):
        self.salario_bruto = float(self.salario_bruto)

    def calcula_aliquota(self):
        if self.salario_bruto <= float(1903.98):
            self.salario_liquido = self.salario_bruto - (self.salario_bruto * 0)

        elif float(1903.99) <= self.salario_bruto <= float(2826.65):
            self.salario_liquido = self.salario_bruto - (self.salario_bruto * 0.075)

        elif float(2826.66) <= self.salario_bruto <= float(3751.05):
            self.salario_liquido = self.salario_bruto - (self.salario_bruto * 0.15)

        elif float(3751.06) <= self.salario_bruto < float(4664.68):
            self.salario_liquido = self.salario_bruto - (self.salario_bruto * 0.225)

        elif self.salario_bruto >= float(4664.68):
            self.salario_liquido = self.salario_bruto - (self.salario_bruto * 0.275)

    def calcula_desconto(self):
        self.desconto = self.salario_bruto - self.salario_liquido

    def retorna_valores(self):
        salario_liquido = locale.currency(self.salario_liquido, grouping=True)
        desconto = locale.currency(self.desconto, grouping=True)
        print(
            f"O seu Salário Líquido é de {salario_liquido} sendo descontados {desconto}"
        )


if __name__ == "__main__":
    salario_liquido = SalarioLiquido()
    salario_bruto = input(
        "Olá, insira seu salário bruto aqui para calcular o IR (exemplos de valores permitido 500.50/500 ): "
    )
    salario_liquido.validar_formato(salario_bruto)
    salario_liquido.calcula_aliquota()
    salario_liquido.calcula_desconto()
    print("Calculando... \n" * 3)
    salario_liquido.retorna_valores()
