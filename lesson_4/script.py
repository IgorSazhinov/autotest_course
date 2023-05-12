my_list = [11, [1, 2, 3, 4, 5], 3, 4, 5]

# for i in range(7):
#    if i == 5:
#        pass
# else:
#     print('Мы завершили цикл')


# print(type(range(1, 6), range(1, 6)[2]))
# a = 0
# for idx, value in enumerate(my_list):
#     print(idx, value)
# print(my_list)


# s_address = [
#    ['dfcswc', 'cds', 'dsc', 'dcssdc', 'cdscd'],
#    ['ewrwe', 'erwe', 'erwer', 'erewe', 'erwer'],
#    ['erwwer', 'ewrwer', 'ewrwer', 'erwer', 'ewrwer']]

# for letter in s_address:
#    for name in letter:
#        for char in name:
#            print(char, end=' ')

# arr = []
# for i in range(100):
#     arr.append(i + 1)
#     print(arr)


# arr1 = [i**2 for i in range(100) if i % 2 == 0]
# print(arr1)


# a = True  # 1
# b = False  # 0

# print(type(b), b)
# print(type(a), a)

# print(bool(0), bool(0), bool(''), bool([]))
# print(bool(1), bool(-12), bool(' '), bool(['']))

# my_age = 23
# if my_age < 18:
#     print('Ура')
# elif my_age >= 70:
#     print('мда')
# else:
#     print('Не ура')

# a = 1
# b = 15

# if a < b:
#    rez = a + b
# else:
#     rez = a - b

# rez = a + b if a < b else a - b

# print(rez)
# i = 0
# while i < 10:
#     i = i + 1
#     if i == 5:
#         break
#     elif i == 2:
#         continue
#     else:
#         print(i)

#print(not True or True)

# print(1 in [1, 2, 34, 4, 3])

# print(type(None))

import math

num = 12345
arr = [int(i) for i in str(num)]
print(arr)
