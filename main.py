
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
            print(f'Найдено на позиции - {i}')
            print(f'Название товара: {inventory[i][0]}', end=' | ')
            print(f'Описание товара: {inventory[i][1]}', end=' | ')
            print(f'Цена товара: {inventory[i][2]}', end=' | ')
            print(f'Количество товара: {inventory[i][3]}', end=' | ')
            print(f'Категория товара: {inventory[i][4]}')
            break

        else:
            print(f'Не найдено на позиции - {i}')
def edit_option():
    index = input('Введите название: ')
    for i, row in enumerate(inventory):
        if index in row:
            inInv = row.index(index)
            print(f'Найдено на позиции - {i}')
            while True:
                doEdit = input('Что изменить (Название, Описание, Цена, Количество, Категория): ')
                if doEdit.lower() == 'название':
                    inventory[i][0] = input('Введите новое название: ')
                    break
                elif doEdit.lower() == 'описание':
                    inventory[i][0] = input('Введите новое описание: ')
                    break
                elif doEdit.lower() == 'цена':
                    inventory[i][0] = input('Введите новую цену: ')
                    break
                elif doEdit.lower() == 'количество':
                    inventory[i][0] = input('Введите новое количесво: ')
                    break
                elif doEdit.lower() == 'категория':
                    inventory[i][0] = input('Введите новую категорию: ')
                    break
                else:
                    print('Ты шо головой ударился, написанно на исконно русском языке что можно выбрать балбес')
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
while True:
    invlen = len(inventory) - 1
    print('Колво - ' + str(invlen))
    do = input('Что делать: ')
    if do.lower() == '1':
        input_and_create()
    elif do.lower() == '2':
        look_option()
    elif do.lower() == '3':
        edit_option()
    elif do.lower() == '4':
        delete_option()
    elif do.lower() == '5':
        loop = input('Продожить? y/n   ')
        if loop == 'y':
            continue
        else:
            save_inventory()
            exit()




