def choose():  # Функция выбора режимов (главное меню)
    print('Выберите режим:')
    print('1 - Шифрование')
    print('2 - Расшифровка ')
    print('3 - Выйти')
    mode = int(input())
    if mode == 1:
        encryption()
    elif mode == 2:
        decryption()
    elif mode == 3:  # Выход из программы
        return 0

    else:
        print('Введен некорректный символ')
        choose()


def encryption():  # Функция шифрования
    print('Выберите режим Шифрования:')
    print('1 - один символ')
    print('2 - группа символов ')
    print('3 - слово')
    encryption_mode = int(input())
    if encryption_mode == 1:  # (один символ), с 25 по 29 получаем все нужные параметры
        print('Введите текст:')
        text = input()
        print('Введите ключ')
        key = input()
        len_key = len(key)
        for numb in key:  # проверка, что цифры в ключе не превосходят длину
            if int(numb) >= len_key:
                print('Цифры в ключе не должны быть больше чем длина ключа -1')
                encryption()  # если превосходят, вызываем функцию заново (рекурсия)
        list_text = [(text[i:i + len_key]) for i in range(0, len(text), len_key)]
        if len(list_text[-1]) != len_key:  # способ шифрования последнего блока с 35 по 37 строку
            while len(list_text[-1]) != len_key:
                list_text[-1] += '\0'
        result = []
        for elements in list_text:  # заранее создаем список из нулей, потом 0 будут заменяться на конечный результат
            elements = list(elements)
            arr = [0] * len_key
            total = 0
            for numbers in key:  # сам цикл шифрования, по итогу у нас получается двумерный список
                arr[int(numbers)] = elements[total]
                total += 1
            result.append(arr)
            res1 = []
        for res in result:  # превращаем двумерный список в одномерный
            res1.append(''.join(res))

        res1 = ''.join(res1)  # превращаем одномерный список в строку
        end_result = res1.replace('\0', '')  # убираем все \0
        print('Результат шифрования:')
        print(end_result)
        choose()  # возвращаемся в главное меню

