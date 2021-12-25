

class FlatIterator:
    def __init__(self, item_list):
        self.item_list = item_list

    def __iter__(self):
        self.outer_list_curs = 0
        self.inner_list_curs = -1
        return self

    def __next__(self):
        if (self.outer_list_curs == len(self.item_list) - 1)\
                and (self.inner_list_curs == len(self.item_list[self.outer_list_curs]) - 1):
            raise StopIteration
        elif self.inner_list_curs < len(self.item_list[self.outer_list_curs]) - 1:
                self.inner_list_curs += 1
        else:
            self.outer_list_curs += 1
            self.inner_list_curs = 0
            return self.item_list[self.outer_list_curs][0]
        return self.item_list[self.outer_list_curs][self.inner_list_curs]


class FlatIterator_pro:
    def __init__(self, item_list):
        self.item_list = item_list
        self.tmp_list = []

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if len(self.item_list) > self.cursor:
            while True:
                if isinstance(self.item_list[self.cursor], list):
                    self.tmp_list.extend(self.item_list.pop(self.cursor))
                    for id, val in enumerate(self.tmp_list):
                        self.item_list.insert(self.cursor + id, val)
                    self.tmp_list.clear()
                else:
                    self.cursor += 1
                    return self.item_list[self.cursor-1]
        else:
            raise StopIteration


def flat_generator(list_item):
    cursor_global = 0
    cursor_local = 0
    while cursor_global < len(list_item):
        while cursor_local < len(list_item[cursor_global]):
            yield list_item[cursor_global][cursor_local]
            cursor_local += 1
        cursor_global += 1
        cursor_local = 0
    return

def flat_generator_pro(list_item):
    for elmt in list_item:
        if isinstance(elmt, list):
            for inner in flat_generator_pro(elmt):
                yield inner
        else:
            yield elmt
    return


if __name__ == '__main__':
    # итератор
    print('Вывод при помощи ИТЕРАТОРА списка:')
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)
    #===============================================================

    # итератор с любым уровнем вложенности
    print('\nВывод при помощи ИТЕРАТОРА списка любой глубины вложенности:')
    nested_list = [
        [['a', 'b'], 'c'],
        [['d', 'e', 'f'], [1, [2, None]]]
    ]
    for item in FlatIterator_pro(nested_list):
        print(item)
    # ===============================================================

    # генератор
    print('\nВывод при помощи ГЕНЕРАТОРА списка:')
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None]
    ]
    for item in flat_generator(nested_list):
        print(item)
    #===============================================================

    # генератор с любым уровнем вложенности
    print('\nВывод при помощи ГЕНЕРАТОРА списка любой глубины вложенности:')
    nested_list = [
        [['a', 'b'], 'c'],
        [['d', 'e', 'f'], [1, [2, None]]],
    ]
    for item in flat_generator_pro(nested_list):
        print(item)