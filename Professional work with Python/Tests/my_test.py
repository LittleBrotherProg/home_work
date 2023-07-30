class unique_id:
  
    def __init__(self):
        self.ids = {'user1': [213, 213, 213, 15, 213],
                    'user2': [54, 54, 119, 119, 119],
                    'user3': [213, 98, 98, 35]}
        self.result = []

    def chec_unique(self):
       return list(set(self.result.append(id) for id in self.ids.values()))
    
import pytest

def test_unique_id():
    id = unique_id()
    result = id.chec_unique()
    assert (result.count(item)>1 for item in result)
