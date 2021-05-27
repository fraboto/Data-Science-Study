def read():
    numbers = []

    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            try:
                numbers.append(int(line))
            except ValueError:
                numbers.append('NaN')

    print(numbers)


def write():
    names = ['Francisco', 'José', 'Ana', 'María']

    with open('./files/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(f'{name}\n')


def run():
    # read()
    write()


if __name__ == '__main__':
    run()