import unittest

from engine.sternman_engine import SternmanEngine

class TestStermanEngine(unittest.TestCase):
  def Car_service_is_due(self):
    '''
    Test will return True
    when the warning light is on
    '''
    test_engine = SternmanEngine(True)
    self.asserTrue(test_engine.needs_service())

  def Car_service_is_not_due(self):
    '''
    Test will return False
    when the warning light is off
    '''
    test_engine = SternmanEngine(False)
    self.asserTrue(test_engine.needs_service())

if __name__ == '__main__':
  unittest.main()
