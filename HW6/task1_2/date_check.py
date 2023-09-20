'''
Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY 
Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна. 
Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
Проверку года на високосность вынести в отдельную защищённую функцию.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.'''

MONTHS_DURATION = {'01': 31, '02': 28, '03': 31,
                   '04': 30, '05': 31, '06': 30,
                   '07': 31, '08': 31, '09': 30,
                   '10': 31, '11': 30, '12': 31,
                   }

YEAR_RANGE = [1, 9999]


def _date_format_check(entry):
    '''Проверка если аргумент это строка в формате DD.MM.YYYY.'''
    if (len(entry) == 10) & (len(entry.split('.')) == 3):
        if (len(entry.split('.')[0]) == 2) & (len(entry.split('.')[1]) == 2) & (len(entry.split('.')[2]) == 4):
            if all(map(lambda x: x.isdigit(), entry.split('.'))):
                return True
            return False
        return False
    return False


def _get_date_from_user():
    '''Получение от пользователя строкового значения в формате DD.MM.YYYY.'''
    entry = input('Введите дату в формате DD.MM.YYYY\n')
    while _date_format_check(entry) == False:
        entry = input('Неверный формат. Введите дату в формате DD.MM.YYYY\n')
    return entry


def _leap_year_check(year):
    '''Проверка, если год високосный.'''
    if int(year) % 4 == 0:
        if int(year) % 100 != 0:
            return True
        elif int(year) % 400 == 0:
            return True
        else:
            return False
    else:
        return False


def date_check(date):
    if _date_format_check(date):
        day = date.split('.')[0]
        mth = date.split('.')[1]
        year = date.split('.')[2]

        if YEAR_RANGE[0] < int(year) < YEAR_RANGE[1]:
            if not _leap_year_check(year):

                if MONTHS_DURATION.get(mth) != None:
                    if 0 < int(day) <= MONTHS_DURATION.get(mth):
                        return True
                    return False
                else:
                    return False    
                
            else:
                if MONTHS_DURATION.get(mth) != None:
                    if (mth == '02') & (0 < int(day) <= 29):
                        return True
                    elif 0 < int(day) <= MONTHS_DURATION.get(mth):
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False


