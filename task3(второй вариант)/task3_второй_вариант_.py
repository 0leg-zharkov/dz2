month = int(input('Введите номер месяца: '))
while month < 0 or month > 12:
    month = int(input('Неверно, введите номер месяца: '))

seasons = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
           8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn', 12: 'winter'}
print(seasons[month])

# Реализация через list.
month = int(input('Введите номер месяца: '))
while month < 0 or month > 12:
    month = int(input('Неверно, введите номер месяца: '))
seasons = ('winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn',
           'autumn', 'осень', 'зима')
print(seasons[month - 1])

