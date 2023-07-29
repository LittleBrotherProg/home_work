class FlatIterator:

    def __init__(self, list_of_list):
        self.l_of_l = list_of_list
        self.my_list = []
        self.all_list = len(self.l_of_l)
        self.count_all_list = 0
        self.count_list = 0

    def __iter__(self):
        print('Старт цикла')
        return self

    def __next__(self):
        if self.count_all_list != self.all_list:
            self.items = len(self.l_of_l[self.count_all_list])
            if self.count_list == self.items:
                self.count_all_list += 1
                if self.count_all_list == self.all_list:
                    print('Конец цикла')
                    raise StopIteration
                else:
                    self.count_list = 0    
            self.item = self.l_of_l[self.count_all_list][self.count_list]
            self.my_list.append(self.item)
            self.count_list += 1
            return self.item
                

            


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()