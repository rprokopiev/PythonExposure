# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# Получить от пользователя число в нужном диапазоне:
def getNeededValue(message, min, max):
    num = int(getDigit(message))
    while num not in range(min, max + 1):
        num = getDigit(message)
    return num

# Получить от пользователя число:
def getDigit(message):
    flag = False
    num = ''
    while flag == False:
        num = input(message)
        if num.isdigit():
            flag = True
    return num

a = getNeededValue('Введите число от 1 до 10000: ', 1, 10000)
result = ''

if (a % 2 != 0) & (a != 1):
    for i in range(3, (a + 1), 2):
        if i == a:
            continue        
        if a % i == 0:
            result = 'Число составное'
            break
    else: 
        result = 'Число простое'    
else:
    result = 'Число составное'

print(result)