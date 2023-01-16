PASSWORD = '12345'


def password_required(func):
    def wrapper():
        password = input('What is your password? ')

        if password == PASSWORD:
            return func()
        else:
            print('Wrong password!')

    return wrapper

@password_required #decorator, allows code to be executed before this function
def needs_password():
    print('Correct password!')
    return True

def upper_word(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        return result.upper()

    return wrapper


@upper_word
def say_my_name(name):
    return 'Hi, {} nice to know you!'.format(name)


if __name__ == '__main__':
    if needs_password():
        print(say_my_name(input('What\'s your name: ')))