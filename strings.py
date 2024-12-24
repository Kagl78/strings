my_string = input("Введите любой текст: ")
print("Количество символов в тексте:", len(my_string))
print("Текст в верхнем регистре:", my_string.upper())
print("Текст в нижнем регистре:", my_string.lower())
my_string_no_spaces = my_string.replace(" ", "")
print("Текст без пробелов:", my_string_no_spaces)
if my_string:
    print("Первый символ строки:", my_string[0])
if my_string:
    print("Последний символ строки:", my_string[-1])
