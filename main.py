
import csv

inventory_file_path = 'inventory.csv' # Ссылка на файл с массивом

# Загрузка массива из файла
try:
    with open(inventory_file_path, newline='', encoding='utf-8') as csvfile: # Открываем файл для сохранения в utf-8 и ставим курсор на начало строки
        reader = csv.reader(csvfile) # Создаем ссылку на содержимое массива
        inventory = list(reader) # Присваеваем значенмие файла массиву
except FileNotFoundError: # Если файла не будет, впишем стандартные значения
    inventory = [['Название', 'Описание', 'Цена', 'Колво', 'Категория']]

def save_inventory(): # Функция сохранения
    with open(inventory_file_path, 'w', newline='', encoding='utf-8') as csvfile: # Открываем файл
        writer = csv.writer(csvfile) # Создаем ссылку на запись
        writer.writerows(inventory) # Записываем весь массив в файл
invlen = len(inventory) - 1 # Очень важный костыль
def input_and_create(): #функция создания нового товара

    inventory.append([input('Введите название: '), input(f'Введите описание: '), # Спрашиваем и присваеваем введенные значенияц
                      input('Введите цену: '), input('Введите количество: '),
                      input('Введите категория: ')])

    return
def look_option(): # Функция просмотра одного элемента
    index = input('Введите название: ').lower()
    for i, row in enumerate(inventory): # Перебираем все элементы массива inventory
        if index in map(str.lower, row): # если введенное название есть в массиве
            print(f'Название товара: {inventory[i][0]}', end=' | ')
            print(f'Описание товара: {inventory[i][1]}', end=' | ')
            print(f'Цена товара: {inventory[i][2]}', end=' | ')
            print(f'Количество товара: {inventory[i][3]}', end=' | ')
            print(f'Категория товара: {inventory[i][4]}', end=' | ')
            print(f'Позиция в реестре: {i}')
            break
        elif index not in map(str.lower, [row[0] for row in inventory]): # если введенного названия нету в массиве
            print(f'Такого удивительного существа нету - {index}')
            break
        else: # Очень важная эмитация работы
            print('Поиск..')
def edit_option():
    index = input('Введите название: ').lower()
    for i, row in enumerate(inventory): # Перебираем все элементы массива inventory
        if index in map(str.lower, row): # если введенное название есть в массиве
            while True: # Бесконечный цикл который имеет конец, для выбора того что изменить
                doEdit = input('Что изменить (Название, Описание, Цена, Количество, Категория): ').lower()
                if doEdit.lower() == 'название':
                    inventory[i][0] = input('Введите новое название: ')
                    break
                elif doEdit.lower() == 'описание':
                    inventory[i][1] = input('Введите новое описание: ')
                    break
                elif doEdit.lower() == 'цена':
                    inventory[i][2] = input('Введите новую цену: ')
                    break
                elif doEdit.lower() == 'количество':
                    inventory[i][3] = input('Введите новое количесво: ')
                    break
                elif doEdit.lower() == 'категория':
                    inventory[i][4] = input('Введите новую категорию: ')
                    break
                else:
                    print('Ты что головой ударился, написанно на исконно русском языке что можно выбрать, балбес')
                    continue
            break
        elif index not in map(str.lower, [row[0] for row in inventory]):  # если введенного названия нету в массиве
            print(f'Такого удивительного существа нету - {index}')
            break
        else: # Очень важная эмитация работы
            print('Поиск..')
def delete_option(): # Функция удаления
    index = input('Введите название: ')
    for i, row in enumerate(inventory):# Перебираем все элементы массива inventory
        if index in map(str.lower, row): # если введенное название есть в массиве
            while True: # Бесконечный цикл выбора растатся ли с выбранным элементом
                do_delete = input(f'Вы точно хотите удалить: {index}? y/n ')
                if do_delete.lower() == 'y':
                    del inventory[i]
                    break
                else:
                    back = input('Вернутся назад? y/n  ') # Если мискликнул вернутся к удалению элемента, или вернуться на главную
                    if back == 'y':
                        break
                    else:
                        continue
            break
        elif index not in map(str.lower, [row[0] for row in inventory]): # если введенного названия нету в массиве
            print(f'Такого удивительного существа нету - {index}')
            break
        else: # Очень важная эмитация работы
            print('Поиск..')
def look_on_all_array(): # Функция просмотра всего массива
    for i, row in enumerate(inventory): # Перебираем все элементы массива inventory
        print(f'Название: {inventory[i][0]} | Описание: {inventory[i][1]} | Цена: {inventory[i][2]}  | Количество: {inventory[i][3]} | Категория: {inventory[i][4]}') # Выводим каждый элемент

while True: # Бесконечный цикл для постоянной работы программы
    do = input('Что делать? (Создать | Поиск | Изменить | Удалить | Выйти) : ') # Узнаем что надо выполнить
    if do.lower() == 'создать':
        input_and_create()
    elif do.lower() == 'поиск':
        print(f'Количество значений в базе - {invlen}')
        while True: # Бескочный цикл для выбора функции поиска
            oneOrAll = input('Все варианты или определенный (Все | Один): ')
            if oneOrAll.lower() == 'все':
                look_on_all_array() # Выводит весь массив
                break
            elif oneOrAll.lower() == 'один':
                look_option() # Ищет элемент по его имени
                break
            else:
                print(f'Не ну я все понимаю, но тут всего 4 буквы максимум - заруинить тут надо уметь, пепежа - {oneOrAll}') # Важная часть фэмели френдли интерфейса
    elif do.lower() == 'Изменить'.lower():
        edit_option()
    elif do.lower() == 'Удалить'.lower():
        delete_option()
    elif do.lower() == 'Выйти'.lower():
        loop = input('Выйти? y/n   ') # Удостовериваемся что пользователь не ошибся
        if loop == 'n': # Продолжаем если нет
            continue
        else: # Все остальное считаем как призыв закрыть эту страшную и ужасную программу
            save_inventory() # Сохраняем массив в csv файл
            exit()
    else:
        print(f'Ну я все понимаю, но такого мы не умеем - {do}') # Важная часть фэмели френдли интерфейса




