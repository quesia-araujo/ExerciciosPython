def reverse_username(username: str) -> str:
    return username.upper()[::-1]


if __name__ == '__main__':
    print(reverse_username('Yohanna'))
    print(reverse_username('Milena'))
    print(reverse_username('Siomara'))
    print(reverse_username('Quesia'))
