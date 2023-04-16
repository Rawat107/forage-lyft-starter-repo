import unittest

from engine.willoughby_engine import WilloughbyEngine

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
