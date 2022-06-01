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
