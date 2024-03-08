def shift_char_ru(char, shift):
    char_code = ord(char)
    if 'а' <= char <= 'я':
        shifted_code = (char_code - ord('а') + shift) % 32 + ord('а')
    elif 'А' <= char <= 'Я':
        shifted_code = (char_code - ord('А') + shift) % 32 + ord('А')
    else:
        return char

    return chr(shifted_code)


def decode_shift_char_ru(char, shift):
    char_code = ord(char)
    if 'а' <= char <= 'я':
        shifted_code = (char_code - ord('а') - shift) % 32 + ord('а')
    elif 'А' <= char <= 'Я':
        shifted_code = (char_code - ord('А') - shift) % 32 + ord('А')
    else:
        return char

    return chr(shifted_code)


def shift_char_eng(char, shift):
    char_code = ord(char)
    if 'a' <= char <= 'z':
        shifted_code = (char_code - ord('a') + shift) % 26 + ord('a')
    elif 'A' <= char <= 'Z':
        shifted_code = (char_code - ord('A') + shift) % 26 + ord('A')
    else:
        return char

    return chr(shifted_code)


def decode_shift_char_eng(char, shift):
    char_code = ord(char)
    if 'a' <= char <= 'z':
        shifted_code = (char_code - ord('a') - shift) % 26 + ord('a')
    elif 'A' <= char <= 'Z':
        shifted_code = (char_code - ord('A') - shift) % 26 + ord('A')
    else:
        return char

    return chr(shifted_code)


def coding_ru(text, shift):
    shifted_string = ''.join(shift_char_ru(char, shift) for char in text)
    return shifted_string


def decoding_ru(text, shift):
    shifted_string = ''.join(decode_shift_char_ru(char, shift)
                             for char in text)
    return shifted_string


def coding_eng(text, shift):
    shifted_string = ''.join(shift_char_eng(char, shift) for char in text)
    return shifted_string


def decoding_eng(text, shift):
    shifted_string = ''.join(decode_shift_char_eng(char, shift)
                             for char in text)
    return shifted_string


def main():
    enter = input("Кодирование(1), декодирование(2): ")
    if enter == '1':
        language = input("Rusian(1), English(2): ")
        if language == '1':
            text = input("Введите строку: ")
            shift = int(input("Введите сдвиг: "))
            print(coding_ru(text, shift))
        elif language == '2':
            text = input("Введите строку: ")
            shift = int(input("Введите сдвиг: "))
            print(coding_eng(text, shift))
        else:
            print("Error")
    elif enter == '2':
        language = input("Rusian(1), English(2): ")
        if language == '1':
            text = input("Введите строку: ")
            shift = int(input("Введите сдвиг: "))
            print(decoding_ru(text, shift))
        elif language == '2':
            text = input("Введите строку: ")
            shift = int(input("Введите сдвиг: "))
            print(decoding_eng(text, shift))
        else:
            print("Error")
    else:
        print("Неправильный ввод!")


if __name__ == '__main__':
    main()
