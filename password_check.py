"""
Description: A simple password checker

Name: Nurul Syafini Subhan
"""


def is_valid_password(text):
    """Check whether a given text has the correct password format"""
    return 8 <= len(text) <= 20


def main():
    """Start program"""
    new_password = input("Input password: ")
    new_password = len(new_password)
    for i in range(new_password):
        print('*', end='')


if __name__ == '__main__':
    main()
