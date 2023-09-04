# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

def getFraction(message):
    print(message)
    numerator = getDigit('Введите числитель: ')
    denumerator = getDigit('Введите знаменатель: ')
    result = numerator + '/' + denumerator
    return result


# Получить от пользователя число:
def getDigit(message):
    flag = False
    num = ''
    while flag == False:
        num = input(message)
        if num.isdigit():
            flag = True
    return num

f_1 = getFraction('Введите первую дробь')
print(f_1)

f_2 = getFraction('Введите вторую дробь')
print(f_2)

multiplication = \
    str(int(f_1.split('/')[0]) * int(f_2.split('/')[0])) + '/' + \
    str(int(f_1.split('/')[1]) * int(f_2.split('/')[1]))

f_12 = \
    str(int(f_1.split('/')[0]) * int(f_2.split('/')[1])) + '/' + \
    str(int(f_1.split('/')[1]) * int(f_2.split('/')[1]))
print(f_12)

f_21 = \
    str(int(f_2.split('/')[0]) * int(f_1.split('/')[1])) + '/' + \
    str(int(f_2.split('/')[1]) * int(f_1.split('/')[1]))
print(f_21)

f_addition = \
    str(int(f_12.split('/')[0]) + int(f_21.split('/')[0])) + '/' + \
    str(f_12.split('/')[1])

print(f'{f_1} * {f_2} = {multiplication}')
print(f'{f_1} + {f_2} = {f_addition}')