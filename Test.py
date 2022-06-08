#  1  Знайти найменше число в списку
import numpy as np

lst1 = np.random.randint(-10, 10, 20)


def lowest(x):
    low = 0
    for i in x:
        if low > i:
            low = i
    return low


print(f"Найменше число в списку: {lowest(lst1)}")

#  2 Вивести в циклі всі парні числа до 100, крім 6, 8, 86 якщо число 90 зустрінеться в
# списку то перервати його роботу

# lst2 = np.random.randint(0, 100, 100)
lst2 = list(range(0, 100))


def odd(x):
    lst = []
    for i in lst2:
        if i == 90:
            break
        else:
            if i % 2 == 0 and i != 6 and i != 8 and i != 86:
                lst.append(i)
    return lst


print(f"Результат: {odd(lst2)}")


#  3. Написати функцію що перевіряє чи є строка правильно записаний номер телефона (+380ХХ-ХХХ-ХХ-ХХ )
# +38011-111-11-11

def telephone_number():
    number = input('Введіть номер телефону у форматі +380ХХ-ХХХ-ХХ-ХХ:')
    try:
        str1 = '+380---'
        number2 = number[:4] + number[6] + number[10] + number[13]
        number_number = number[4:6] + number[7:10] + number[11:13] + number[14:16]
        if number_number.isdigit() and len(number) == 16:
            if number2 == str1:
                a = 'правильно.'
            else:
                a = 'неправильно.'
        else:
            a = 'неправильно.'
    except Exception:  # Слишком много ошибок обрабатывать
        a = 'неправильно.'
    return print(f'Телефонний номер записано {a}')


telephone_number()


#  4. Скільки існує комбінацій пароля 4 символів, якщо відомо що друга цифра 4, 5 або 7,
#  перша не 0, третя менша 6 а четверта більша 7
print(9*3*6*2)  # first variant


def perebor():
    lst_of_pass = []
    first = range(1, 10)
    second = [4, 5, 7]
    third = range(0, 6)
    fourth = range(8, 10)
    for i1 in first:
        a = i1 * 1000
        for i2 in second:
            a += i2 * 100
            for i3 in third:
                a += i3 * 10
                for i4 in fourth:
                    a += i4
                    lst_of_pass.append(a)
    return print(len(lst_of_pass))


perebor()  # second variant


#  5. За допомогою filter залишити в списку тільки числа кратні 8
lst5 = [1, 32, 3, 213, 123, 3, 8, 88, 88888, 88]
print(list(filter(lambda x: x % 8 == 0, lst5)))

#  6. Дано список цілих чисел, порахувати скільки чисел з цього списку мають парну
#  кількість цифр
#  Приклад: [12,345,7,6,7896] -> 2
lst6 = [12, 3451, 7, 6, 7896]


def p6(x):
    a = 0
    for i in x:
        if len(str(i)) % 2 == 0:
            a += 1
    return a


print(p6(lst6))


#  8.Дано ціле число що містить тільки цифри 9 і 6, використовуючи всього одну заміну
#  цифри в числі знайти максимальне число.
#  Приклад: 9669 -> 9969
def high(x):
    y = []
    trigger = False
    for i in x:
        if not trigger:
            if i == '6':
                y.append('9')
                trigger = True
            else:
                y.append(i)
        else:
            y.append(i)
    return ''.join(y)


print(high('9669'))

#  10. Дано дві строки, перевірити чи є вони анаграмою. Тобто чи з першої строки можна
#  получить іншу за допомогою перестановок букв.


def anagram(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False


print(anagram('abba', 'baba'))


#  11 .Є файл з даними учнів у форматі Прізвище;ім’я;зріст Написати функцію що зчитує дані з
#  файлу, функцію що добавляє учня до файлу, функцію що перевіряє чи є валідним формат
#  даних що вводить користувач.
a = []
counter = 0
with open("C:\\Users\\SS\\Desktop\pup.txt", "r") as file:
    for line in file:
        print(line)
        a += line.split(';')  # записывает все значения, разделенные знаком " ; " в список " а "
        counter += 1  # Считает количество строк в файле
print(f"Number of lines: {counter}")

def data_input():
    surname = input("Введіть прізвище")
    name = input("Введіть ім'я")
    height = input("Введіть зріст")
    if height.isdigit():
        messages = [surname + ';', name + ';', height + ';', '\n']
        return messages
    else:
        return print('Error')

try:
    with open("C:\\Users\\SS\\Desktop\pup.txt", "a") as file:
        for message in data_input():
            file.write(message)
except:
    Exception


