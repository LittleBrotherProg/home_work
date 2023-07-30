import pytest
class unique_id:
  
    def __init__(self):
        self.ids = {'user1': [213, 213, 213, 15, 213],
                    'user2': [54, 54, 119, 119, 119],
                    'user3': [213, 98, 98, 35]}
        self.result = []

    def chec_unique(self):
        all_val = [val for sublist in self.ids.values() for val in sublist]
        return  list(set(all_val))
        

import pytest

def test_unique_id():
    id = unique_id()
    result = id.chec_unique()
    assert bool([True for item in result if result.count(item) != 2]) == True
