# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

number = int(input('Enter number: '))
base = 16

original_number = number
result_number = ''
replacement_letters = ['A', 'B', 'C', 'D', 'E', 'F']

while number:
    l = ''
    if (number%base >= 10):
        l = replacement_letters[int(str(number%base)[len(str(number%base)) - 1])]
        result_number = l + result_number
        number //= base
    result_number = str(number%base) + result_number
    number //= base

print(f'{result_number} is {original_number} in 16 numeral system')
print(hex(original_number)[2:])