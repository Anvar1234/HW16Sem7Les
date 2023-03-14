# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке.

# Ввод: 
# пара-ра-рам рам-пам-папам па-ра-па-дам 
# Вывод:
# Парам пам-пам

# #1 способ
# date = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# lst = list(date.split())
# print(date)

# bukvy = 'уеыаоэяию'
# print(bukvy)

# count = 0
# lst2 = []

# for i in range(len(lst)):
#     for j in range(len(lst[i])):
#         for k in bukvy:
#             if k == lst[i][j]:
#                 count += 1
#     lst2.append(count)
#     count = 0
# print(lst2)

# if lst2.count(lst2[0]) == len(lst2):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")



#2 способ, усовершенствованный. С функц высшего порядка.

# # Функция для подсчета гласных букв в слове:
# def numb_of_glasnyi(word):
#     bukvy = 'уеыаоэяию' #список гласных
#     count = 0
#     for i in word:
#         if i in bukvy:
#             count += 1
#     return count

# date = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# date = list(date.split()) # Разделяем предложение на фразы и переводим в список фраз.
# print(date)

# # Применяем функцию по подсчету гласных для каждого элемента (фразы) списка.
# numb_lst = list(map(numb_of_glasnyi, date)) # и получаем список чисел, сколько в каждой фразе гласных.
# print(numb_lst)

# # Если количество раз, которое встречается первый элемент списка == длине списка, то
# # значит все элементы списка равны между собой, след-но кол-во слогов во всех фразах одинаковое.
# if numb_lst.count(numb_lst[0]) == len(numb_lst): 
#     print("Парам пам-пам")
# else:
#     print("Пам парам")



# ======================================================================================================
# Задача 36: 
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.

# Ввод: 
# print_operation_table(lambda x, y: x * y)
# Вывод:
# 1 2  3  4  5  6
# 2 4  6  8  10 12
# 3 6  9  12 15 18
# 4 8  12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def print_operation_table(func, x, y):
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            print(func(i, j), end= '\t')
        print()

num_rows = 6
num_columns = 6
print_operation_table(lambda x, y: x * y, num_rows, num_columns)

