PASS = '1234'

def pass_required(func):
    def wrapper():
        password = input('Cual es tu password? ')

        if password == PASS:
            return func()
        else:
            print('La contraseña no es correcta')

    return wrapper

def upper_name(func):
    def wrapper(*args, **kwargs):
        result = func(*args, *kwargs)
        return result.upper()
    return wrapper

@pass_required
def needs_pass():
    print('La contraseña es correcta')

@upper_name
def say_my_name(name):
    return 'Hola {}'.format(name)


if __name__ == '__main__':
    needs_pass()
    print(say_my_name('Fer'))