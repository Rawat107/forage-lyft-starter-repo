import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
  def car_service_is_due(self):
    """
    Test will return True
    when the mileage difference is over 30000
    """
    last_service_mileage = 0
    current_mileage = 30001
    test_engine = CapuletEngine(current_mileage, last_service_mileage)
    self.assertTrue(test_engine.needs_service())

  def car_service_is_not_due(self):
    """
    Test will return False
    when the mileage difference is under 30000
    """
    last_service_mileage = 30001
    current_mileage = 30100
    test_engine = CapuletEngine(current_mileage, last_service_mileage)
    self.assertFalse(test_engine.needs_service())

  def car_service_is_not_due_case2(self):
    """
    Test will return False
    when the mileage difference is at 30000
    """
    test_engine = CapuletEngine(current_mileage=30000, last_service_mileage=0)
    self.assertFalse(test_engine.needs_service())

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

class TestWilloughbyEngine(unittest.TestCase):
  def car_service_is_due(self):
    """
    Test will return True
    when the mileage difference is over 60000
    """
    last_service_mileage = 0
    current_mileage = 60001
    test_engine = WilloughbyEngine(current_mileage, last_service_mileage)
    self.assertTrue(test_engine.needs_service())

  def car_service_is_not_due(self):
    """
    Test will return False
    when the mileage difference is under 60000
    """
    last_service_mileage = 60000
    current_mileage = 60022
    test_engine = WilloughbyEngine(current_mileage, last_service_mileage)
    self.assertFalse(test_engine.needs_service())

  def car_service_is_not_due_case2(self):
    """
    Test will return False
    when the mileage difference is at 60000
    """
    test_engine = WilloughbyEngine(current_mileage=60000, last_service_mileage=0)
    self.assertFalse(test_engine.needs_service())

if __name__ == '__main__':
  unittest.main()
