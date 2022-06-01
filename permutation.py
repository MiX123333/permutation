result = ''
message = ''
choice = ''

while choice != '-1':
    choice = input("\nВы хотите зашифровать или расшифровать сообщение?\nВведите 1 для шифрования, 2 для расшифровки, -1 Выход из программы: ")
#если выбрали 1
    if choice == '1':
        choice = input("\nУкажите вид элемента.\n Введите 1 для ввода одного символа, 2 для ввода группы символов, 3 для ввода слова: ")
        message = input("\nВедите сообщение для шифрования: ")
#перебираем сообщение посимвольно
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) - 2)

        print (result + '\n\n')
        result = ''
#если выбрали 2
    elif choice == '2':
        choice = input("\nУкажите вид элемента.\n Введите 1 для расшифрования одного символа, 2 для расшифрования группы символов, 3 для расшифрования слова: ")
        message = input("\nВведите сообщение для расшифрования: ")
        
        for i in range(0, len(message)):
            result = result + chr(ord(message[i]) + 2)

        print (result + '\n\n')
        result = ''

    elif choice != '-1':
        print ("Вы ввели неверный выбор.Повторите попытку\n\n")
    
