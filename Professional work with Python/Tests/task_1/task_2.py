class sorting:

    def __init__(self):
        self.geo_log = [
                        {'visit1': ['Москва', 'Россия']},
                        {'visit2': ['Дели', 'Индия']},
                        {'visit3': ['Владимир', 'Россия']},
                        {'visit4': ['Лиссабон', 'Португалия']},
                        {'visit5': ['Париж', 'Франция']},
                        {'visit6': ['Лиссабон', 'Португалия']},
                        {'visit7': ['Тула', 'Россия']},
                        {'visit8': ['Тула', 'Россия']},
                        {'visit9': ['Курск', 'Россия']},
                        {'visit10': ['Архангельск', 'Россия']}
                    ]
    
    def sort(self):
        result = []
        for visit in self.geo_log:
            for items in visit.values():
                if items[1] == 'Россия':
                    result.append(visit)
        return result
    

import pytest

@pytest.fixture
def start():
    sort = sorting()
    return sort.sort()


def test_sort(start):
    assert True == bool([True for num in range(len(start)) if start[num].get(list(start[num].keys())[0])[1] == 'Россия'])
