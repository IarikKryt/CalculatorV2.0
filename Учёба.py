def menu():
    ans = input('Для математичских действий(N), площадь(S), обьём(V). Напишите:\n')
    if ans == 'N' or ans == 'n':
        qw = input('Введите 0 для простого калькулятора, @ для процентов:\n')


def calculator():
    while True:
        print('A + B — сумма\nA - B — разность\nA * B — произведение\nA / B — частное\nA ** B — возведение в степень\nA // B — целочисленное деление\nA % B — остаток от деления.')


        calc = input("Введите математическое действие:\n")
        print("Ответ: " + str(eval(calc)))
        ex = input('Хотите продолжить?(Да/Нет):\n')

        if ex == 'Нет'or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break

        if ex == 'Да' or ex == 'да':
            print('Нажмите Enter чтобы продолжить!')
            input()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time
            time.sleep(5)
            break

def percent():
    while True:
        b = input('Введите число:\n')
        a = input('Введите число процент которого хотите узнать:\n')
        c =float(a) / float(b) * 100
        print('ответ: ' +str(c) + '%')
        ex = input('Хотите продолжить?(Да/Нет):\n')

        if ex == 'Нет' or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
            import time

            time.sleep(5)
            break

        if ex == 'Да' or ex == 'да':
            print('Нажмите Enter чтобы продолжить!')
            input()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time

            time.sleep(5)
            break
def sqare():
    while True:
        import math
        R = float(input('Введите радиус круга:\n'))
        S = math.pi * R * R
        print('Площадь круга:', S)
        ex = input('Хотите продолжить?(Да/Нет):\n')

        if ex == 'Нет' or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
            import time

            time.sleep(5)
            break

        if ex == 'Да' or ex == 'да':
            print('Нажмите Enter чтобы продолжить!')
            input()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time
            time.sleep(5)
            break

def sqare2():
    while True:
        Vex = input('Обьём квадрата(С), или обьём параллелепипеда(P):\n')

        if Vex == 'P' or Vex == 'p':
            x = input('Введите высоту:\n')
            y = input('Введите ширину:\n')
            z = input('Введите глубину:\n')
            f = float(x) * float(y) * float(z)
            print('Результат' + str(f))
            ex = input('Хотите продолжить?(Да/Нет):\n')

            if ex == 'Нет' or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break

            if ex == 'Да' or ex == 'да':
                print('Нажмите Enter чтобы продолжить!')
                    input()

        else:
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time
            time.sleep(5)
            break

def volmume():
    while True:
        cube = input('Введите сторону куба: ')
        vcube = float(cube) ** 3
        print ('Oбьём вашего куба равен: ' +str(vcube))
        ex = input('Хотите продолжить?(Да/Нет):\n')

        if ex == 'Нет' or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break

        if ex == 'Да' or ex == 'да':
            print('Нажмите Enter чтобы продолжить!')
            input()

        else:
            print('Ты что за ахинею написал. Программа отказывается это делать!!!')
            print('ПРОГРАММА СЛОМАНА, КРИТИЧЕСКИЙ СБОЙ. ЗАКРЫТИЕ НА ПОЧИНКУ ЧЕРЕЗ 5 СЕКУНД!!!')
            import time

            time.sleep(5)
            break
