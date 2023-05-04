import math


# ###Задание 1

def square(a):
    print('Периметр квадрата:', a * 4)
    print('Площадь квадрата:', a ** 2)
    print('Диагональ квадрата:', math.sqrt(a))


# square(5)

# ###Задание 2

def discriminant(a, b, c):
    d = b ** 2 - 4 * a * c
    print(d)


# discriminant(1, 2, 3)


# ###Задание 3

def two_lines(string_1, string_2):
    a = string_1[:2]
    b = string_2[:2]
    print(b + string_1[2:] + ' ' + a + string_2[2:])
    return


# two_lines('мама', 'vfvfbfggf')

# ###Задание 4

def without_extensions(path):
    reversed_string = ''.join(reversed(path))  # перевернул строку
    point = reversed_string.index('.') + 1  # вычислил индекс точки + 1 для расчета
    end_delimiter = reversed_string.index('\\')  # вычислил  индекс косой
    result_name = ''.join(
        reversed(reversed_string[point:end_delimiter]))  # вырезал все что от точки до косой и перевернул
    print('Название файла: ' + result_name)

    print('Название диска: ' + path[:1])

    start_delimiter = path[3:].index('\\')  # 3 - это значение диска со спецсимволами. Вычислил индекс второй косой
    print('Название корневой папки: ' + path[3:start_delimiter + 3])
    return


# without_extensions(r'C:\Usegrs\sazhinovia\Desktop\Итоги\Итоги для видеообучеgния.txt')


# ###Задание 5

def two_numbers(a, b):
    summ = a + b
    pro = a * b
    print(f'{a} + {b} = {summ}')
    print(f'{a} * {b} = {pro}')
    return


# two_numbers(2, 3)

# ###Задание 6

def string_del(string):
    result = string[1::2]
    print(result)
    return


# string_del('ф1ф2ф3ф4ф5ф6ф7ф8ф')

# ###Задание 7

def two_string(string1, string2):
    first_cut = string2.index(string1[0])
    second_cut = string2.index(string1[1])
    third_cut = string2.index(string1[2])
    i_1 = min(first_cut, third_cut, second_cut)
    i_2 = max(first_cut, third_cut, second_cut) + 1

    print(first_cut, third_cut, second_cut)
    print(i_1, i_2)
    result = string2[i_1:i_2]
    print(result)
    return

# two_string('123','bdb  1 ebgfbv2 bf3')
