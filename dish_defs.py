import json
from random import randint


def file_write(name, data):  # Запись списка блюд во внешний файл для хранения
    with open(f"{name}.json", "w") as name:
        return json.dump(data, name)


def file_read(name):  # Чтение списка блюд из внешнего файла
    with open(f"{name}.json", "r") as read_dishes:
        return json.load(read_dishes)


def day_menu(dishes_dict):  # Составление случайного списка блюд на день
    for k, v in dishes_dict.items():
        rand_int = randint(0, len(v) - 1)
        print(f"{k}:  {v[rand_int]}")
    exit_prg()


def select_do():  # Функция выбора действия, добавление или удаление
    d_type = None
    if d_type is None:
        do_ans = input("Выберите действие, добавить \"+\", удалить \"-\" блюдо ")
        if do_ans == "+" or do_ans == "=":
            d_type = 1
            return d_type
        elif do_ans == "-" or do_ans == "_":
            d_type = 2
            return d_type
        else:
            a = input("Выбор некорректный. Хотите повторить? (д):")
            if a == "д" or a == "l":
                select_do()
            else:
                exit_prg()
    else:
        print("Действие выбрано")
        return d_type


def select_section(dishes_dict):
    dish_type = list((dishes_dict.keys()))
    sel_sect = None
    if sel_sect is None:
        sel_sect = input(f"Выберите, в каком разделе хотите изменить данные: {dish_type}: ")
        if sel_sect in dish_type:
            return sel_sect
        else:
            f = input("Выбор некорректный. Хотите повторить? (д)")
            if f == "l" or f == "д":
                select_section(dishes_dict)
            else:
                exit_prg()


def add_dishes(dishes_dict, sect_do):  # Добаваление блюда в список
    if sect_do is not None:
        print(f"В данном разделе уже есть следующие блюда: {dishes_dict[sect_do]}")
    added_dish = None
    if added_dish is None:
        added_dish = input("введите название нового блюда: ")
        if added_dish == "й" or added_dish == "q":
            exit_prg()
        elif added_dish in dishes_dict[sect_do]:
            f = input("Выбранное блюдо уже есть в списке. Хотите ввести другое блюдо? (д)")
            if f == "l" or f == "д":
                add_dishes(dishes_dict, sect_do)
            else:
                exit_prg()
        else:
            if len(added_dish) > 1:
                dishes_dict[sect_do].append(added_dish)
                file_write("dishes", dishes_dict)
                print(dishes_dict[sect_do])
            else:
                print("Слишком короткое название блюда")
                add_dishes(dishes_dict, sect_do)
    else:
        start_program()


def del_dish(dishes_dict, sect_do):  # Удаление блюда из списка
    key_d = 3
    while key_d > 0:
        dish_rqst = input(f"введите название удаляемого блюда: {dishes_dict[sect_do]}: ")
        while dish_rqst in dishes_dict[sect_do]:
            dishes_dict[sect_do].remove(dish_rqst)
            print("Вот что осталось: ", dishes_dict[sect_do])
            input("Нажмите ввод для продолжения ")
            key_d = 0
            file_write("dishes", dishes_dict)
            start_program()
        else:
            print("Введенное блюдо отсутствует в списке")
            key_d -= 1
    else:
        print()
        start_program()


def make_change(menu_dict, dishes_dict):
    sel_do = select_do()
    sect_do = select_section(dishes_dict)
    if sel_do == 1:
        add_dishes(dishes_dict, sect_do)
        return add_dishes()
    elif sel_do == 2:
        del_dish(dishes_dict, sect_do)
    else:
        add_dish = input("введите название блюда: ")
        return add_dish


def exit_prg():
    re_question = input("Закончить и выйти? (д/н)")
    l_ans = ["l", "L", "д", "Д", "Да", "да", "yes", "Yes"]
    if re_question in l_ans:
        quit()
    else:
        start_program()


def do_it(key_do, menu_dict, dishes_dict):
    key_3 = 3
    while key_3 > 0:
        if key_do in ["м", "m", "M", "Ь", "ь"]:
            key_3 = 0
            start_program()
        elif key_do == "g" or key_do == "п":  # Запрос на случайное меню через функцию day_menu()
            key_3 = 0
            day_menu(dishes_dict)
        elif key_do in ["b", "B", "И", "и"]:  # Изменение пункта в меню
            key_3 = 0
            make_change(menu_dict, dishes_dict)
        elif key_do == "в" or key_do == "d":  # Запрос на выход из программы
            key_3 = 0
            exit_prg()
        else:
            print("введите корректное значение!")
            key_3 -= 1


def make_menu():
    add_menu_dict = {}
    try:
        main_menu_dict = file_read("menu")
        add_menu_dict = file_read("add_menu")
    except IOError:
        main_menu_dict = {0: "Главное меню (м)", 1: "Получить меню (п)", 2: "Изменить меню (и) ", 3: "Выйти (в) "}
    dicts = list(main_menu_dict.values()) + list(add_menu_dict.values())
    menu_dict = {}
    for i in range(0, len(dicts)):
        menu_dict[i] = dicts[i]
    return menu_dict


def make_dish_menu():
    try:
        dishes_dict = file_read("dishes")
    except IOError:
        dishes_dict = {"первые блюда": ["суп"]}
    return dishes_dict


def start_program():  # Функция меню программы, продолжается до указания выхода
    menu_dict = make_menu()
    dishes_dict = make_dish_menu()
    for i in range(0, len(menu_dict)):
        print(menu_dict[i])
    key_do = input("Выберите требуемое действие: ")
    do_it(key_do, menu_dict, dishes_dict)


#start_program()
