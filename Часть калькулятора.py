ans = input('Для математичских действий(N), площадь(S), обьём(V). Напишите:')
if ans == 'N' or ans == 'n':
    Qw = input('Введите 0 для простого калькулятора, @ для процентов:')
    while True:
        if Qw == '0':
            calc = input("Введите математическое действие:\n")
            print("Ответ: " + str(eval(calc)))
            ex = input('Хотите продолжить?(Да/Нет):')
            if ex == 'Нет'or ex == 'нет':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break
            if ex == 'Да' or ex == 'да':
                print('Нажмите Enter чтобы продолжить!')
                input()
        if Qw == '@':
            b = input('Введите число:')
            a = input('Введите число процент которого хотите узнать:')
            c =float(a) / float(b) * 100
            print('ответ: ' +str(c))
            ex = input('Хотите продолжить?(Да/Нет):')
            if ex == 'Нет' or ex == 'нет':
                print('Программа закроется через 5 секунд!!!')
                import time
                time.sleep(5)
                break
            if ex == 'Да' or ex == 'да':
                print('Нажмите Enter чтобы продолжить!')
                input()
while True:
    if ans == 'S' or ex == 's':
        import math
        R = float(input('Введите радиус круга:'))
        S = math.pi * R * R
        print('Площадь круга:', S)
        ex = input('Хотите продолжить?(Да/Нет):')
        if ex == 'Нет' or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
            import time
            time.sleep(5)
            break
        if ex == 'Да' or ex == 'да':
            print('Нажмите Enter чтобы продолжить!')
            input()
if ans == 'S' or ex == 's':
    Vex = input('Площадь квадрата(С), или площадь параллелепипеда(P)')
    if Vex == 'C' or Vex == 'c':
        a = input('Введите высоту:')
        b = input('Введите ширину:')
        с = input('Введите глубину:')
        d = a * b * c
        print('Результат' +str(d))
        ex = input('Хотите продолжить?(Да/Нет):')
        if ex == 'Нет' or ex == 'нет':
            print('Программа закроется через 5 секунд!!!')
            import time

            time.sleep(5)
            break
        if ex == 'Да' or ex == 'да':
            print('Нажмите Enter чтобы продолжить!')
            input()
