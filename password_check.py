def is_valid_password(text):
    return 8 <= len(text) <= 20


def main():
    new_password = input("Input password: ")
    new_password = len(new_password)
    for i in range(new_password):
        print('*', end='')


if __name__ == '__main__':
    main()
