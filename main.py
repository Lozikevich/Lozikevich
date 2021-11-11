import cmath
import math
import random
from random import choice

ch = 'y'
while ch == 'y':
    def is_digit(x):
        if x.isdigit():
            return True
        else:
            try:
                float(x)
                return True
            except ValueError:
                return False
# Объявление переменной a
    print('Введите коэффициент a:')
    a = input()
    n=0
    while not is_digit(a):
        print('Используйте в качестве коэффициентов только числовые значения', '\nПовторно введите коэффициент a:')
        a = input()
        n=n+1
        if is_digit(a):
            break
        if n>2:
            print(random.choice(['В этот раз подумайте хорошенько', 'Давайте попробуем еще раз', 'Скорее всего сегодня получится']))
    a=float(a)

# Объявление переменной b
    print('Введите коэффициент b:')
    b = input()
    n = 0
    while not is_digit(b):
        print('Используйте в качестве коэффициентов только числовые значения', '\nПовторно введите коэффициент b:')
        b = input()
        n = n + 1
        if is_digit(b):
            break
        if n > 2:
            print(random.choice(
                ['В этот раз подумайте хорошенько', 'Давайте попробуем еще раз', 'Скорее всего сегодня получится']))
    b = float(b)

# Объявление переменной c
    print('Введите коэффициент c:')
    c = input()
    n = 0
    while not is_digit(c):
        print('Используйте в качестве коэффициентов только числовые значения', '\nПовторно введите коэффициент c:')
        c = input()
        n = n + 1
        if is_digit(c):
            break
        if n > 2:
            print(random.choice(
                ['В этот раз подумайте хорошенько', 'Давайте попробуем еще раз', 'Скорее всего сегодня получится']))
    c = float(c)
# Расчет корней уравнения
    if b * b - 4 * a * c < 0:
        print('Уравнение с заданными коэффициентами имеет комплексные корни:',
            '\n x1=', ((- b / 2 * a - cmath.sqrt(b * b - 4 * a * c)) / 2 * a),
            '\n x2=', ((- b / 2 * a + cmath.sqrt(b * b - 4*a*c)) / 2 * a))
    else:
        print('Уравнение с заданными коэффициентами имеет действительные корни:',
            '\n x1=', ((- b / 2 * a - math.sqrt(b * b - 4 * a * c)) / 2 * a),
            '\n x2=', ((- b / 2 * a + math.sqrt(b * b - 4 * a * c)) / 2 * a))

    print('Задать новые коэффициенты y/n?')
    ch = input()
    if ch == 'n':
        break