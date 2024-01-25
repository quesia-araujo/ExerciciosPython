class AuthenticationError(Exception):
    pass


ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'


def access_user(username: str, password: str) -> bool:
    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    raise AuthenticationError('Invalid credentials')


try:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    access_user(username, password)
    print('Authentication successful!')
except AuthenticationError:
    print('Error: Invalid credentials. Please try again.')
