import unittest

from engine.capulet_engine import CapuletEngine

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

if __name__ == '__main__':
  unittest.main()
