import unittest

from tires.base import InvalidValueException, ArrayLenException
from tires.octoprimetires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
  def sum_under_margin(self):
    """
    Should return False
    when sum of val is under margin
    """
    tire_wear = [0.1, 0.2, 0.3, 0.4]
    test_tires = OctoprimeTires(tire_wear)
    self.assertFalse(test_tires.needs_service())

  def sum_over_margin(self):
    '''
    should return True
    when the sun of val is over margin
    '''
    tire_wear = [1.0, 1.0, 1.0, 1.0]
    test_tires = OctoprimeTires(tire_wear)
    self.assertTrue(test_tires.needs_service())

  def sum_at_margin(self):
    '''
    should return True
    when the sum of val is at the margin
    '''
    tire_wear = [0.2, 0.8, 1.0, 1.0]
    test_tires = OctoprimeTires(tire_wear)
    self.assertTrue(test_tires.needs_service())

  def value_not_in_range(self):
    '''
    Should raise an error
    when value is over the range of (0-1.0)
    '''
    tire_wear = [0.3, 1.1, 0.6, 0.7]
    test_tires = OctoprimeTires(tire_wear)
    self.assertRaises(InvalidValueException, test_tires.needs_service())

  def Array_len_is_not_four(self):
    '''
    SHould raise an error
    when array is shorter than four
    '''
    tire_wear = [0.2, 0.3]
    test_tires = OctoprimeTires(tire_wear)
    self.assertRaises(ArrayLenException, test_tires.needs_service())


if __name__ == '__main__':
  unittest.main()
