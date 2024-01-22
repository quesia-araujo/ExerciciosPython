import sys


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9


def convert_temperature(choice: str, value: float) -> str:
    if choice == '1':
        return f'{celsius_to_fahrenheit(value)}°F'
    elif choice == '2':
        return f'{fahrenheit_to_celsius(value)}°C'
    elif choice == '3':
        sys.exit()
    else:
        raise ValueError('Você digitou uma escolha não mapeada')


def display_menu() -> None:
    print(
        '__________________________________________\n'
        '|             MENU CONVERSÃO             |\n'
        '------------------------------------------\n'
        '| 1) Converter para Fahrenheit           |\n'
        '| 2) Converter para Celsius              |\n'
        '| 3) Sair do Menu                        |'
        '|________________________________________|\n'
    )


def main() -> str:
    try:
        display_menu()
        choice = input('>>> ')
        return sys.exit() if choice == '3' else convert_temperature(choice, float(input('Digite o valor que deseja converter: '))) 
    except ValueError as e:
        print('Ocorreu um ERRO!! --> ', e, '\nTente novamente')
        return main()


if __name__ == '__main__':
    print(main())
