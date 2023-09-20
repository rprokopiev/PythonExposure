import sys
from date_check import date_check

'''
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
'''

if __name__ == '__main__':
    a = sys.argv[1:]
    date = str(a[0])
    print(date_check(date))