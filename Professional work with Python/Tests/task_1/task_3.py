class check_like():
  
  def __init__(self, stats):
    self.stats = stats

  def max_like(self):
    return [key for key, value in self.stats.items() if value == max(self.stats.values())][0]

import pytest

@pytest.fixture
def start():
  stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
  class_incidentalization = check_like(stats)
  return class_incidentalization.max_like()

def test_max_like(start):
  test = start
  assert "yandex" == test
  