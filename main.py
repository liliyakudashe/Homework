# file_brodsky = 'brodsky.txt'
# file = open(file_brodsky, 'r')
# # file_content = file.read()
# # print(file_content)
# file.close()
# import os
#
# print('*' * 30)
# bro = 'brodskySkyros.txt'
# if not os.path.exists('myPoem.txt'):
#     with open(file='myPoem.txt', mode='w', encoding='utf-8') as file:
#         with open(bro, 'r', encoding='utf-8') as my_file:
#             rea = my_file.readline()
#             file.write(rea)
#
#
# with open('myPoem.txt', 'r', encoding='utf-8') as my_file:
#     rea = my_file.readline()
#     print(rea)

class InOutBlock:

    def __enter__(self):   # Выполняется при входе
        print('Входим в блок кода')  #

    def __exit__(self, exc_type, exc_val, exc_tb):   # Выполняется при выходе
        print(f'Выходим из блока кода {exc_type}, {exc_val}, {exc_tb}')  # В тексте упомин.ошиб.параметр кот.наход в zip
        return True    # Возвращаем истину, чтобы погасить полёт исключения


with InOutBlock() as in_out:  # Программа входит в блок-кода
    print('Работаем...')    # Выполняет первую строку
    a = bla_bla / number    # Затем возникает ошибочная ситуация связанная с неопределённой переменной
    print('Вычислили значение')   # Ошибка обрабатывается в блоке zip связанных с ошибкой
print('После контекстного менеджера')   # особенность менеджера-возвращать значения и функции zip,
# Если значение True - исключение обработано, его больше не надо вызывать

print(InOutBlock)
print(in_out)
print(exit())
