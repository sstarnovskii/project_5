# Project file.
import local as lc
lang = input(lc.LANG)
while lang != '1' and lang != '2':
    print(lc.ERR)
    lang = input(lc.LANG)
if lang == '1':
    import local_en as lc
else:
    import local_ru as lc
option = input(lc.WTD)
while option != '1' and option != '2':
    print(lc.ERR)
    option = input(lc.WTD)
if option == '1':
    name = input(lc.NAME)
    try:
        with open(name, 'r') as file:
            print(file.readlines)
    except FileNotFoundError:
        print(lc.NOT_FOUND)
        create = input(lc.NEW_FILE)
        while create != '1' and create != '2':
            print(lc.ERR)
            create = input(lc.NEW_FILE)
