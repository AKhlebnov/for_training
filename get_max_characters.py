"""
Самое частое слово.
"""


def read_data():
    with open('input.txt', 'r') as file:
        s = ' '.join(file.read().split())

    return s


def write_data(data):
    with open('output.txt', 'w') as file:
        file.write(data)


def max_char(text):
    sep_text = text.lower().split()

    dict_text = {i: sep_text.count(i) for i in sep_text}

    max_char = max(dict_text, key=lambda x: dict_text[x])

    return f'{max_char} {dict_text[max_char]}'


def main():
    data = read_data().strip()
    max_str = max_char(data)
    write_data(max_str)


if __name__ == "__main__":
    main()


# Недавно мы считали для каждого слова количество его вхождений в строку.
# Но на все слова может быть не так интересно смотреть, как, например,
# на наиболее часто используемые.

# Напишите программу, которая считывает текст из файла
# (в файле может быть больше одной строки)
# и выводит самое частое слово в этом тексте и через пробел то, сколько раз
# оно встретилось.
# Если таких слов несколько, вывести лексикографически первое
# (можно использовать оператор < для строк).

# В качестве ответа укажите вывод программы, а не саму программу.

# Слова, написанные в разных регистрах, считаются одинаковыми.

# Sample Input:

# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:

# abc 3
# У вас есть неограниченное число попыток.
# Время одной попытки: 5 mins

# Для запуска программы нужно в корневой директории расположить файл input.txt
# с данными для работы программы. После окончания раюоты программы будет
# создан файл output.txt с результатом работы.
