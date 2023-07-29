class NestedIterator:
    def __init__(self, list_of_list):
        self.result = []
        self.memory = []
        self.lol = list_of_list
        self.count_list = 0

    def __iter__(self):
        return self

    def __next__(self):
        def check_list(item):
            if isinstance(item, list):
                self.memory = item + self.memory
                if len(self.memory) == 0:
                    return
                else:
                    item = self.memory.pop(0) 
                    return check_list(item)
            else:
                self.result.append(item)
                if len(self.memory) != 0:
                    item = self.memory.pop(0) 
                    return check_list(item)

        self.all_list = len(self.lol)
        if self.all_list == self.count_list and len(self.result) == 0:
            raise StopIteration
        else:
            if len(self.result) != 0:
                return self.result.pop(0)
            else:
                items_from_the_list = self.lol[self.count_list]
                for item in items_from_the_list:
                    check_list(item)
                self.count_list += 1
                return self.__next__()
                
            



            
                            



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