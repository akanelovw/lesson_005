# -*- coding: utf-8 -*-
from room_1 import folks as Room_1
from room_2 import folks as Room_2
# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

folks = Room_1 + Room_2
print(",".join(folks))




