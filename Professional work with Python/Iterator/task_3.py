class NestedIterator:
    def __init__(self, list_of_list):
        self.result = []
        self.lol = list_of_list
        self.count_list = 0
        self.memory = [self.lol[self.count_list]]

    def __iter__(self):
        return self

    def __next__(self):
        self.all_list = len(self.lol)
        if len(self.memory) == 0:
                self.count_list += 1
                if self.all_list == self.count_list and len(self.memory) == 0:
                    raise StopIteration
                self.memory = [self.lol[self.count_list]]
                return self.__next__()
        else:
            self.item = self.memory.pop(0)
            if isinstance(self.item, list):
                self.memory = self.item + self.memory
                return self.__next__()
            else:
                return self.item

      
                
            



            
                            



def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            NestedIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(NestedIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()