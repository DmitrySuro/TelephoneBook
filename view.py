def get_name():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[0].strip())


def get_number():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[1].strip())


def what_to_do():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[2].strip())


def export_book(dict_book: dict):
    with open('file_export.txt', 'w') as file:
        for key, value in dict_book.items():
            print(key,value)
            file.write(key + '\n')
            print(key)
            for elem in value:
                file.write(elem + ', ')
                print(elem, end=' ')
            print('')
