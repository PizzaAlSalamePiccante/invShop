
import csv

inventory_file_path = 'inventory.csv'

# Загрузка инвентаря из файла (если файл существует)
try:
    with open(inventory_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        inventory = list(reader)
except FileNotFoundError:
    inventory = [['Название', 'Описание', 'Цена', 'Колво', 'Категория']]

def save_inventory():
    with open(inventory_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(inventory)
invlen = len(inventory) - 1
def input_and_create(): #функция создания нового товара

    inventory.append([input('Введите название: '), input(f'Введите описание: '),
                      int(input('Введите цену: ')), int(input('Введите количество: ')),
                      input('Введите категория: ')])

    return
def look_option():
    index = input('Введите название: ')
    for i, row in enumerate(inventory):
        if index in row:
            inInv = row.index(index)
            print(f'Название товара: {inventory[i][0]}', end=' | ')
            print(f'Описание товара: {inventory[i][1]}', end=' | ')
            print(f'Цена товара: {inventory[i][2]}', end=' | ')
            print(f'Количество товара: {inventory[i][3]}', end=' | ')
            print(f'Категория товара: {inventory[i][4]}', end=' | ')
            print(f'Позиция в реестре: {i}')
            break

        else:
            print('Поиск..')
def edit_option():
    index = input('Введите название: ')
    for i, row in enumerate(inventory):
        if index in row:
            inInv = row.index(index)
            while True:
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
                    print('Ты шо головой ударился, написанно на исконно русском языке что можно выбрать, балбес')
                    continue
            break
        else:
            print(f'Не найдено на позиции - {i}')
            break
def delete_option():
    index = input('Введите название: ')
    for i, row in enumerate(inventory):
        if index in row:
            inInv = row.index(index)
            while True:
                do_delete = input(f'Вы точно хотите удалить: {index}? y/n ')
                if do_delete.lower() == 'y':
                    del inventory[i]
                    break
                else:
                    back = input('Вернутся назад? y/n  ')
                    if back == 'y':
                        break
                    else:
                        continue
            break

        else:
            print(f'Не найдено на позиции - {i}')
def look_on_all_array():
    for i, row in enumerate(inventory):
        print(f'Название: {inventory[i][0]} | Описание: {inventory[i][1]} | Цена: {inventory[i][2]}  | Количество: {inventory[i][3]} | Категория: {inventory[i][4]}')

while True:
    invlen = len(inventory) - 1
    do = input('Что делать? (Создать | Просмотреть | Изменить | Удалить | Выйти) : ')
    if do.lower() == 'Создать'.lower():
        input_and_create()
    elif do.lower() == 'Просмотреть'.lower():
        print(f'Количество значений в базе - {invlen}')
        while True:
            oneOrAll = input('Все варианты или определенный (Все | Один): ')
            if oneOrAll.lower() == 'все':
                look_on_all_array()
                break
            elif oneOrAll.lower() == 'один':
                look_option()
                break
            else:
                print(f'Я все понимаю но такого сделать не могу, хоть убей - {oneOrAll}')
    elif do.lower() == 'Изменить'.lower():
        edit_option()
    elif do.lower() == 'Удалить'.lower():
        delete_option()
    elif do.lower() == 'Выйти'.lower():
        loop = input('Выйти? y/n   ')
        if loop == 'n':
            continue
        else:
            save_inventory()
            exit()
    else:
        print(f'Ну я все понимаю, но такого мы не умеем - {do}')




