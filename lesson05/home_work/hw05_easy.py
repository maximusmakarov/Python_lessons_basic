# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

"""создание директорий"""


def newdir(self):
    os.mkdir(self)


try:
    for n in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(n))
        newdir(dir_path)
        print('Директория ' + 'dir_' + str(n) + ' создана')
except FileExistsError:
    print('Такая директория уже существует')

z = input("\nВведите 'Enter' для удаления директорий")
print(z)


"""удаление директорий"""


def deldir(self):
    os.rmdir(self)


try:
    for n in range(1, 10):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(n))
        deldir(dir_path)
        print('Директория ' + 'dir_' + str(n) + ' удалена')
except FileExistsError:
    print('Уже удалена')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.


def dirlook():
    list = os.listdir()
    for i in list:
        print(i)

dirlook()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

dirname, filename = os.path.split(__file__ + '.copy')
content = open(__file__).read()
open(os.path.join(os.getcwd(), filename), 'w').write(content)
print("\nФайл копии текущего скрипта " + __file__ + '.copy' + " был успешно создан")
