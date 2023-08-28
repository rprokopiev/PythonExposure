# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код:
#       from random import randint
#       num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

GUESS = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(num)

i = 1

flag = False
while i <= GUESS:
    entry = input(f'Угадай число от 0 до 1000. Попытка № {i}: ')
    if num == int(entry):
        print(f'Угадано. Потребовалось {i} попыток')
        flag = True
        break
    elif num < int(entry):
        print(f'Загаданное число меньше. Осталось {GUESS - i} попыток')
    else:
        print(f'Загаданное число больше. Осталось {GUESS - i} попыток')
    i += 1
if flag == False: print('Конец')


